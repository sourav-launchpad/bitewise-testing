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
    IMPORTANT_RULES
)

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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
            
            # Simplified diet options showing only diet names, with None at the bottom
            diet = st.selectbox(
                "**Diet Type**",
                options=[
                    "Vegetarian",
                    "Vegan",
                    "Pescatarian",
                    "Mediterranean",
                    "Paleo",
                    "Keto",
                    "Low-Carb",
                    "Whole Food Plant-Based",
                    "High-Protein",
                    "Diabetic-Friendly",
                    "None"
                ],
                index=10  # Default to "None"
            )
            
            # Changed from multiselect to selectbox
            allergies = st.selectbox(
                "**Allergies/Intolerances**",
                options=["Dairy", "Gluten", "Nuts", "Eggs", "Soy", "Seafood", "Sesame", "Mustard", "Chicken", "Pork", "Beef", "None"],
                index=11  # Default to "None"
            )

        with col2:
            # Changed from multiselect to selectbox
            health_conditions = st.selectbox(
                "**Health Conditions**",
                options=["Diabetes", "Hypertension", "Celiac Disease", "Lactose Intolerance", "IBS", 
                        "Acid Reflux/GERD", "Kidney Disease", "High Cholesterol", "Gout", "None"],
                index=9  # Default to "None"
            )
            
            # Dropdown for meal type where users can select but not type
            meal_type = st.selectbox(
                "**Meal Type Preference**",
                options=["Breakfast", "Lunch", "Dinner", "All"],
                index=3  # Default to "All"
            )
            
            cuisine = st.selectbox(
                "**Preferred Cuisine**",
                options=["Australian", "Italian", "Japanese", "Mexican", "Indian", "Chinese", 
                        "Thai", "Mediterranean", "Middle Eastern", "French", "Korean", 
                        "Vietnamese", "Greek", "Spanish", "All"],
                index=14  # Default to "All"
            )

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
            "allergies": str(allergies),  # Ensure it's a string
            "health_conditions": str(health_conditions),  # Ensure it's a string
            "meal_type": str(meal_type).lower(),  # Ensure it's lowercase string
            "cuisine": str(cuisine),  # Ensure it's a string
            "budget": str(budget),  # Ensure it's a string
            "time_constraint": str(time_constraint),  # Ensure it's a string
            "serving_size": int(serving_size)  # Ensure it's an integer
        }

        # Store preferences in session state
        st.session_state.user_preferences = preferences

        return preferences
    except Exception as e:
        st.error(f"Error getting user preferences: {str(e)}")
        return None

async def generate_meal(meal_type, day, prompt):
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {openai.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are an expert chef creating personalized meal plans. Follow dietary requirements, health conditions, and cultural preferences while maintaining authenticity and practicality."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 2000,  # Keep original token size
                "temperature": 0.7
            }
            
            async with session.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data
            ) as response:
                if response.status == 429:  # Rate limit
                    raise openai.RateLimitError("Rate limit exceeded")
                result = await response.json()
                return (meal_type, day, result['choices'][0]['message']['content'])
    except Exception as e:
        st.error(f"Error generating {meal_type}: {str(e)}")
        return None

