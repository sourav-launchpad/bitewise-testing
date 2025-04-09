import streamlit as st
import openai
import pandas as pd
import time
from datetime import datetime
import os
from dotenv import load_dotenv
import asyncio
import aiohttp
from prompts import (
    get_meal_prompt, 
    SYSTEM_PROMPT,
    DIETARY_REQUIREMENTS,
    IMPORTANT_RULES,
    AUTHENTIC_RECIPE_NAMES
)
import random
import re
from difflib import SequenceMatcher

# Load environment variables
load_dotenv()

# Set OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Common household measurements with focus on Australian staples
COMMON_MEASUREMENTS = {
    "can": ["chickpeas", "tomatoes", "coconut milk", "lentils", "beans", "tuna"],  # 400g standard
    "bunch": ["green onions", "parsley", "coriander", "mint"],  # Common fresh herbs
    "head": ["garlic", "lettuce", "cabbage"],  # Whole vegetables
    "whole": ["lemon", "lime", "orange", "potato", "onion", "carrot"],  # Individual items
    "package": ["frozen vegetables", "frozen peas", "frozen corn", "mixed vegetables"],  # Frozen options
    "kg": ["chicken thighs", "beef mince", "pork shoulder", "potatoes", "rice", "onions", "carrots"],  # Bulk items
    "gram": ["cheese", "greek yogurt", "butter"],  # Dairy products
    "slice": ["bread", "toast"],  # Bread products
    "dozen": ["eggs"],  # Eggs
    "unit": ["zucchini", "cucumber", "capsicum", "eggplant"]  # Individual vegetables
}

# Categories focused on Australian budget-friendly options
CATEGORIES = {
    "Fresh & Frozen Produce": [
        # Budget-friendly fresh vegetables
        "potato", "onion", "carrot", "cabbage", "pumpkin", "sweet potato",
        # Seasonal vegetables
        "zucchini", "cucumber", "capsicum", "eggplant", "broccoli", 
        # Frozen vegetables
        "frozen vegetables", "frozen peas", "frozen corn", "mixed vegetables"
    ],
    "Budget Proteins": [
        # Affordable meats
        "chicken thigh", "beef mince", "pork shoulder", "whole chicken",
        # Budget-friendly proteins
        "egg", "lentil", "chickpea", "black bean", "tuna", "sardine"
    ],
    "Dairy & Eggs": [
        "greek yogurt", "cheese", "milk", "butter", "egg"
    ],
    "Affordable Grains": [
        "rice", "pasta", "oat", "couscous", "bread", "noodle"
    ],
    "Pantry Essentials": [
        "tomato paste", "canned tomato", "stock cube", "flour", "sugar"
    ],
    "Herbs & Spices": [
        # Common herbs
        "parsley", "coriander", "mint", "basil",
        # Essential spices
        "cumin", "coriander", "paprika", "curry powder", "mixed herbs"
    ],
    "Sauces & Condiments": [
        "oil", "soy sauce", "vinegar", "tomato sauce", "bbq sauce", "mayonnaise"
    ]
}

# Standard cup measurements
STANDARD_MEASUREMENTS = {
    "1 cup": 250,      # ml
    "3/4 cup": 180,    # ml
    "2/3 cup": 160,    # ml
    "1/2 cup": 125,    # ml
    "1/3 cup": 80,     # ml
    "1/4 cup": 60,     # ml
    "1 tbsp": 15,      # ml
    "1 tsp": 5,        # ml
}

# Set page config
st.set_page_config(
    page_title="BiteWise",
    page_icon="🍽️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin: 0 auto;
        padding: 1rem 0;
    }
    .stButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .stButton>button {
        width: 200px;  /* Smaller width */
        background-color: #2ecc71;  /* Solid green color */
        color: white;  /* White text */
        border: none;  /* Remove border */
        border-radius: 5px;  /* Rounded corners */
        padding: 0.5rem 1rem;  /* Smaller padding */
        font-size: 1rem;  /* Smaller font size */
        margin: 0 auto;  /* Center the button */
        font-weight: bold;  /* Bold text */
    }
    .stButton>button:hover {
        background-color: #2ecc71;  /* Keep same green color */
        color: black;  /* Black text on hover */
    }
    .stButton>button:active {
        background-color: #2ecc71;  /* Keep same green color */
        color: black !important;  /* Force black text when pressed */
    }
    .stButton>button:focus {
        background-color: #2ecc71;  /* Keep same green color */
        color: black !important;  /* Force black text when focused */
    }
    .stButton>button:visited {
        background-color: #2ecc71;  /* Keep same green color */
        color: black !important;  /* Force black text after visited */
    }
    .stButton>button:active:focus {
        background-color: #2ecc71;  /* Keep same green color */
        color: black !important;  /* Force black text when active and focused */
    }
    .stButton>button:active:hover {
        background-color: #2ecc71;  /* Keep same green color */
        color: black !important;  /* Force black text when active and hovered */
    }
    .meal-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    div.stSpinner > div {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    /* TEMPORARILY COMMENTED OUT: Generation time CSS
    .generation-time {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 14px;
        z-index: 1000;
    }
    */
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'meal_plan' not in st.session_state:
    st.session_state.meal_plan = None

def get_user_preferences():
    try:
        # Center the title using HTML
        st.markdown("<h1 style='text-align: center;'>🍽️ BiteWise - Personalized Meal Planner 🍽️</h1>", unsafe_allow_html=True)

        # Create three columns for better layout
        col1, col2, col3 = st.columns(3)

        with col1:
            # Use number_input with increment/decrement buttons, restricted to 1-7, default 1
            num_days = st.number_input(
                "**Number of Days**",
                min_value=1,
                max_value=7,
                value=1,
                step=1
            )
            
            # Multi-select for diet types
            diet = st.multiselect(
                "**Diet Type**",
                options=[
                    "None",
                    "Whole30",
                    "Paleo",
                    "Ketogenic (Keto)",
                    "Low-carb / High-protein",
                    "High-carb / Low-fat",
                    "Plant-based",
                    "Whole food plant-based",
                    "Vegan",
                    "Vegetarian (Lacto-ovo, Lacto, Ovo)",
                    "Pescatarian",
                    "Flexitarian",
                    "Pegan (Paleo + Vegan hybrid)",
                    "DASH (Dietary Approaches to Stop Hypertension)",
                    "MIND Diet (Mediterranean-DASH hybrid)",
                    "Intermittent Fasting (e.g. 16:8, 5:2)",
                    "Kosher",
                    "Halal",
                    "Jain",
                    "Buddhist",
                    "Seventh-day Adventist",
                    "Rastafarian Ital"
                ],
                default=[],  # Start with empty selection
                placeholder="Choose an option"
            )
            
            # If no option is selected, set to "None"
            if not diet:
                diet = ["None"]
            # If "None" is selected along with other options, clear other selections
            elif "None" in diet and len(diet) > 1:
                diet = ["None"]
            
            # Multi-select for allergies/intolerances
            allergies = st.multiselect(
                "**Allergies/Intolerances**",
                options=[
                    "No allergies or intolerances",
                    "Peanut allergy",
                    "Tree nut allergy (e.g. almond, cashew, walnut)",
                    "Shellfish allergy",
                    "Fish allergy",
                    "Egg allergy",
                    "Milk allergy (cow's milk protein: casein and/or whey)",
                    "Soy allergy",
                    "Wheat allergy",
                    "Sesame allergy",
                    "Mustard allergy",
                    "Lupin allergy",
                    "Celery allergy",
                    "Lactose intolerance",
                    "Gluten intolerance / Non-celiac gluten sensitivity",
                    "Fructose intolerance (hereditary or malabsorption)",
                    "Histamine intolerance",
                    "Salicylate sensitivity",
                    "FODMAP intolerance",
                    "Sulphite sensitivity",
                    "MSG sensitivity",
                    "Caffeine sensitivity",
                    "Alcohol intolerance",
                    "Artificial sweetener sensitivity",
                    "Food additive intolerance (e.g. preservatives, colourings)"
                ],
                default=[],  # Start with empty selection
                placeholder="Choose an option"
            )
            
            # If no option is selected, set to "No allergies or intolerances"
            if not allergies:
                allergies = ["No allergies or intolerances"]
            # If "No allergies or intolerances" is selected along with other options, clear other selections
            elif "No allergies or intolerances" in allergies and len(allergies) > 1:
                allergies = ["No allergies or intolerances"]

        with col2:
            # Multi-select for health conditions
            health_conditions = st.multiselect(
                "**Health Conditions**",
                options=[
                    "None",
                    # Metabolic & Endocrine 
                    "Type 1 Diabetes", "Type 2 Diabetes", "Prediabetes / Insulin Resistance", "Metabolic Syndrome",
                    "PCOS", "Hypothyroidism / Hashimoto's", "Hyperthyroidism / Graves'", "Adrenal Fatigue",
                    "Cushing's Syndrome", "Gestational Diabetes",
                    # Cardiovascular & Blood
                    "Hypertension", "High Cholesterol / Dyslipidemia", "Cardiovascular Disease", "Stroke prevention",
                    "Congestive Heart Failure", "Anticoagulant therapy (e.g. stable vitamin K for Warfarin)",
                    "Anaemia (Iron, B12, Folate)",
                    # Gastrointestinal
                    "Celiac Disease", "IBS (Irritable Bowel Syndrome)", "IBD (Crohn's, Ulcerative Colitis)",
                    "GERD / Acid Reflux", "Peptic Ulcers", "Diverticulosis / Diverticulitis", "Gallbladder disease",
                    "Pancreatitis", "Gastroparesis", "Liver disease / Fatty liver", "Bile acid malabsorption",
                    "SIBO (Small Intestinal Bacterial Overgrowth)",
                    # Kidney, Liver, Gout
                    "Chronic Kidney Disease (CKD)", "Kidney stones", "Nephrotic syndrome", "Gout", "Hemochromatosis",
                    "Liver Cirrhosis",
                    # Cancer & Treatment Recovery
                    "Cancer-related weight loss / Cachexia", "Neutropenic diet (immunosuppressed)",
                    "Low-residue diet (during flare-ups or treatment)",
                    # Autoimmune & Immune Conditions
                    "Lupus", "Rheumatoid Arthritis", "Psoriasis", "Multiple Sclerosis", "Eczema",
                    "Chronic hives / urticaria", "Mast Cell Activation Syndrome (MCAS)",
                    # Neurological & Mental Health
                    "Epilepsy (Keto for seizures)", "ADHD", "Autism Spectrum Disorder", "Depression / Anxiety",
                    "Migraine / Vestibular migraine", "Alzheimer's / Dementia", "Parkinson's Disease",
                    # Muscle, Bone, Joint
                    "Osteoporosis", "Osteopenia", "Sarcopenia / Muscle loss", "Arthritis (Osteoarthritis, Gout, RA)",
                    # Reproductive & Hormonal
                    "Endometriosis", "PMS / PMDD", "Fertility (male and female)", "Pregnancy (Trimester-specific)",
                    "Breastfeeding", "Menopause", "Erectile dysfunction",
                    # Weight & Nutrition Risk
                    "Overweight / Obesity", "Underweight / Malnutrition", "Muscle gain",
                    "Bariatric surgery (pre and post-op)", "Disordered eating / ED recovery", "Cachexia",
                    # Skin Conditions
                    "Acne", "Rosacea", "Eczema", "Psoriasis"
                ],
                default=[],  # Start with empty selection
                placeholder="Choose an option"
            )
            
            # If no option is selected, set to "None"
            if not health_conditions:
                health_conditions = ["None"]
            # If "None" is selected along with other options, clear other selections
            elif "None" in health_conditions and len(health_conditions) > 1:
                health_conditions = ["None"]

            # Multi-select for meal type
            meal_type = st.multiselect(
                "**Meal Type Preference**",
                options=["All", "Breakfast", "Lunch", "Dinner"],
                default=[],  # Start with empty selection
                placeholder="Choose an option"
            )
            
            # If no option is selected, set to "All"
            if not meal_type:
                meal_type = ["All"]
            # If "All" is selected along with other options, clear other selections
            elif "All" in meal_type and len(meal_type) > 1:
                meal_type = ["All"]

            # Multi-select for cuisine
            cuisine = st.multiselect(
                "**Preferred Cuisine**",
                options=[
                    "All",
                    "Mediterranean",
                    "Thai",
                    "Chinese",
                    "Japanese",
                    "Korean",
                    "Vietnamese",
                    "Indian",
                    "Middle Eastern",
                    "Latin American / Mexican",
                    "African",
                    "Nordic / Scandinavian",
                    "Traditional Australian / British / American",
                    "Eastern European",
                    "Caribbean"
                ],
                default=[],  # Start with empty selection
                placeholder="Choose an option"
            )
            
            # If no option is selected, set to "All"
            if not cuisine:
                cuisine = ["All"]
            # If "All" is selected along with other options, clear other selections
            elif "All" in cuisine and len(cuisine) > 1:
                cuisine = ["All"]

        with col3:
            budget = st.selectbox(
                "**Budget**",
                options=["Tight budget ($3-$7)", "Moderate budget ($8-$15)", 
                        "Generous budget ($16-$30)", "No budget constraints ($31+)"],
                index=1  # Default to "Moderate budget"
            )
            
            time_constraint = st.selectbox(
                "**Available Time for Cooking**",
                options=["Busy schedule (15 mins)", "Moderate schedule (30 mins)", 
                        "Busy on some days (45 mins)", "Flexible Schedule (60 mins)", 
                        "No Constraints (Any duration)"],
                index=1  # Default to "Busy on some days"
            )
            
            # Changed from selectbox to number_input for serving size
            serving_size = st.number_input(
                "**Number of Servings per Meal**",
                min_value=1,
                max_value=8,
                value=2,  # Default to 2 servings
                step=1
            )

        # Create a dictionary with all preferences
        preferences = {
            "num_days": int(num_days),  # Ensure it's an integer
            "diet": str(diet),  # Ensure it's a string
            "health_conditions": str(health_conditions),  # Ensure it's a string
            "meal_type": str(meal_type),  # Ensure it's a string
            "cuisine": str(cuisine),  # Ensure it's a string
            "budget": str(budget),  # Ensure it's a string
            "time_constraint": str(time_constraint),  # Ensure it's a string
            "serving_size": int(serving_size),  # Ensure it's an integer
            "allergies": str(allergies)  # Ensure it's a string
        }

        # Store preferences in session state
        st.session_state.user_preferences = preferences

        return preferences
    except Exception as e:
        st.error(f"Error getting user preferences: {str(e)}")
        return None

async def generate_meal(meal_type, day, prompt, cuisine="All"):
    try:
        # Create a session for concurrent requests
        async with aiohttp.ClientSession() as session:
            # Prepare the request data with full system prompt
            data = {
                "model": "gpt-3.5-turbo-0125",
                "messages": [
                    {"role": "system", "content": """You are an expert Australian nutritionist and chef specializing in practical, flavorful home cooking. Follow dietary requirements, health conditions, and cultural preferences while maintaining authenticity and practicality. Prioritize generating distinct recipes. Avoid repeating the same or very similar recipes unless absolutely unavoidable. Ensure recipes differ significantly in ingredients, preparation, and flavor profiles. You create meals that:
                     
                    **IMPORTANT - RECIPE NAMES:**
                     
                    Generate a list of creative and original recipe names based on the given dish description or ingredients. *Recipe name must be over 5 words*. DO NOT use Recipe Names that starts with Aussie Brekkie. Avoid generic or overused words like: *Fragrant*, *Oceanic*, *Zesty*, *Stir-Fry*, *Delight*, *Aussie*,  *Brekkie*, *Lemony*, *Outback*
                     
                    - The names should feel fun, fresh, and inviting — but avoid being overly playful, exaggerated, or cliché. Aim for subtle creativity that sounds natural and appetizing. Keep titles clear, concise (5-8 words), and reflective of the key ingredients or style of the dish.  

                    **Guidelines:**
                    - Use clear, descriptive language.  
                    - Avoid generic or overused words like: *Fragrant*, *Oceanic*, *Zesty*, *Stir-Fry*, *Delight*, *Aussie*, *Brekkie*, *Lemony* 
                    - Subtle wordplay, alliteration, or sensory imagery is encouraged — only where it feels organic.  
                    - Focus on the key ingredient(s), cooking method, or regional influence.  
                    - The name should feel modern, refined, and not overly "foodie" or forced.
                     
                    **IMPORTANT - CUISINE REQUIREMENTS:**
                    - When a specific cuisine is selected, ALL meals MUST strictly follow that cuisine
                    - Use authentic ingredients, cooking methods, and flavor combinations
                    - Breakfast, lunch, and dinner must all reflect the chosen cuisine
                    - Only use ingredients and techniques traditional to that cuisine
                    - Adapt traditional dishes to meet dietary restrictions while maintaining authenticity
                    - Never mix cuisines unless "All" is selected
                    - Research and include authentic dishes for each meal type
                    - Use traditional cooking methods and equipment
                    - Include authentic garnishes and presentation styles
                    - Maintain cultural authenticity while meeting dietary needs
                    
                    **IMPORTANT - MEAL PLAN LENGTH:**
                    - Generate a complete day of meals with all required meal types (breakfast, lunch, dinner)
                    - Maintain consistency with previous days
                    - Ensure variety across the entire plan
                    - Each day MUST include all requested meal types
                    - Keep track of ingredient usage across the entire plan
                    
                    ** IMPORTANT RULES: Australian Dietary Guidelines Compliance**   
                    "Create a meal that strictly follows the **Australian Dietary Guidelines**. Ensure it includes:  
                    - A **protein source** (meat, fish, chicken, eggs, legumes, beans, etc.).  
                    - A **carbohydrate source**, preferably **whole grains** (wholegrain bread, rice, noodles, pasta, oats, quinoa, etc.).  
                    - A **healthy fat source** (dairy, olive oil, nuts, seeds, etc.).  
                    - At least **two different vegetables** for a balanced meal."  

                    ** IMPORTANT RULES: Ingredient Diversity**  
                    "Design a weekly meal plan that ensures **diversity in ingredients**. Avoid using the same proteins, carbohydrates, and vegetables repeatedly unless necessary to reduce food waste. Each meal should incorporate a variety of nutrient-dense ingredients."  

                    ** IMPORTANT RULES: Cooking Methods & Texture**  
                    "Generate a meal with **varied and interesting cooking methods** to enhance flavor and texture. Avoid plain techniques like steaming or baking without enhancements. Instead, use methods such as:  
                    - Sautéing  
                    - Air-frying  
                    - Roasting  
                    - Grilling  
                    - Charring  
                    Incorporate a mix of textures (e.g., **crispy, crunchy, creamy, or tender**) to create a satisfying dish."  

                    ** IMPORTANT RULES: Herbs & Spices Usage**  
                    "Ensure every meal includes **at least 2-3 herbs and spices**, excluding salt and pepper. Use both fresh and dried herbs where appropriate to enhance flavor. **Do not list salt or pepper as ingredients**—instead, mention 'season to taste' in the instructions."  

                    ** IMPORTANT RULES: Complete & Well-Rounded Meals**  
                    "Meals should be **nutritionally complete and well-balanced**, so be sure to include suitable sides with each main dish. Examples:  
                    - A stir-fry must include **rice or noodles** rather than just vegetables and protein.  
                    - A grilled protein should have complementary sides to enhance flavor and texture, such as **crispy sweet potato wedges or sautéed mixed greens**."  

                    ** IMPORTANT RULES: Measurement Units & Packaging Relevance**  
                    "Use **Australian supermarket measurement units** for all ingredients. Ensure:  
                    - **Liquids** are measured in teaspoons, tablespoons, or millilitres (ml).  
                    - **Solids** are measured in grams (g) or whole units (e.g., ½ avocado, 1 zucchini, ½ capsicum).  
                    - **Garlic** is measured in cloves, and **tomatoes** in halves or quarters.  
                    Reference **Coles or Woolworths packaging sizes** where possible to ensure accurate portioning."  

                    ** IMPORTANT RULES: Recipe Instructions Formatting**  
                    "Write clear, structured recipe instructions in **UK English** using the **metric system**. Ensure:  
                    - Steps flow logically and include **practical cooking tips**.  
                    - Instructions are easy to follow, catering to a **basic skill level**.  
                    - The format remains **concise yet detailed**, making recipes accessible for all users."
                    
                    **REMINDER**:  
                    - **Follow all the rules strictly. Do not ignore any points from the instructions above.**
                    - **Every recipe must include all necessary instructions** and adhere to the specific guidelines listed."""},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 4096,
                "temperature": 0.7,
                "presence_penalty": 0.1,
                "frequency_penalty": 0.1
            }

            # Make the API request
            headers = {
                "Authorization": f"Bearer {openai.api_key}",
                "Content-Type": "application/json"
            }
            
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                json=data,
                headers=headers
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    return (meal_type, day, result['choices'][0]['message']['content'])
                else:
                    error_text = await response.text()
                    raise Exception(f"API request failed with status {response.status}: {error_text}")

    except Exception as e:
        st.error(f"Error generating {meal_type}: {str(e)}")
        return None

def clean_recipe_text(text):
    """Clean recipe text for comparison."""
    # Remove measurements and quantities
    text = re.sub(r'\d+\s*(?:tbsp|tsp|cup|cups|g|kg|ml|l|oz|lb|inch|cm|mm|°C|°F|min|hour|hours|minute|minutes|second|seconds)', '', text)
    # Remove common words and ingredients
    common_words = ['ingredients', 'instructions', 'method', 'steps', 'serves', 'total time', 'prep time', 'cook time', 'time', 'serving', 'servings']
    for word in common_words:
        text = text.replace(word, '')
    # Remove extra spaces and convert to lowercase
    text = ' '.join(text.split()).lower()
    return text

def calculate_similarity(recipe1, recipe2):
    """Calculate similarity between two recipes using multiple criteria."""
    # Text similarity for recipe names
    name_similarity = SequenceMatcher(None, recipe1['name'].lower(), recipe2['name'].lower()).ratio()
    
    # Extract ingredients and convert to sets
    ingredients1 = set(recipe1['ingredients'].lower().split('\n'))
    ingredients2 = set(recipe2['ingredients'].lower().split('\n'))
    
    # Calculate ingredient similarity
    if ingredients1 and ingredients2:
        ingredient_similarity = len(ingredients1.intersection(ingredients2)) / max(len(ingredients1), len(ingredients2))
    else:
        ingredient_similarity = 0.0
    
    # Extract cooking methods
    methods1 = set([word.lower() for word in recipe1['instructions'].split() if word in ['bake', 'fry', 'grill', 'roast', 'steam', 'boil', 'stir-fry']])
    methods2 = set([word.lower() for word in recipe2['instructions'].split() if word in ['bake', 'fry', 'grill', 'roast', 'steam', 'boil', 'stir-fry']])
    
    # Calculate cooking method similarity
    if methods1 and methods2:
        method_similarity = len(methods1.intersection(methods2)) / max(len(methods1), len(methods2))
    else:
        method_similarity = 0.0
    
    # Calculate weighted average of similarities
    weights = {
        'name': 0.4,
        'ingredients': 0.3,
        'methods': 0.3
    }
    
    total_similarity = (
        name_similarity * weights['name'] +
        ingredient_similarity * weights['ingredients'] +
        method_similarity * weights['methods']
    )
    
    return total_similarity

def is_recipe_unique(new_recipe, existing_recipes, threshold=0.3):
    """Check if a recipe is unique compared to existing recipes."""
    for existing_recipe in existing_recipes:
        similarity = calculate_similarity(new_recipe, existing_recipe)
        if similarity > threshold:
            return False
    return True

async def generate_meal_plan(user_prefs):
    try:
        # Initialize tracking for unique recipes and cuisine distribution
        st.session_state.generated_recipes = []
        st.session_state.meal_types_used = set()
        st.session_state.cuisines_used = set()
        st.session_state.cuisine_distribution = {}  # Initialize cuisine distribution
        
        if not isinstance(user_prefs, dict):
            raise ValueError("user_prefs must be a dictionary")

        # Access values from dictionary with error handling
        required_keys = ['num_days', 'diet', 'allergies', 'health_conditions', 
                        'meal_type', 'cuisine', 'budget', 'time_constraint', 'serving_size']
        
        for key in required_keys:
            if key not in user_prefs:
                raise KeyError(f"Missing required preference: {key}")

        # Cache frequently used values
        num_days = user_prefs['num_days']
        diet_type = user_prefs['diet']
        allergies = user_prefs['allergies']
        health_conditions = user_prefs['health_conditions']
        meal_type = user_prefs['meal_type']
        cuisine = user_prefs['cuisine']
        budget = user_prefs['budget']
        cooking_time = user_prefs['time_constraint']
        servings = user_prefs['serving_size']
        
        # Create a formatted preferences dictionary for get_meal_prompt
        formatted_prefs = {
            'num_days': num_days,
            'diet': diet_type,
            'allergies': allergies,
            'health_conditions': health_conditions,
            'meal_type': meal_type,
            'cuisine': cuisine,
            'budget': budget,
            'time_constraint': cooking_time,
            'serving_size': servings
        }

        # Pre-compute common requirements
        health_requirements = IMPORTANT_RULES if health_conditions != "None" else ""
        
        # Get specific dietary requirements based on diet type
        diet_rules = ""
        if diet_type != "None":
            # Handle multiple diet types if selected
            if isinstance(diet_type, list):
                for diet in diet_type:
                    if diet in DIETARY_REQUIREMENTS:
                        diet_info = DIETARY_REQUIREMENTS[diet]
                        diet_rules += f"\n{diet} Requirements:\n"
                        diet_rules += f"- Allowed: {', '.join(diet_info['allowed'])}\n"
                        diet_rules += f"- Restricted: {', '.join(diet_info['restricted'])}\n"
                        diet_rules += f"- Notes: {diet_info['notes']}\n"
            else:
                if diet_type in DIETARY_REQUIREMENTS:
                    diet_info = DIETARY_REQUIREMENTS[diet_type]
                    diet_rules = f"\n{diet_type} Requirements:\n"
                    diet_rules += f"- Allowed: {', '.join(diet_info['allowed'])}\n"
                    diet_rules += f"- Restricted: {', '.join(diet_info['restricted'])}\n"
                    diet_rules += f"- Notes: {diet_info['notes']}\n"
        
        dietary_requirements = f"""
        {diet_rules}
        
        Additional Requirements:
        - Allergies/Intolerances: {allergies}
        - Health Conditions: {health_conditions}
        - Budget: {budget}
        - Time Constraint: {cooking_time}
        - Serving Size: {servings} people
        
        IMPORTANT: The recipe MUST strictly follow all dietary requirements listed above.
        If there are conflicts between different diet types, prioritize the most restrictive requirements.
        """

        # Pre-compute budget requirements
        budget_requirements = {
            "Tight budget": """
            Use these budget-friendly ingredients:
            - Proteins: eggs, lentils, chickpeas, beans, canned tuna
            - Vegetables: potatoes, onions, carrots, cabbage, frozen vegetables
            - Grains: rice, pasta, oats
            - Avoid: expensive cuts of meat and exotic ingredients
            """,
            "Moderate budget": """
            Use these moderately priced ingredients:
            - Proteins: chicken thighs, ground beef, tofu, eggs
            - Vegetables: seasonal vegetables, frozen vegetables
            - Grains: rice, pasta, bread
            - Include some fresh herbs and spices
            """,
            "Generous budget": """
            Use these premium ingredients:
            - Proteins: fish, lean meats, specialty proteins
            - Vegetables: fresh seasonal vegetables, specialty produce
            - Grains: quinoa, specialty grains
            - Include premium ingredients and fresh herbs
            """
        }.get(budget, "")

        # Pre-compute measurement requirements
        measurement_requirements = """
        Use these standard measurements:
        - 1 cup = 250ml
        - 1 tablespoon = 15ml
        - 1 teaspoon = 5ml
        - Use metric measurements for liquids
        - Use standard household measurements for solids
        """

        # Pre-compute available ingredients based on budget
        available_ingredients = []
        for category, items in CATEGORIES.items():
            if any(budget.lower() in category.lower() for budget in ["Budget", "Affordable"]):
                available_ingredients.extend(items)

        # Pre-compute cuisine preferences
        cuisine_prefs = eval(user_prefs['cuisine'])
        if not cuisine_prefs or "All" in cuisine_prefs:
            available_cuisines = [
                "Mediterranean", "Mexican", "Indian", "Japanese",
                "Chinese", "Middle Eastern", "Vietnamese",
                "Korean", "American", "British", "Australian", "African"
            ]
            available_cuisines = [c for c in available_cuisines if c != "Thai"]
            random.shuffle(available_cuisines)
        else:
            available_cuisines = cuisine_prefs.copy()
            random.shuffle(available_cuisines)
        
        # Create tasks for all meals
        tasks = []
        used_cuisines = set()
        cuisine_index = 0
        
        for day in range(1, num_days + 1):
            st.session_state.cuisine_distribution[day] = {
                'breakfast': None,
                'lunch': None,
                'dinner': None
            }
            
            meal_types = []
            if "All" in user_prefs['meal_type']:
                meal_types = ["Breakfast", "Lunch", "Dinner"]
            else:
                meal_types = [meal for meal in ["Breakfast", "Lunch", "Dinner"] 
                            if meal in user_prefs['meal_type']]
            
            if not meal_types:
                meal_types = ["Breakfast", "Lunch", "Dinner"]
            
            for meal in meal_types:
                selected_cuisine = available_cuisines[cuisine_index % len(available_cuisines)]
                cuisine_index += 1
                
                st.session_state.cuisine_distribution[day][meal.lower()] = selected_cuisine
                used_cuisines.add(selected_cuisine)
                
                # Get authentic recipe names for the selected cuisine
                authentic_recipes = AUTHENTIC_RECIPE_NAMES.get(selected_cuisine, [])
                recipe_inspiration = "\n".join([f"- {recipe}" for recipe in authentic_recipes])

                # Add cuisine-specific ingredients
                cuisine_ingredients = [item for item in available_ingredients 
                                    if selected_cuisine.lower() in item.lower()]
                current_ingredients = available_ingredients + cuisine_ingredients

                # Create a more specific prompt that emphasizes using authentic recipe names
                prompt = get_meal_prompt(
                    meal_type=meal,
                    day=day,
                    user_prefs=formatted_prefs,
                    health_requirements=health_requirements,
                    cuisine_requirements=f"""
                    {selected_cuisine} Cuisine Requirements:
                    - Use authentic {selected_cuisine} ingredients and methods
                    - Follow {selected_cuisine} cultural traditions
                    - Use traditional {selected_cuisine} dishes
                    - Include {selected_cuisine} specific ingredients
                    - Avoid mixing with other cuisines
                    - Use authentic {selected_cuisine} cooking techniques
                    - Follow {selected_cuisine} plating styles
                    - Use proper {selected_cuisine} terminology
                    - Ensure dish is recognizably {selected_cuisine}
                    - The recipe MUST explicitly mention "{selected_cuisine}" in its description or title
                    
                    Authentic {selected_cuisine} Recipe Examples:
                    {recipe_inspiration}
                    
                    IMPORTANT: When generating the recipe:
                    1. Choose one of the authentic recipe names above as inspiration
                    2. Adapt it to meet dietary requirements while maintaining authenticity
                    3. Use traditional ingredients and methods from the chosen recipe
                    4. Keep the core concept and flavors of the original dish
                    5. Make necessary adjustments for health conditions and allergies
                    6. Ensure the recipe name reflects the authentic dish while being unique
                    
                    The generated recipe should:
                    - Be inspired by one of the authentic recipes listed above
                    - Maintain cultural authenticity
                    - Use traditional ingredients and methods
                    - Have a distinct {selected_cuisine} flavor profile
                    - Be appropriate for {meal}
                    """ + dietary_requirements + budget_requirements + measurement_requirements,
                    available_ingredients=current_ingredients,
                    authentic_recipes=authentic_recipes
                )
                tasks.append(generate_meal(meal, day, prompt, selected_cuisine))

        # Process all tasks concurrently with maximum parallelization
        semaphore = asyncio.Semaphore(10)  # Increased to allow more concurrent requests
        
        async def generate_with_semaphore(task):
            async with semaphore:
                try:
                    return await task
                except Exception as e:
                    if "rate limit" in str(e).lower():
                        await asyncio.sleep(1)  # Reduced from 5 to 2 seconds
                        return await task
                    st.error(f"Error in meal generation: {str(e)}")
                    return None

        # Process all tasks in parallel
        results = await asyncio.gather(*[generate_with_semaphore(task) for task in tasks])
        results = [r for r in results if r and isinstance(r, tuple) and len(r) == 3]

        if not results:
            raise ValueError("No valid meals were generated")

        # Verify all selected cuisines are represented if specific cuisines were selected
        if cuisine_prefs:
            generated_cuisines = set()
            for result in results:
                meal_type, day, recipe = result
                assigned_cuisine = st.session_state.cuisine_distribution[day][meal_type.lower()]
                if assigned_cuisine:
                    generated_cuisines.add(assigned_cuisine)

            if len(generated_cuisines) < len(cuisine_prefs):
                missing_cuisines = set(cuisine_prefs) - generated_cuisines
                raise ValueError(f"Not all selected cuisines were represented. Missing: {', '.join(missing_cuisines)}")

        # Process and sort results
        processed_results = []
        for result in results:
            meal_type, day, recipe = result
            processed_results.append({
                "day": day,
                "meal_type": meal_type,
                "recipe": recipe
            })

        # Sort results by day and meal type
        meal_type_order = {"Breakfast": 0, "Lunch": 1, "Dinner": 2}
        processed_results.sort(key=lambda x: (x['day'], meal_type_order[x['meal_type']]))

        # Check for recipe uniqueness in batches
        unique_recipes = []
        for meal in processed_results:
            recipe = meal['recipe']
            if is_recipe_unique(recipe, st.session_state.generated_recipes):
                unique_recipes.append(recipe)
            else:
                st.warning(f"Regenerating {meal['meal_type']} for Day {meal['day']} to ensure uniqueness...")
                # Add specific requirements for uniqueness
                prompt = get_meal_prompt(
                    meal_type=meal['meal_type'],
                    day=meal['day'],
                    user_prefs=formatted_prefs,
                    health_requirements=health_requirements,
                    cuisine_requirements="" + dietary_requirements + budget_requirements + measurement_requirements,
                    available_ingredients=available_ingredients
                )
                new_recipe = await generate_meal(meal['meal_type'], meal['day'], prompt, cuisine)
                if new_recipe:
                    unique_recipes.append(new_recipe)
                else:
                    raise ValueError(f"Failed to generate unique {meal['meal_type']} for Day {meal['day']}")

        # Update session state with unique recipes
        st.session_state.generated_recipes.extend(unique_recipes)

        return processed_results

    except Exception as e:
        st.error(f"Error generating meal plan: {str(e)}")
        return []

def display_meal_plan(meal_plan):
    st.title("Your Personalized Meal Plan")
    
    # Format meal plan for display and download
    formatted_meal_plan = ""
    for meal in meal_plan:
        # Format the recipe content
        recipe_content = meal['recipe']
        
        # Split the recipe into sections
        sections = recipe_content.split("\n")
        formatted_sections = []
        
        for section in sections:
            if section.strip().lower().startswith("ingredients:"):
                # Format ingredients section
                ingredients_text = section.replace("Ingredients:", "").strip()
                # Split by bullet points and clean up
                ingredients = [ing.strip() for ing in ingredients_text.split("•") if ing.strip()]
                formatted_ingredients = "Ingredients:\n"
                for ingredient in ingredients:
                    formatted_ingredients += f"• {ingredient}\n"
                formatted_sections.append(formatted_ingredients)
            elif section.strip().lower().startswith("instructions:"):
                # Add extra newline before instructions
                formatted_sections.append("\nInstructions:")
            else:
                formatted_sections.append(section)
        
        # Join the sections back together with proper spacing
        formatted_recipe = "\n".join(formatted_sections)
        
        # Add to the meal plan
        formatted_meal_plan += "\n"
        formatted_meal_plan += formatted_recipe
        formatted_meal_plan += "\n"
    
    # Add download button with formatted text
    st.download_button(
        label="Download Meal Plan",
        data=formatted_meal_plan,
        file_name=f"meal_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        mime="text/plain"
    )

    # Display the formatted meal plan
    st.markdown(formatted_meal_plan)
    
    # TEMPORARILY COMMENTED OUT: Generation time display
    # if hasattr(st.session_state, 'generation_time'):
    #     st.markdown(f"<p style='color: #666666; text-align: right; font-size: 0.9em;'>Total Generation Time: {st.session_state.generation_time:.2f} seconds</p>", unsafe_allow_html=True)

def extract_ingredients(recipe_text):
    """Extract main ingredients from recipe text."""
    ingredients = set()
    
    # Look for ingredients section
    if "Ingredients:" in recipe_text:
        ingredients_section = recipe_text.split("Ingredients:")[1].split("Instructions:")[0]
        
        # Split into lines and process each line
        for line in ingredients_section.split('\n'):
            line = line.strip()
            if line and not line.startswith('•') and not line.startswith('-'):
                # Remove quantities and units
                ingredient = line.split('(')[0].strip()
                ingredient = ingredient.split(',')[0].strip()
                ingredient = ingredient.split('or')[0].strip()
                if ingredient:
                    ingredients.add(ingredient.lower())
    
    return ingredients

def extract_cooking_methods(recipe_text):
    """Extract cooking methods from recipe text."""
    cooking_methods = set()
    
    # Common cooking methods to look for
    methods = {
        'bake', 'boil', 'broil', 'grill', 'fry', 'sauté', 'sauté', 'roast', 
        'steam', 'stir-fry', 'simmer', 'poach', 'braise', 'blanch', 'deep-fry',
        'pan-fry', 'sear', 'toast', 'warm', 'heat', 'cook', 'prepare'
    }
    
    # Look for cooking methods in instructions
    if "Instructions:" in recipe_text:
        instructions = recipe_text.split("Instructions:")[1]
        
        # Check each line for cooking methods
        for line in instructions.split('\n'):
            line = line.lower()
            for method in methods:
                if method in line:
                    cooking_methods.add(method)
    
    return cooking_methods

def extract_sauces(recipe_text):
    """Extract sauces and seasonings from recipe text."""
    sauces = set()
    
    # Common sauces and seasonings to look for
    sauce_types = {
        'soy sauce', 'fish sauce', 'oyster sauce', 'hoisin sauce', 'teriyaki sauce',
        'worcestershire sauce', 'barbecue sauce', 'hot sauce', 'chili sauce',
        'tahini', 'harissa', 'sambal oelek', 'gochujang', 'miso', 'pesto',
        'vinaigrette', 'dressing', 'marinade', 'sauce', 'glaze', 'dip'
    }
    
    # Look for sauces in ingredients and instructions
    if "Ingredients:" in recipe_text:
        ingredients_section = recipe_text.split("Ingredients:")[1].split("Instructions:")[0]
        
        # Check ingredients section
        for line in ingredients_section.split('\n'):
            line = line.lower()
            for sauce in sauce_types:
                if sauce in line:
                    sauces.add(sauce)
    
    if "Instructions:" in recipe_text:
        instructions = recipe_text.split("Instructions:")[1]
        
        # Check instructions section
        for line in instructions.split('\n'):
            line = line.lower()
            for sauce in sauce_types:
                if sauce in line:
                    sauces.add(sauce)
    
    return sauces

def extract_proteins(recipe_text):
    # Extract protein sources from recipe text
    proteins = set()
    protein_keywords = [
        'chicken', 'beef', 'pork', 'lamb', 'fish', 'salmon', 'tuna', 'shrimp',
        'eggs', 'tofu', 'tempeh', 'chickpeas', 'lentils', 'beans', 'quinoa',
        'yogurt', 'cheese', 'milk', 'protein powder'
    ]
    
    # Convert recipe text to lowercase for case-insensitive matching
    recipe_lower = recipe_text.lower()
    
    # Look for protein keywords in the recipe text
    for keyword in protein_keywords:
        if keyword in recipe_lower:
            proteins.add(keyword)
    
    return proteins

def extract_vegetables(recipe_text):
    # Extract vegetables from recipe text
    vegetables = set()
    vegetable_keywords = [
        'spinach', 'kale', 'lettuce', 'broccoli', 'cauliflower', 'carrots',
        'zucchini', 'squash', 'peppers', 'onions', 'garlic', 'tomatoes',
        'cucumber', 'celery', 'mushrooms', 'asparagus', 'green beans',
        'sweet potato', 'potato', 'pumpkin'
    ]
    
    # Convert recipe text to lowercase for case-insensitive matching
    recipe_lower = recipe_text.lower()
    
    # Look for vegetable keywords in the recipe text
    for keyword in vegetable_keywords:
        if keyword in recipe_lower:
            vegetables.add(keyword)
    
    return vegetables

def extract_grains(recipe_text):
    # Extract grains from recipe text
    grains = set()
    grain_keywords = [
        'rice', 'quinoa', 'oats', 'barley', 'couscous', 'pasta', 'bread',
        'wheat', 'buckwheat', 'millet', 'amaranth', 'teff', 'sorghum'
    ]
    
    # Convert recipe text to lowercase for case-insensitive matching
    recipe_lower = recipe_text.lower()
    
    # Look for grain keywords in the recipe text
    for keyword in grain_keywords:
        if keyword in recipe_lower:
            grains.add(keyword)
    
    return grains

def main():
    try:
        # Get user preferences
        user_prefs = get_user_preferences()
        
        if user_prefs is None:
            st.error("Failed to get user preferences. Please try again.")
            return
        
        # Inject custom CSS to center the spinner and text
        st.markdown(
            """
            <style>
            div.stSpinner > div {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            /* TEMPORARILY COMMENTED OUT: Generation time CSS
            .generation-time {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background-color: rgba(0, 0, 0, 0.7);
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 14px;
                z-index: 1000;
            }
            */
            </style>
            """,
            unsafe_allow_html=True,
        )
        
        # Generate meal plan button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Generate Meal Plan"):
                # Use the standard spinner
                with st.spinner("Generating Your Personalized Meal Plan..."):
                    try:
                        # Start timing
                        start_time = time.time()
                        
                        # Use asyncio to run the async function
                        meal_plan = asyncio.run(generate_meal_plan(user_prefs))
                        
                        # TEMPORARILY COMMENTED OUT: Generation time calculation
                        # generation_time = time.time() - start_time
                        # st.session_state.generation_time = generation_time
                        
                        if meal_plan:  # Only show success if we actually got a meal plan
                            st.session_state.meal_plan = meal_plan

                            # Using markdown to mimic st.success() with centered alignment
                            st.markdown(
                                "<div style='text-align: center; background-color: #d4edda; padding: 10px; border-radius: 5px; color: #155724; font-weight: bold;'>"
                                "Meal Plan Generated Successfully!"
                                "</div>",
                                unsafe_allow_html=True
                            )
                            
                            # TEMPORARILY COMMENTED OUT: Generation time display
                            # st.markdown(
                            #     f"<div class='generation-time'>Generation Time: {generation_time:.2f} seconds</div>",
                            #     unsafe_allow_html=True
                            # )
                        else:
                            st.error("Failed to Generate Meal Plan. Please Try Again")
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
                        st.session_state.meal_plan = None
        
        # Display meal plan if available
        if st.session_state.meal_plan:
            display_meal_plan(st.session_state.meal_plan)
            
            # TEMPORARILY COMMENTED OUT: Generation time display at bottom
            # if hasattr(st.session_state, 'generation_time'):
            #     st.markdown(
            #         f"<div class='generation-time'>Generation Time: {st.session_state.generation_time:.2f} seconds</div>",
            #         unsafe_allow_html=True
            #     )
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()