async def generate_meal_plan(user_prefs):
    try:
        if not isinstance(user_prefs, dict):
            raise ValueError("user_prefs must be a dictionary")

        # Access values from dictionary with error handling
        required_keys = ['num_days', 'diet', 'allergies', 'health_conditions', 
                        'meal_type', 'cuisine', 'budget', 'time_constraint', 'serving_size']
        
        for key in required_keys:
            if key not in user_prefs:
                raise KeyError(f"Missing required preference: {key}")

        num_days = user_prefs['num_days']
        diet_type = user_prefs['diet']
        allergies = user_prefs['allergies']
        health_conditions = user_prefs['health_conditions']
        meal_type = user_prefs['meal_type']
        cuisine = user_prefs['cuisine']
        budget = user_prefs['budget']
        cooking_time = user_prefs['time_constraint']
        servings = user_prefs['serving_size']

        # Set health and cuisine requirements based on user preferences
        health_requirements = ""
        if health_conditions != "None":
            health_requirements = IMPORTANT_RULES

        # Add dietary requirements based on allergies and diet type
        dietary_requirements = f"""
        Please ensure the recipe meets the following dietary requirements:
        - Diet Type: {diet_type}
        - Allergies/Intolerances: {allergies}
        - Health Conditions: {health_conditions}
        - Budget: {budget}
        - Time Constraint: {cooking_time}
        - Serving Size: {servings} people
        """

        # Set cuisine requirements based on user preferences
        cuisine_requirements = ""
        if user_prefs['cuisine'] == 'Indian':
            cuisine_requirements = """
            Essential Indian Ingredients:
            - Breakfast staples: moong dal, besan, semolina, poha
            - Spices & aromatics: turmeric, cumin, coriander, ginger, garlic
            - Fresh ingredients: curry leaves, coriander, mint
            - Pantry essentials: ghee, coconut oil, lentils, rice
            """
        else:
            cuisine_requirements = f"""
            Follow these requirements for {user_prefs['cuisine']} cuisine:
            - Use authentic ingredients and cooking methods
            - Maintain cultural authenticity
            - Include traditional dishes
            - Follow regional variations
            - Ensure proper meal structure
            """

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

        # Initialize tracking sets for each meal type
        used_recipes = {
            'breakfast': set(),
            'lunch': set(),
            'dinner': set()
        }
        used_ingredients = {
            'breakfast': set(),
            'lunch': set(),
            'dinner': set()
        }
        used_cooking_methods = {
            'breakfast': set(),
            'lunch': set(),
            'dinner': set()
        }
        used_sauces = {
            'breakfast': set(),
            'lunch': set(),
            'dinner': set()
        }
        used_proteins = {
            'breakfast': set(),
            'lunch': set(),
            'dinner': set()
        }
        used_vegetables = {
            'breakfast': set(),
            'lunch': set(),
            'dinner': set()
        }
        used_grains = {
            'breakfast': set(),
            'lunch': set(),
            'dinner': set()
        }

        def is_recipe_unique(meal_type, recipe, ingredients, cooking_methods, sauces, proteins, vegetables, grains):
            # Check recipe name
            recipe_key = f"{meal_type}_{recipe[:100]}"
            if recipe_key in used_recipes[meal_type]:
                return False
            
            # Check ingredients
            for ingredient in ingredients:
                if ingredient in used_ingredients[meal_type]:
                    return False
            
            # Check cooking methods
            for method in cooking_methods:
                if method in used_cooking_methods[meal_type]:
                    return False
            
            # Check sauces
            for sauce in sauces:
                if sauce in used_sauces[meal_type]:
                    return False
            
            # Check proteins
            for protein in proteins:
                if protein in used_proteins[meal_type]:
                    return False
            
            # Check vegetables
            for veg in vegetables:
                if veg in used_vegetables[meal_type]:
                    return False
            
            # Check grains
            for grain in grains:
                if grain in used_grains[meal_type]:
                    return False
            
            return True

        def update_used_items(meal_type, recipe, ingredients, cooking_methods, sauces, proteins, vegetables, grains):
            recipe_key = f"{meal_type}_{recipe[:100]}"
            used_recipes[meal_type].add(recipe_key)
            used_ingredients[meal_type].update(ingredients)
            used_cooking_methods[meal_type].update(cooking_methods)
            used_sauces[meal_type].update(sauces)
            used_proteins[meal_type].update(proteins)
            used_vegetables[meal_type].update(vegetables)
            used_grains[meal_type].update(grains)

        meal_plan = []
        
        # Create tasks for all meals
        tasks = []
        for day in range(1, num_days + 1):
            # Generate breakfast if requested
            if meal_type in ["breakfast", "all"]:
                breakfast_prompt = get_meal_prompt(
                    meal_type="breakfast",
                    day=day,
                    user_prefs=formatted_prefs,
                    health_requirements=health_requirements,
                    cuisine_requirements=cuisine_requirements + dietary_requirements + "\nPlease create a unique breakfast recipe that hasn't been used before. Do not include any additional notes or suggestions."
                )
                tasks.append(generate_meal("breakfast", day, breakfast_prompt))

            # Generate lunch if requested
            if meal_type in ["lunch", "all"]:
                lunch_prompt = get_meal_prompt(
                    meal_type="lunch",
                    day=day,
                    user_prefs=formatted_prefs,
                    health_requirements=health_requirements,
                    cuisine_requirements=cuisine_requirements + dietary_requirements + "\nPlease create a unique lunch recipe that hasn't been used before. Do not include any additional notes or suggestions."
                )
                tasks.append(generate_meal("lunch", day, lunch_prompt))

            # Generate dinner if requested
            if meal_type in ["dinner", "all"]:
                dinner_prompt = get_meal_prompt(
                    meal_type="dinner",
                    day=day,
                    user_prefs=formatted_prefs,
                    health_requirements=health_requirements,
                    cuisine_requirements=cuisine_requirements + dietary_requirements + "\nPlease create a unique dinner recipe that hasn't been used before. Do not include any additional notes or suggestions."
                )
                tasks.append(generate_meal("dinner", day, dinner_prompt))

        # Execute all tasks concurrently with a semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(5)  # Limit to 5 concurrent requests
        async def generate_with_semaphore(task):
            async with semaphore:
                return await task

        results = await asyncio.gather(*[generate_with_semaphore(task) for task in tasks])
        
        # Process results and update tracking sets
        for result in results:
            if result:
                meal_type, day, recipe = result
                
                # Extract components
                ingredients = extract_ingredients(recipe)
                cooking_methods = extract_cooking_methods(recipe)
                sauces = extract_sauces(recipe)
                proteins = extract_proteins(recipe)
                vegetables = extract_vegetables(recipe)
                grains = extract_grains(recipe)
                
                # Update tracking sets
                update_used_items(meal_type, recipe, ingredients, cooking_methods, sauces, proteins, vegetables, grains)
                
                # Add to meal plan
                meal_plan.append({
                    "day": day,
                    "meal": meal_type.capitalize(),
                    "recipe": recipe
                })

        return meal_plan

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
    
    # Display generation time in a subtle style at the bottom right
    if hasattr(st.session_state, 'generation_time'):
        st.markdown(f"<p style='color: #666666; text-align: right; font-size: 0.9em;'>Total Generation Time: {st.session_state.generation_time:.2f} seconds</p>", unsafe_allow_html=True)

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
        
        # Create a centered container for the button
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        
        # Generate meal plan button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Generate Meal Plan"):
                with st.spinner("Generating your personalized meal plan..."):
                    try:
                        # Use asyncio to run the async function
                        meal_plan = asyncio.run(generate_meal_plan(user_prefs))
                        if meal_plan:  # Only show success if we actually got a meal plan
                            st.session_state.meal_plan = meal_plan
                            st.success("Meal plan generated successfully!")
                        else:
                            st.error("Failed to generate meal plan. Please try again.")
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
                        st.session_state.meal_plan = None
        
        # Close the button container
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display meal plan if available
        if st.session_state.meal_plan:
            display_meal_plan(st.session_state.meal_plan)
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()