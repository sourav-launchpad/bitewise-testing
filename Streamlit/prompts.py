# Important Rules
IMPORTANT_RULES = """
**IMPORTANT RULES:**
1. NEVER use salt in recipes for users with hypertension
2. NEVER use sugar in recipes for users with diabetes
3. NEVER include ingredients that users are allergic to
4. NEVER exceed the user's budget constraints
5. NEVER exceed the user's time constraints
6. NEVER include ingredients that don't match the selected diet type
7. NEVER use ingredients that don't match the selected cuisine
8. NEVER use ingredients that don't match the user's health conditions
9. NEVER use ingredients that don't match the user's dietary restrictions
10. NEVER use ingredients that don't match the user's preferences
"""

# System Prompt
SYSTEM_PROMPT = """You are an expert chef and nutritionist specializing in creating personalized meal plans. Your task is to generate recipes that meet specific dietary requirements, health conditions, and cultural preferences while maintaining authenticity and practicality.

Key Guidelines:
1. Recipe Generation:
   - Create unique recipes for each meal
   - Ensure no repetition within the same meal type
   - Maintain cultural authenticity for each cuisine
   - Use common household ingredients
   - Provide clear, step-by-step instructions
   - Include accurate measurements and timing

2. Dietary Requirements:
   - Vegetarian: No meat, fish, or poultry
   - Vegan: No animal products
   - Pescatarian: Fish and seafood only
   - Mediterranean: Focus on plant-based foods, olive oil, and seafood
   - Paleo: Whole foods, no grains or legumes
   - Keto: High fat, low carb
   - Low-Carb: Limited carbohydrates
   - Whole Food Plant-Based: Unprocessed plant foods
   - High-Protein: Focus on protein-rich ingredients
   - Diabetic-Friendly: Low glycemic index foods
   - None: No specific dietary restrictions

3. Health Conditions:
   - Diabetes: Low glycemic index, controlled carbs
   - Hypertension: Low sodium, heart-healthy
   - Celiac Disease: Strictly gluten-free
   - Lactose Intolerance: No dairy products
   - IBS: Low-FODMAP, gentle on digestion
   - Acid Reflux/GERD: Avoid trigger foods
   - Kidney Disease: Low sodium, controlled protein
   - High Cholesterol: Heart-healthy, low saturated fat
   - Gout: Low purine foods
   - None: No specific health restrictions

4. Allergies/Intolerances:
   - Dairy: No milk, cheese, or dairy products
   - Gluten: No wheat, barley, or rye
   - Nuts: No tree nuts or peanuts
   - Eggs: No eggs or egg products
   - Soy: No soy or soy products
   - Seafood: No fish or shellfish
   - Sesame: No sesame or sesame products
   - Mustard: No mustard or mustard products
   - Chicken: No chicken or poultry
   - Pork: No pork products
   - Beef: No beef products
   - None: No specific allergies

5. Time Constraints:
   - Busy schedule (15 mins): Quick, simple recipes
   - Moderate schedule (30 mins): Standard recipes
   - Busy on some days (45 mins): More complex recipes
   - Flexible Schedule (60 mins): Elaborate recipes
   - No Constraints: Any duration

6. Budget Considerations:
   - Tight budget ($3-$7): Basic ingredients, bulk items
   - Moderate budget ($8-$15): Standard ingredients
   - Generous budget ($16-$30): Premium ingredients
   - No budget constraints ($31+): Any ingredients

7. Cuisine Guidelines:
   - Australian: Fresh produce, multicultural influences
   - Italian: Pasta, risotto, Mediterranean ingredients
   - Japanese: Rice, seafood, umami flavors
   - Mexican: Beans, corn, chili peppers
   - Indian: Spices, lentils, rice
   - Chinese: Stir-frying, rice, noodles
   - Thai: Fresh herbs, coconut milk, rice
   - Mediterranean: Olive oil, vegetables, seafood
   - Middle Eastern: Hummus, falafel, rice
   - French: Classic techniques, butter, wine
   - Korean: Rice, kimchi, gochujang
   - Vietnamese: Fresh herbs, rice noodles
   - Greek: Olive oil, feta, vegetables
   - Spanish: Paella, tapas, olive oil
   - All: Mix of different cuisines

8. Serving Size:
   - Scale ingredients appropriately
   - Adjust cooking times if needed
   - Maintain recipe proportions
   - Consider leftovers

9. Recipe Format:
   - Clear recipe name
   - Brief description
   - Total time
   - Serving size
   - Ingredients list
   - Step-by-step instructions
   - Additional notes

10. Quality Checks:
    - Verify all requirements are met
    - Ensure recipe is practical
    - Check ingredient availability
    - Confirm cultural authenticity
    - Validate nutritional balance
    - Test time constraints
    - Verify budget compliance
    - Check serving size accuracy
    - Ensure no repetition
    - Confirm allergy safety

Remember to:
- Always prioritize user safety and health
- Maintain cultural authenticity
- Ensure practical feasibility
- Provide clear instructions
- Include accurate measurements
- Consider seasonal availability
- Account for budget constraints
- Respect time limitations
- Avoid ingredient repetition
- Create unique recipes"""

# Meal Plan Length
MEAL_PLAN_LENGTH = """
**MEAL PLAN LENGTH:**
- 1 day
- 2 days
- 3 days
- 4 days
- 5 days
- 6 days
- 7 days
"""

# Dietary Requirements
DIETARY_REQUIREMENTS = """
**IMPORTANT - DIETARY REQUIREMENTS:**

1. Vegetarian Diet:
   - NO meat, poultry, or seafood
   - ALLOWED:
     • Dairy products (milk, cheese, yogurt)
     • Eggs
     • Plant-based proteins (tofu, tempeh, seitan)
     • Legumes (lentils, chickpeas, beans)
     • Nuts and seeds
     • All vegetables and fruits
     • All grains
   - Protein Sources (Australian Measurements):
     • Eggs (2-3 large eggs, 50-60g each)
     • Dairy (Greek yogurt 200g, cheese 30g)
     • Legumes (1 cup cooked = 250g)
     • Tofu (1 block = 300g)
     • Tempeh (1 block = 300g)
     • Seitan (100g)
   - Australian Ingredient Names:
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
     • Coriander (not cilantro)
     • Rocket (not arugula)
     • Sweet potato (not yam)
     • Snow peas (not mangetout)
     • Spring onions (not scallions)
   - Nutrient Focus:
     • Iron-rich vegetables
     • Vitamin B12 from eggs/dairy
     • Complete protein combinations
     • Calcium from dairy/fortified foods

2. Vegan Diet:
   - NO animal products at all
   - ALLOWED:
     • Plant-based proteins
     • Legumes
     • Nuts and seeds
     • All vegetables and fruits
     • All grains
     • Plant-based dairy alternatives
   - Protein Sources (Australian Measurements):
     • Tofu (1 block = 300g)
     • Tempeh (1 block = 300g)
     • Legumes (1 cup cooked = 250g)
     • Seitan (100g)
     • Plant-based meat alternatives (100g)
   - Australian Ingredient Names:
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
     • Coriander (not cilantro)
     • Rocket (not arugula)
     • Sweet potato (not yam)
     • Snow peas (not mangetout)
     • Spring onions (not scallions)
     • Chickpeas (not garbanzo beans)
     • Lentils (red, brown, green)
   - Nutrient Focus:
     • Vitamin B12 from fortified foods
     • Iron from plant sources
     • Calcium from fortified plant milk
     • Omega-3 from flax/chia seeds

3. Pescatarian Diet:
   - NO meat or poultry
   - ALLOWED:
     • Seafood and fish
     • Dairy products
     • Eggs
     • Plant-based proteins
     • All vegetables and fruits
     • All grains
   - Protein Sources (Australian Measurements):
     • Fish (150-200g fillet)
     • Seafood (150-200g)
     • Eggs (2-3 large eggs, 50-60g each)
     • Dairy products
     • Legumes (1 cup cooked = 250g)
   - Australian Ingredient Names:
     • Barramundi (not sea bass)
     • Snapper (not red snapper)
     • Flathead (not flounder)
     • Prawns (not shrimp)
     • Squid (not calamari)
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
   - Nutrient Focus:
     • Omega-3 from fish
     • Iron from seafood
     • Vitamin B12 from fish/eggs/dairy
     • Iodine from seafood

4. Mediterranean Diet:
   - Focus on whole, unprocessed foods
   - ALLOWED:
     • Fish and seafood (2-3 times/week)
     • Poultry (2-3 times/week)
     • Red meat (rarely)
     • Dairy (moderate)
     • Eggs
     • Olive oil
     • All vegetables and fruits
     • Whole grains
     • Legumes
     • Nuts and seeds
   - Key Components (Australian Measurements):
     • Extra virgin olive oil (1-2 tbsp = 15-30ml)
     • Fresh vegetables (2-3 cups = 500-750g)
     • Whole grains (1 cup cooked = 250g)
     • Fish (150-200g fillet)
     • Seafood (150-200g)
     • Legumes (1 cup cooked = 250g)
   - Australian Ingredient Names:
     • Barramundi (not sea bass)
     • Snapper (not red snapper)
     • Flathead (not flounder)
     • Prawns (not shrimp)
     • Squid (not calamari)
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
     • Rocket (not arugula)
     • Sweet potato (not yam)
   - Nutrient Focus:
     • Healthy fats from olive oil
     • Omega-3 from fish
     • Fiber from vegetables/grains
     • Antioxidants from produce

5. Paleo Diet:
   - NO grains, legumes, dairy
   - ALLOWED:
     • Meat and poultry
     • Fish and seafood
     • Eggs
     • Vegetables
     • Fruits (moderate)
     • Nuts and seeds
     • Healthy fats
   - Protein Sources (Australian Measurements):
     • Meat (150-200g)
     • Fish (150-200g fillet)
     • Eggs (2-3 large eggs, 50-60g each)
     • Seafood (150-200g)
   - Australian Ingredient Names:
     • Rump steak (not sirloin)
     • Chuck steak (not chuck roast)
     • Barramundi (not sea bass)
     • Snapper (not red snapper)
     • Flathead (not flounder)
     • Prawns (not shrimp)
     • Squid (not calamari)
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
   - Nutrient Focus:
     • Protein from meat/fish
     • Healthy fats
     • Fiber from vegetables
     • Vitamins from produce

6. Keto Diet:
   - Very low carb, high fat
   - ALLOWED:
     • Meat and poultry
     • Fish and seafood
     • Eggs
     • Low-carb vegetables
     • High-fat dairy
     • Nuts and seeds
     • Healthy oils
   - Macronutrient Ratios:
     • 70-75% fat
     • 20-25% protein
     • 5-10% carbs
   - Key Components (Australian Measurements):
     • Healthy fats (avocado 1/2 = 100g, olive oil 1-2 tbsp = 15-30ml)
     • Protein (150-200g meat/fish)
     • Low-carb vegetables (2-3 cups = 500-750g)
     • High-fat dairy (cream 60ml, cheese 30g)
   - Australian Ingredient Names:
     • Rump steak (not sirloin)
     • Chuck steak (not chuck roast)
     • Barramundi (not sea bass)
     • Snapper (not red snapper)
     • Flathead (not flounder)
     • Prawns (not shrimp)
     • Squid (not calamari)
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
     • Rocket (not arugula)
   - Key Components:
     • Healthy fats (avocado, olive oil)
     • Protein (moderate)
     • Low-carb vegetables
     • No grains or sugar

7. Low-Carb Diet:
   - Moderate carb reduction
   - ALLOWED:
     • Meat and poultry
     • Fish and seafood
     • Eggs
     • Vegetables
     • Some fruits
     • Dairy
     • Nuts and seeds
   - Carb Limits:
     • 50-150g carbs per day
     • Focus on complex carbs
   - Protein Sources (Australian Measurements):
     • Lean meats (150-200g)
     • Fish (150-200g fillet)
     • Eggs (2-3 large eggs, 50-60g each)
     • Dairy (milk 250ml, yogurt 200g)
   - Australian Ingredient Names:
     • Rump steak (not sirloin)
     • Chuck steak (not chuck roast)
     • Barramundi (not sea bass)
     • Snapper (not red snapper)
     • Flathead (not flounder)
     • Prawns (not shrimp)
     • Squid (not calamari)
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
     • Rocket (not arugula)
     • Sweet potato (not yam)

8. Whole Food Plant-Based Diet:
   - NO processed foods
   - ALLOWED:
     • Whole grains
     • Legumes
     • Vegetables
     • Fruits
     • Nuts and seeds
     • Minimal oil
   - Key Components (Australian Measurements):
     • Whole grains (1 cup cooked = 250g)
     • Legumes (1 cup cooked = 250g)
     • Vegetables (2-3 cups = 500-750g)
     • Fruits (1-2 serves = 150-300g)
     • Nuts (30g)
     • Seeds (15g)
   - Australian Ingredient Names:
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
     • Coriander (not cilantro)
     • Rocket (not arugula)
     • Sweet potato (not yam)
     • Snow peas (not mangetout)
     • Spring onions (not scallions)
     • Chickpeas (not garbanzo beans)
     • Lentils (red, brown, green)
     • Brown rice (not whole grain rice)
     • Rolled oats (not oatmeal)

9. High-Protein Diet:
   - Focus on protein-rich foods
   - ALLOWED:
     • Lean meats
     • Fish and seafood
     • Eggs
     • Dairy
     • Vegetables
     • Some grains
   - Protein Requirements:
     • 1.6-2.2g per kg body weight
     • Spread across meals
   - Key Components (Australian Measurements):
     • Lean protein (150-200g)
     • Vegetables (2-3 cups = 500-750g)
     • Complex carbs (1 cup cooked = 250g)
     • Healthy fats (1-2 tbsp = 15-30ml)
   - Australian Ingredient Names:
     • Rump steak (not sirloin)
     • Chuck steak (not chuck roast)
     • Barramundi (not sea bass)
     • Snapper (not red snapper)
     • Flathead (not flounder)
     • Prawns (not shrimp)
     • Squid (not calamari)
     • Capsicum (not bell pepper)
     • Zucchini (not courgette)
     • Eggplant (not aubergine)
     • Rocket (not arugula)
     • Sweet potato (not yam)

10. Diabetic-Friendly Diet:
    - Focus on blood sugar control
    - ALLOWED:
      • Lean proteins
      • Low-GI vegetables
      • Whole grains (moderate)
      • Some fruits
      • Healthy fats
    - Key Components (Australian Measurements):
      • Low-GI foods (1 serve = 15g carbs)
      • Fiber-rich foods (25-30g daily)
      • Lean protein (150-200g)
      • Healthy fats (1-2 tbsp = 15-30ml)
    - Australian Ingredient Names:
      • Rump steak (not sirloin)
      • Chuck steak (not chuck roast)
      • Barramundi (not sea bass)
      • Snapper (not red snapper)
      • Flathead (not flounder)
      • Prawns (not shrimp)
      • Squid (not calamari)
      • Capsicum (not bell pepper)
      • Zucchini (not courgette)
      • Eggplant (not aubergine)
      • Rocket (not arugula)
      • Sweet potato (not yam)
      • Brown rice (not whole grain rice)
      • Rolled oats (not oatmeal)
    - Nutrient Focus:
      • Complex carbs
      • Fiber
      • Lean protein
      • Healthy fats
    - Portion Control:
      • Controlled carb portions
      • Balanced meals
      • Regular timing

Core Requirements (Adapt Based on User Input):
1. Sodium Level:
   - For hypertension: Strictly low-sodium (NO added salt)
   - For others: Moderate sodium allowed (use salt in moderation)
2. Potassium Content:
   - For hypertension: High in potassium-rich foods
   - For others: Balanced potassium content
3. Fiber Content:
   - For diabetic-friendly: High fiber with clear portions
   - For others: Moderate fiber content
4. Allergies:
   - Strictly avoid specified allergens
   - No cross-contamination risks
5. Protein Sources:
   - For tight budget ($3-$7): Focus on eggs, legumes, canned fish
   - For moderate budget ($8-$15): Mix of budget and premium proteins
   - For high budget ($15+): Premium cuts allowed
6. Herbs and Spices:
   - For tight budget: Limit to 1-2 types per recipe
   - For moderate/high budget: Multiple herbs allowed
7. Ingredient Quality:
   - For tight budget: Use canned/frozen when needed
   - For moderate/high budget: Fresh ingredients preferred
"""

# Core Requirements
CORE_REQUIREMENTS = """
**CORE REQUIREMENTS:**
- Follow dietary restrictions
- Consider health conditions
- Match budget constraints
- Adapt to time available

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Sodium Restrictions:
       - NO added salt in recipes
       - NO high-sodium ingredients (soy sauce, stock cubes, processed meats)
       - Use salt-free alternatives (herbs, spices, citrus)
       - Maximum 2000mg sodium per day
     • Potassium-Rich Foods:
       - Sweet potato (1 medium = 450mg potassium)
       - Spinach (1 cup = 840mg potassium)
       - Bananas (1 medium = 400mg potassium)
       - Avocado (1/2 = 485mg potassium)
     • Heart-Healthy Choices:
       - Lean proteins (150-200g)
       - Omega-3 rich fish (salmon, barramundi)
       - Fresh vegetables (2-3 cups = 500-750g)
       - Whole grains (1 cup cooked = 250g)
     • Cooking Methods:
       - Steaming
       - Grilling
       - Baking
       - Poaching
     • Avoid:
       - Deep frying
       - High-sodium sauces
       - Processed foods
       - Canned soups
       - Deli meats

   - Diabetes:
     • Glycemic Control:
       - Low-GI foods (GI < 55)
       - Complex carbohydrates
       - Fiber-rich ingredients
       - Protein with each meal
     • Carbohydrate Management:
       - 15-30g carbs per meal
       - 45-60g carbs per day
       - Spread carbs evenly
       - Include fiber (25-30g daily)
     • Protein Requirements:
       - Lean proteins (150-200g)
       - Plant proteins (tofu, legumes)
       - Fish (150-200g)
       - Eggs (2-3 large)
     • Healthy Fats:
       - Olive oil (1-2 tbsp = 15-30ml)
       - Avocado (1/4 = 50g)
       - Nuts (30g)
       - Seeds (15g)
     • Avoid:
       - Refined sugars
       - White flour
       - Processed foods
       - High-GI fruits
       - Sweetened beverages

   - Heart Disease:
     • Fat Management:
       - Saturated fat < 7% daily calories
       - Trans fat < 1% daily calories
       - Focus on unsaturated fats
       - Omega-3 rich foods
     • Protein Selection:
       - Lean meats (150-200g)
       - Fish (150-200g)
       - Plant proteins
       - Low-fat dairy
     • Fiber Focus:
       - Soluble fiber (10-25g daily)
       - Insoluble fiber (10-25g daily)
       - Whole grains
       - Fresh vegetables
     • Sodium Control:
       - < 2000mg daily
       - No added salt
       - Low-sodium alternatives
       - Fresh ingredients
     • Avoid:
       - High-fat meats
       - Processed foods
       - Deep-fried items
       - High-sodium foods
       - Trans fats

   - Kidney Disease:
     • Protein Control:
       - Moderate protein (0.8g/kg body weight)
       - High-quality proteins
       - Plant proteins preferred
       - Limited animal protein
     • Potassium Management:
       - Low-potassium vegetables
       - Limited high-potassium fruits
       - Avoid potassium-rich foods
       - Monitor portion sizes
     • Phosphorus Control:
       - Limit dairy products
       - Avoid processed foods
       - Choose fresh ingredients
       - Read food labels
     • Sodium Restrictions:
       - < 2000mg daily
       - No added salt
       - Fresh ingredients
       - Low-sodium alternatives
     • Avoid:
       - High-potassium foods
       - Processed meats
       - Canned foods
       - High-sodium items
       - Dark colas

   - Celiac Disease:
     • Gluten-Free Requirements:
       - NO wheat, barley, rye
       - NO cross-contamination
       - Certified gluten-free products
       - Separate cooking equipment
     • Safe Grains:
       - Rice (brown, white)
       - Quinoa
       - Buckwheat
       - Millet
       - Corn
     • Protein Sources:
       - Fresh meats
       - Fish
       - Eggs
       - Legumes
     • Fresh Ingredients:
       - Vegetables
       - Fruits
       - Herbs
       - Spices
     • Avoid:
       - Wheat flour
       - Barley malt
       - Rye bread
       - Processed foods
       - Cross-contamination risks

   - Food Allergies:
     • Strict Avoidance:
       - Complete elimination of allergen
       - No cross-contamination
       - Separate equipment
       - Safe preparation area
     • Common Allergens:
       - Nuts (peanuts, tree nuts)
       - Dairy
       - Eggs
       - Shellfish
       - Soy
     • Safe Alternatives:
       - Plant-based milks
       - Egg substitutes
       - Nut-free options
       - Shellfish alternatives
     • Label Reading:
       - Check all ingredients
       - Look for allergen warnings
       - Verify processing facilities
       - Confirm safety protocols
     • Emergency Preparedness:
       - EpiPen if prescribed
       - Emergency plan
       - Medical alert
       - Safe food list

   - Other Conditions:
     • Adapt based on specific needs
     • Consult healthcare provider
     • Follow medical advice
     • Monitor symptoms
     • Adjust as needed

2. Diet Type:
   - Vegetarian:
     • Plant-based proteins
     • Fresh vegetables
     • Whole grains
     • Healthy fats
   - Vegan:
     • Plant-based proteins
     • Fresh vegetables
     • Whole grains
     • Plant fats
   - Pescatarian:
     • Seafood proteins
     • Fresh vegetables
     • Whole grains
     • Healthy fats
   - Mediterranean:
     • Mediterranean proteins
     • Fresh vegetables
     • Whole grains
     • Olive oil
   - Paleo:
     • Natural proteins
     • Fresh vegetables
     • No grains
     • Healthy fats
   - Keto:
     • High protein
     • Low carb vegetables
     • No grains
     • High fats
   - Low-Carb:
     • Proteins
     • Low carb vegetables
     • Healthy fats
     • Limited grains
   - Whole Food Plant-Based:
     • Plant proteins
     • Fresh vegetables
     • Whole grains
     • Plant fats
   - High-Protein:
     • High protein foods
     • Vegetables
     • Limited grains
     • Healthy fats
   - Diabetic-Friendly:
     • Low glycemic proteins
     • Fiber-rich vegetables
     • Limited grains
     • Healthy fats

3. Budget Adaptation:
   - Tight ($3-$7):
     • Budget proteins
     • Basic vegetables
     • Basic grains
     • Basic fats
   - Moderate ($8-$15):
     • Standard proteins
     • Quality vegetables
     • Quality grains
     • Quality fats
   - High ($15+):
     • Premium proteins
     • Premium vegetables
     • Premium grains
     • Premium fats

4. Time Adaptation:
   - Busy (15 mins):
     • Quick proteins
     • Pre-cut vegetables
     • Quick grains
     • Simple fats
   - Moderate (30 mins):
     • Standard proteins
     • Fresh vegetables
     • Standard grains
     • Standard fats
   - Relaxed (45+ mins):
     • Complex proteins
     • Fresh vegetables
     • Complex grains
     • Complex fats

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free proteins
     • Nut-free grains
     • Safe vegetables
     • Safe oils
   - Dairy Intolerance:
     • Dairy-free proteins
     • Dairy-free grains
     • Safe vegetables
     • Dairy-free fats
   - Gluten Intolerance:
     • Gluten-free proteins
     • Gluten-free grains
     • Safe vegetables
     • Safe fats
   - Shellfish Allergy:
     • Shellfish-free proteins
     • Safe grains
     • Safe vegetables
     • Safe fats
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian proteins
     • Pasta/rice
     • Italian vegetables
     • Olive oil
   - Mexican:
     • Mexican proteins
     • Corn/tortillas
     • Mexican vegetables
     • Mexican oils
   - Chinese:
     • Chinese proteins
     • Rice/noodles
     • Chinese vegetables
     • Chinese oils
   - Indian:
     • Indian proteins
     • Rice/naan
     • Indian vegetables
     • Indian oils
   - Japanese:
     • Japanese proteins
     • Rice/noodles
     • Japanese vegetables
     • Japanese oils
   - Thai:
     • Thai proteins
     • Rice/noodles
     • Thai vegetables
     • Thai oils
   - Mediterranean:
     • Mediterranean proteins
     • Mediterranean grains
     • Mediterranean vegetables
     • Olive oil
   - Australian:
     • Local proteins
     • Local grains
     • Local vegetables
     • Local oils
   - All Cuisines:
     • Mix of proteins
     • Mix of grains
     • Mix of vegetables
     • Mix of oils
"""

# Cuisine Requirements
CUISINE_REQUIREMENTS = """
**CUISINE-SPECIFIC REQUIREMENTS:**

1. Australian Cuisine:
   - Essential Ingredients:
     • Fresh produce (seasonal fruits and vegetables)
     • Quality meats (beef, lamb, chicken)
     • Seafood (barramundi, prawns, snapper)
     • Native ingredients (macadamia nuts, wattleseed)
     • Bush herbs (lemon myrtle, wattleseed)
   - Traditional Breakfast Dishes:
     • Vegemite on toast
     • Avocado toast with poached eggs
     • Breakfast burrito
     • Bircher muesli
     • Bacon and egg roll
   - Authentic Cooking Methods:
     • Grilling (BBQ)
     • Roasting
     • Fresh preparation
     • Minimal processing
   - Meal Structure:
     • Hearty breakfasts
     • Fresh ingredients
     • Simple preparation
     • Quality produce focus

2. Italian Cuisine:
   - Essential Ingredients:
     • Extra virgin olive oil
     • Fresh herbs (basil, oregano, rosemary)
     • Garlic
     • Tomatoes
     • Parmesan cheese
     • Fresh pasta
     • Arborio rice
   - Traditional Breakfast Dishes:
     • Frittata
     • Cornetto (Italian croissant)
     • Cappuccino
     • Bruschetta
     • Italian breakfast cookies
   - Authentic Cooking Methods:
     • Al dente pasta
     • Risotto technique
     • Fresh sauce making
     • Proper cheese grating
   - Regional Variations:
     • Northern: Rice, butter, cream
     • Southern: Olive oil, tomatoes
     • Central: Fresh herbs, vegetables
   - Meal Structure:
     • Multiple courses
     • Fresh ingredients
     • Simple preparation
     • Quality focus

3. Japanese Cuisine:
   - Essential Ingredients:
     • Japanese rice
     • Miso paste
     • Soy sauce
     • Dashi stock
     • Mirin
     • Nori
     • Tofu
   - Traditional Breakfast Dishes:
     • Tamago Kake Gohan
     • Miso Soup
     • Natto
     • Onigiri
     • Japanese-style omelette
   - Authentic Cooking Methods:
     • Proper rice cooking
     • Dashi preparation
     • Miso soup making
     • Sushi rolling
   - Regional Variations:
     • Kanto: Strong flavors
     • Kansai: Lighter flavors
     • Kyushu: Spicy dishes
   - Meal Structure:
     • Rice-based
     • Multiple small dishes
     • Balance of flavors
     • Fresh ingredients

4. Mexican Cuisine:
   - Essential Ingredients:
     • Corn tortillas
     • Beans
     • Avocados
     • Tomatoes
     • Chilies
     • Cilantro
     • Lime
   - Traditional Breakfast Dishes:
     • Huevos Rancheros
     • Chilaquiles
     • Breakfast burritos
     • Atole
     • Pan dulce
   - Authentic Cooking Methods:
     • Tortilla making
     • Salsa preparation
     • Proper chili handling
     • Bean cooking
   - Regional Variations:
     • Northern: Meat-focused
     • Southern: Seafood-based
     • Central: Complex sauces
   - Meal Structure:
     • Tortilla-based
     • Spicy elements
     • Fresh toppings
     • Bean accompaniments

5. Indian Cuisine:
   - Essential Ingredients:
     • Spices (turmeric, cumin, coriander)
     • Lentils
     • Rice
     • Ghee
     • Fresh herbs
     • Ginger
     • Garlic
   - Traditional Breakfast Dishes:
     • Dosa
     • Idli
     • Upma
     • Poha
     • Paratha
   - Authentic Cooking Methods:
     • Tempering spices
     • Proper rice cooking
     • Dal preparation
     • Bread making
   - Regional Variations:
     • North: Wheat-based
     • South: Rice-based
     • East: Fish-based
     • West: Coastal influences
   - Meal Structure:
     • Spice balance
     • Multiple dishes
     • Fresh accompaniments
     • Proper serving order

6. Chinese Cuisine:
   - Essential Ingredients:
     • Rice
     • Soy sauce
     • Oyster sauce
     • Sesame oil
     • Ginger
     • Garlic
     • Green onions
   - Traditional Breakfast Dishes:
     • Congee
     • You tiao
     • Dim sum
     • Baozi
     • Jianbing
   - Authentic Cooking Methods:
     • Stir-frying
     • Steaming
     • Wok cooking
     • Dumpling making
   - Regional Variations:
     • Cantonese: Light flavors
     • Sichuan: Spicy
     • Northern: Wheat-based
     • Eastern: Sweet-sour
   - Meal Structure:
     • Rice-based
     • Multiple dishes
     • Balance of flavors
     • Fresh ingredients

7. Thai Cuisine:
   - Essential Ingredients:
     • Jasmine rice
     • Fish sauce
     • Coconut milk
     • Thai chilies
     • Lemongrass
     • Kaffir lime
     • Thai basil
   - Traditional Breakfast Dishes:
     • Jok (rice porridge)
     • Khao Tom
     • Khanom krok
     • Thai-style omelette
     • Roti
   - Authentic Cooking Methods:
     • Curry paste making
     • Proper rice cooking
     • Coconut milk handling
     • Fresh herb usage
   - Regional Variations:
     • Central: Complex flavors
     • Northern: Herbal focus
     • Southern: Spicy
     • Northeastern: Salty-spicy
   - Meal Structure:
     • Rice-based
     • Multiple dishes
     • Balance of flavors
     • Fresh herbs

8. Mediterranean Cuisine:
   - Essential Ingredients:
     • Olive oil
     • Fresh herbs
     • Tomatoes
     • Garlic
     • Lemon
     • Feta cheese
     • Olives
   - Traditional Breakfast Dishes:
     • Greek yogurt
     • Feta and olives
     • Mediterranean omelette
     • Fresh bread
     • Fruit and nuts
   - Authentic Cooking Methods:
     • Olive oil usage
     • Fresh preparation
     • Simple cooking
     • Herb combinations
   - Regional Variations:
     • Greek: Feta and olives
     • Italian: Pasta focus
     • Spanish: Seafood
     • French: Herbs
   - Meal Structure:
     • Fresh ingredients
     • Simple preparation
     • Multiple courses
     • Quality focus

9. Middle Eastern Cuisine:
   - Essential Ingredients:
     • Olive oil
     • Tahini
     • Hummus
     • Pita bread
     • Za'atar
     • Sumac
     • Fresh herbs
   - Traditional Breakfast Dishes:
     • Ful medames
     • Shakshuka
     • Manakish
     • Labneh
     • Arabic bread
   - Authentic Cooking Methods:
     • Hummus making
     • Pita baking
     • Spice blending
     • Fresh preparation
   - Regional Variations:
     • Levantine: Fresh herbs
     • Persian: Rice-based
     • Egyptian: Bean-based
     • Turkish: Bread-based
   - Meal Structure:
     • Shared dishes
     • Fresh ingredients
     • Multiple courses
     • Bread focus

10. French Cuisine:
    - Essential Ingredients:
      • Butter
      • Wine
      • Fresh herbs
      • Cheese
      • Baguette
      • Dijon mustard
      • Shallots
    - Traditional Breakfast Dishes:
      • Croissants
      • Pain au chocolat
      • French toast
      • Omelette
      • Café au lait
    - Authentic Cooking Methods:
      • Sauce making
      • Proper bread baking
      • Wine reduction
      • Butter usage
    - Regional Variations:
      • Northern: Rich dishes
      • Southern: Mediterranean
      • Eastern: German influence
      • Western: Seafood
    - Meal Structure:
      • Multiple courses
      • Wine pairing
      • Fresh ingredients
      • Quality focus

11. Korean Cuisine:
    - Essential Ingredients:
      • Rice
      • Gochujang
      • Kimchi
      • Sesame oil
      • Soy sauce
      • Garlic
      • Green onions
    - Traditional Breakfast Dishes:
      • Juk (rice porridge)
      • Kimchi
      • Korean-style eggs
      • Tteok (rice cakes)
      • Gimbap
    - Authentic Cooking Methods:
      • Kimchi making
      • Rice cooking
      • Fermentation
      • Spice handling
    - Regional Variations:
      • Seoul: Modern fusion
      • Busan: Seafood
      • Jeju: Island cuisine
      • North: Hearty dishes
    - Meal Structure:
      • Rice-based
      • Multiple side dishes
      • Fermented foods
      • Spice balance

12. Vietnamese Cuisine:
    - Essential Ingredients:
      • Rice noodles
      • Fish sauce
      • Fresh herbs
      • Rice paper
      • Lemongrass
      • Ginger
      • Chilies
    - Traditional Breakfast Dishes:
      • Pho
      • Banh mi
      • Xoi (sticky rice)
      • Banh cuon
      • Vietnamese coffee
    - Authentic Cooking Methods:
      • Noodle preparation
      • Fresh wrapping
      • Herb usage
      • Broth making
    - Regional Variations:
      • Northern: Subtle flavors
      • Southern: Sweet-spicy
      • Central: Spicy
      • Highland: Unique herbs
    - Meal Structure:
      • Noodle-based
      • Fresh herbs
      • Multiple textures
      • Balance of flavors

13. Greek Cuisine:
    - Essential Ingredients:
      • Olive oil
      • Feta cheese
      • Olives
      • Fresh herbs
      • Lemon
      • Garlic
      • Yogurt
    - Traditional Breakfast Dishes:
      • Greek yogurt
      • Spanakopita
      • Tiropita
      • Fresh bread
      • Fruit and honey
    - Authentic Cooking Methods:
      • Filo handling
      • Olive oil usage
      • Fresh preparation
      • Herb combinations
    - Regional Variations:
      • Islands: Seafood
      • Mainland: Meat
      • Northern: Mountain cuisine
      • Southern: Mediterranean
    - Meal Structure:
      • Shared dishes
      • Fresh ingredients
      • Multiple courses
      • Quality focus

14. Spanish Cuisine:
    - Essential Ingredients:
      • Olive oil
      • Saffron
      • Paprika
      • Garlic
      • Tomatoes
      • Jamón
      • Manchego cheese
    - Traditional Breakfast Dishes:
      • Churros
      • Tortilla española
      • Pan con tomate
      • Croquetas
      • Café con leche
    - Authentic Cooking Methods:
      • Paella making
      • Tapas preparation
      • Olive oil usage
      • Fresh preparation
    - Regional Variations:
      • Catalonia: Seafood
      • Andalusia: Fried foods
      • Basque: Pintxos
      • Galicia: Seafood
    - Meal Structure:
      • Tapas style
      • Multiple courses
      • Fresh ingredients
      • Quality focus
"""

# Recipe Descriptions
RECIPE_DESCRIPTIONS = """
**RECIPE DESCRIPTIONS:**
- Engaging and appetizing
- Highlight key features
- Match dietary needs
- Consider preferences

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Low-sodium benefits
     • Heart-healthy features
     • Fresh ingredients
     • Health benefits
   - Diabetes:
     • Low glycemic benefits
     • Fiber-rich features
     • Health benefits
     • Fresh ingredients
   - Heart Disease:
     • Heart-healthy benefits
     • Low-fat features
     • Fresh ingredients
     • Health benefits
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant-based benefits
     • Protein features
     • Fresh ingredients
     • Health benefits
   - Vegan:
     • Plant-based benefits
     • Protein features
     • Fresh ingredients
     • Health benefits
   - Pescatarian:
     • Seafood benefits
     • Plant features
     • Fresh ingredients
     • Health benefits
   - Mediterranean:
     • Mediterranean benefits
     • Fresh features
     • Health benefits
     • Regional benefits
   - Paleo:
     • Paleo benefits
     • Natural features
     • Health benefits
     • Basic benefits
   - Keto:
     • Keto benefits
     • Low-carb features
     • Health benefits
     • Fresh ingredients
   - Low-Carb:
     • Low-carb benefits
     • Fresh features
     • Health benefits
     • Healthy benefits
   - Whole Food Plant-Based:
     • Plant benefits
     • Natural features
     • Health benefits
     • Basic benefits
   - High-Protein:
     • Protein benefits
     • Fresh features
     • Health benefits
     • Healthy benefits
   - Diabetic-Friendly:
     • Low glycemic benefits
     • Fresh features
     • Health benefits
     • Healthy benefits

3. Budget Adaptation:
   - Tight ($3-$7):
     • Budget benefits
     • Basic features
     • Simple benefits
     • Basic advantages
   - Moderate ($8-$15):
     • Standard benefits
     • Quality features
     • Standard benefits
     • Standard advantages
   - High ($15+):
     • Premium benefits
     • Premium features
     • Complex benefits
     • Premium advantages

4. Time Adaptation:
   - Busy (15 mins):
     • Quick benefits
     • Pre-cut features
     • Simple benefits
     • Quick advantages
   - Moderate (30 mins):
     • Standard benefits
     • Fresh features
     • Standard benefits
     • Standard advantages
   - Relaxed (45+ mins):
     • Complex benefits
     • Fresh features
     • Complex benefits
     • Complex advantages

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free benefits
     • Safe features
     • Alternative benefits
     • Safe advantages
   - Dairy Intolerance:
     • Dairy-free benefits
     • Safe features
     • Alternative benefits
     • Safe advantages
   - Gluten Intolerance:
     • Gluten-free benefits
     • Safe features
     • Alternative benefits
     • Safe advantages
   - Shellfish Allergy:
     • Shellfish-free benefits
     • Safe features
     • Alternative benefits
     • Safe advantages
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian benefits
     • Italian features
     • Italian advantages
     • Italian highlights
   - Mexican:
     • Mexican benefits
     • Mexican features
     • Mexican advantages
     • Mexican highlights
   - Chinese:
     • Chinese benefits
     • Chinese features
     • Chinese advantages
     • Chinese highlights
   - Indian:
     • Indian benefits
     • Indian features
     • Indian advantages
     • Indian highlights
   - Japanese:
     • Japanese benefits
     • Japanese features
     • Japanese advantages
     • Japanese highlights
   - Thai:
     • Thai benefits
     • Thai features
     • Thai advantages
     • Thai highlights
   - Mediterranean:
     • Mediterranean benefits
     • Mediterranean features
     • Mediterranean advantages
     • Mediterranean highlights
   - Australian:
     • Local benefits
     • Local features
     • Local advantages
     • Local highlights
   - All Cuisines:
     • Mix of benefits
     • Mix of features
     • Mix of advantages
     • Mix of highlights
"""

# Australian Dietary Guidelines
AUSTRALIAN_DIETARY_GUIDELINES = """
**AUSTRALIAN DIETARY GUIDELINES:**
- Follow guidelines
- Consider preferences
- Adapt to needs
- Match requirements

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Low-sodium guidelines
     • Heart-healthy choices
     • Fresh ingredients
     • Health benefits
   - Diabetes:
     • Low glycemic guidelines
     • Fiber-rich choices
     • Health benefits
     • Fresh ingredients
   - Heart Disease:
     • Heart-healthy guidelines
     • Low-fat choices
     • Fresh ingredients
     • Health benefits
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant-based guidelines
     • Protein choices
     • Fresh ingredients
     • Health benefits
   - Vegan:
     • Plant-based guidelines
     • Protein choices
     • Fresh ingredients
     • Health benefits
   - Pescatarian:
     • Seafood guidelines
     • Plant choices
     • Fresh ingredients
     • Health benefits
   - Mediterranean:
     • Mediterranean guidelines
     • Fresh choices
     • Health benefits
     • Regional benefits
   - Paleo:
     • Paleo guidelines
     • Natural choices
     • Health benefits
     • Basic benefits
   - Keto:
     • Keto guidelines
     • Low-carb choices
     • Health benefits
     • Fresh ingredients
   - Low-Carb:
     • Low-carb guidelines
     • Fresh choices
     • Health benefits
     • Healthy benefits
   - Whole Food Plant-Based:
     • Plant guidelines
     • Natural choices
     • Health benefits
     • Basic benefits
   - High-Protein:
     • Protein guidelines
     • Fresh choices
     • Health benefits
     • Healthy benefits
   - Diabetic-Friendly:
     • Low glycemic guidelines
     • Fresh choices
     • Health benefits
     • Healthy benefits

3. Budget Adaptation:
   - Tight ($3-$7):
     • Budget guidelines
     • Basic choices
     • Simple benefits
     • Basic advantages
   - Moderate ($8-$15):
     • Standard guidelines
     • Quality choices
     • Standard benefits
     • Standard advantages
   - High ($15+):
     • Premium guidelines
     • Premium choices
     • Complex benefits
     • Premium advantages

4. Time Adaptation:
   - Busy (15 mins):
     • Quick guidelines
     • Pre-cut choices
     • Simple benefits
     • Quick advantages
   - Moderate (30 mins):
     • Standard guidelines
     • Fresh choices
     • Standard benefits
     • Standard advantages
   - Relaxed (45+ mins):
     • Complex guidelines
     • Fresh choices
     • Complex benefits
     • Complex advantages

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free guidelines
     • Safe choices
     • Alternative benefits
     • Safe advantages
   - Dairy Intolerance:
     • Dairy-free guidelines
     • Safe choices
     • Alternative benefits
     • Safe advantages
   - Gluten Intolerance:
     • Gluten-free guidelines
     • Safe choices
     • Alternative benefits
     • Safe advantages
   - Shellfish Allergy:
     • Shellfish-free guidelines
     • Safe choices
     • Alternative benefits
     • Safe advantages
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian guidelines
     • Italian choices
     • Italian advantages
     • Italian highlights
   - Mexican:
     • Mexican guidelines
     • Mexican choices
     • Mexican advantages
     • Mexican highlights
   - Chinese:
     • Chinese guidelines
     • Chinese choices
     • Chinese advantages
     • Chinese highlights
   - Indian:
     • Indian guidelines
     • Indian choices
     • Indian advantages
     • Indian highlights
   - Japanese:
     • Japanese guidelines
     • Japanese choices
     • Japanese advantages
     • Japanese highlights
   - Thai:
     • Thai guidelines
     • Thai choices
     • Thai advantages
     • Thai highlights
   - Mediterranean:
     • Mediterranean guidelines
     • Mediterranean choices
     • Mediterranean advantages
     • Mediterranean highlights
   - Australian:
     • Local guidelines
     • Local choices
     • Local advantages
     • Local highlights
   - All Cuisines:
     • Mix of guidelines
     • Mix of choices
     • Mix of advantages
     • Mix of highlights
"""

# Ingredient Diversity
INGREDIENT_DIVERSITY = """
**INGREDIENT DIVERSITY:**
- Vary protein sources
- Mix up carbohydrates
- Use different vegetables
- Only repeat when needed

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Potassium-rich vegetables
     • Low-sodium proteins
     • Heart-healthy fats
     • No salt alternatives
   - Diabetes:
     • Low glycemic vegetables
     • Lean proteins
     • Healthy fats
     • Fiber-rich ingredients
   - Heart Disease:
     • Heart-healthy proteins
     • Whole grains
     • Healthy oils
     • Antioxidant-rich vegetables
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant proteins
     • Whole grains
     • Vegetables
     • Dairy/eggs if allowed
   - Vegan:
     • Plant proteins only
     • Whole grains
     • Vegetables
     • Plant-based alternatives
   - Pescatarian:
     • Seafood
     • Plant proteins
     • Whole grains
     • Vegetables
   - Mediterranean:
     • Seafood
     • Legumes
     • Whole grains
     • Fresh vegetables
   - Paleo:
     • Meat/fish
     • No grains
     • Vegetables
     • Healthy fats
   - Keto:
     • High protein
     • Low carb vegetables
     • Healthy fats
     • No grains
   - Low-Carb:
     • Proteins
     • Low carb vegetables
     • Healthy fats
     • Limited grains
   - Whole Food Plant-Based:
     • Plant proteins
     • Whole grains
     • Vegetables
     • Plant fats
   - High-Protein:
     • High protein foods
     • Vegetables
     • Healthy fats
     • Limited grains
   - Diabetic-Friendly:
     • Lean proteins
     • Low glycemic vegetables
     • Healthy fats
     • Limited grains

3. Budget Adaptation:
   - Tight ($3-$7):
     • Budget proteins
     • Basic grains
     • Seasonal vegetables
     • Basic oils
   - Moderate ($8-$15):
     • Mix of proteins
     • Quality grains
     • Fresh vegetables
     • Quality oils
   - High ($15+):
     • Premium proteins
     • Specialty grains
     • Premium vegetables
     • Premium oils

4. Time Adaptation:
   - Busy (15 mins):
     • Quick-cook proteins
     • Quick-cook grains
     • Pre-cut vegetables
     • Simple ingredients
   - Moderate (30 mins):
     • Standard proteins
     • Standard grains
     • Fresh-cut vegetables
     • Standard ingredients
   - Relaxed (45+ mins):
     • Complex proteins
     • Complex grains
     • Fresh vegetables
     • Complex ingredients

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free proteins
     • Nut-free grains
     • Safe vegetables
     • Safe oils
   - Dairy Intolerance:
     • Dairy-free proteins
     • Dairy-free grains
     • Safe vegetables
     • Dairy-free fats
   - Gluten Intolerance:
     • Gluten-free proteins
     • Gluten-free grains
     • Safe vegetables
     • Safe fats
   - Shellfish Allergy:
     • Shellfish-free proteins
     • Safe grains
     • Safe vegetables
     • Safe fats
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian proteins
     • Pasta/rice
     • Italian vegetables
     • Olive oil
   - Mexican:
     • Mexican proteins
     • Corn/tortillas
     • Mexican vegetables
     • Mexican oils
   - Chinese:
     • Chinese proteins
     • Rice/noodles
     • Chinese vegetables
     • Chinese oils
   - Indian:
     • Indian proteins
     • Rice/naan
     • Indian vegetables
     • Indian oils
   - Japanese:
     • Japanese proteins
     • Rice/noodles
     • Japanese vegetables
     • Japanese oils
   - Thai:
     • Thai proteins
     • Rice/noodles
     • Thai vegetables
     • Thai oils
   - Mediterranean:
     • Mediterranean proteins
     • Mediterranean grains
     • Mediterranean vegetables
     • Olive oil
   - Australian:
     • Local proteins
     • Local grains
     • Local vegetables
     • Local oils
   - All Cuisines:
     • Mix of proteins
     • Mix of grains
     • Mix of vegetables
     • Mix of oils
"""

# Cooking Methods
COOKING_METHODS = """
**COOKING METHODS:**
- Choose appropriate methods
- Consider time constraints
- Use equipment available
- Adapt for dietary needs

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Low-sodium cooking
     • Steaming
     • Poaching
     • Grilling without salt
   - Diabetes:
     • Low-fat methods
     • Steaming
     • Baking
     • Grilling
   - Heart Disease:
     • Heart-healthy methods
     • Steaming
     • Baking
     • Grilling
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant-based methods
     • Tofu pressing
     • Tempeh marinating
     • Vegetable roasting
   - Vegan:
     • Plant-based methods
     • Tofu pressing
     • Tempeh marinating
     • Vegetable roasting
   - Pescatarian:
     • Seafood methods
     • Fish poaching
     • Shellfish steaming
     • Fish grilling
   - Mediterranean:
     • Olive oil methods
     • Grilling
     • Baking
     • Steaming
   - Paleo:
     • Meat methods
     • Grilling
     • Roasting
     • Pan-frying
   - Keto:
     • High-fat methods
     • Pan-frying
     • Baking
     • Grilling
   - Low-Carb:
     • Low-carb methods
     • Steaming
     • Baking
     • Grilling
   - Whole Food Plant-Based:
     • Plant methods
     • Steaming
     • Baking
     • Roasting
   - High-Protein:
     • Protein methods
     • Grilling
     • Baking
     • Pan-frying
   - Diabetic-Friendly:
     • Low-fat methods
     • Steaming
     • Baking
     • Grilling

3. Budget Adaptation:
   - Tight ($3-$7):
     • Simple methods
     • One-pot cooking
     • Basic equipment
     • Minimal prep
   - Moderate ($8-$15):
     • Standard methods
     • Multi-step cooking
     • Standard equipment
     • Moderate prep
   - High ($15+):
     • Complex methods
     • Multi-pan cooking
     • Premium equipment
     • Extensive prep

4. Time Adaptation:
   - Busy (15 mins):
     • Quick methods
     • One-pan cooking
     • Pre-cut ingredients
     • Minimal prep
   - Moderate (30 mins):
     • Standard methods
     • Two-pan cooking
     • Standard prep
     • Moderate steps
   - Relaxed (45+ mins):
     • Complex methods
     • Multi-pan cooking
     • Full prep
     • Multiple steps

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free methods
     • Separate equipment
     • Cross-contamination prevention
     • Safe alternatives
   - Dairy Intolerance:
     • Dairy-free methods
     • Plant-based alternatives
     • Safe equipment
     • Safe prep
   - Gluten Intolerance:
     • Gluten-free methods
     • Separate equipment
     • Safe alternatives
     • Safe prep
   - Shellfish Allergy:
     • Shellfish-free methods
     • Separate equipment
     • Safe alternatives
     • Safe prep
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Pasta cooking
     • Sauce making
     • Pizza baking
     • Risotto making
   - Mexican:
     • Tortilla making
     • Taco assembly
     • Salsa making
     • Guacamole making
   - Chinese:
     • Stir-frying
     • Steaming
     • Wok cooking
     • Sauce making
   - Indian:
     • Curry making
     • Rice cooking
     • Naan baking
     • Spice toasting
   - Japanese:
     • Sushi making
     • Tempura frying
     • Miso making
     • Rice cooking
   - Thai:
     • Curry making
     • Stir-frying
     • Rice cooking
     • Sauce making
   - Mediterranean:
     • Grilling
     • Baking
     • Steaming
     • Sauce making
   - Australian:
     • BBQ methods
     • Roasting
     • Grilling
     • Baking
   - All Cuisines:
     • Mix of methods
     • Adapt to ingredients
     • Consider equipment
     • Match cuisine style
"""

# Seasoning
SEASONING = """
**SEASONING:**
- Use appropriate seasonings
- Consider dietary restrictions
- Adapt to time constraints
- Match budget constraints

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • No added salt
     • Herbs and spices
     • Citrus
     • Vinegars
   - Diabetes:
     • Low-sugar seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Heart Disease:
     • Low-sodium seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant-based seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Vegan:
     • Plant-based seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Pescatarian:
     • Seafood seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Mediterranean:
     • Mediterranean herbs
     • Olive oil
     • Citrus
     • Vinegars
   - Paleo:
     • Natural seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Keto:
     • Low-carb seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Low-Carb:
     • Low-carb seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Whole Food Plant-Based:
     • Plant-based seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - High-Protein:
     • Protein seasonings
     • Herbs and spices
     • Citrus
     • Vinegars
   - Diabetic-Friendly:
     • Low-sugar seasonings
     • Herbs and spices
     • Citrus
     • Vinegars

3. Budget Adaptation:
   - Tight ($3-$7):
     • Basic herbs
     • Basic spices
     • Basic oils
     • Basic vinegars
   - Moderate ($8-$15):
     • Standard herbs
     • Standard spices
     • Quality oils
     • Quality vinegars
   - High ($15+):
     • Premium herbs
     • Premium spices
     • Premium oils
     • Premium vinegars

4. Time Adaptation:
   - Busy (15 mins):
     • Quick seasonings
     • Pre-mixed blends
     • Basic herbs
     • Basic spices
   - Moderate (30 mins):
     • Standard seasonings
     • Custom blends
     • Fresh herbs
     • Fresh spices
   - Relaxed (45+ mins):
     • Complex seasonings
     • Multiple blends
     • Premium herbs
     • Premium spices

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free seasonings
     • Safe herbs
     • Safe spices
     • Safe oils
   - Dairy Intolerance:
     • Dairy-free seasonings
     • Safe herbs
     • Safe spices
     • Safe oils
   - Gluten Intolerance:
     • Gluten-free seasonings
     • Safe herbs
     • Safe spices
     • Safe oils
   - Shellfish Allergy:
     • Shellfish-free seasonings
     • Safe herbs
     • Safe spices
     • Safe oils
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian herbs
     • Italian spices
     • Olive oil
     • Balsamic vinegar
   - Mexican:
     • Mexican herbs
     • Mexican spices
     • Mexican oils
     • Mexican vinegars
   - Chinese:
     • Chinese herbs
     • Chinese spices
     • Chinese oils
     • Chinese vinegars
   - Indian:
     • Indian herbs
     • Indian spices
     • Indian oils
     • Indian vinegars
   - Japanese:
     • Japanese herbs
     • Japanese spices
     • Japanese oils
     • Japanese vinegars
   - Thai:
     • Thai herbs
     • Thai spices
     • Thai oils
     • Thai vinegars
   - Mediterranean:
     • Mediterranean herbs
     • Mediterranean spices
     • Olive oil
     • Mediterranean vinegars
   - Australian:
     • Local herbs
     • Local spices
     • Local oils
     • Local vinegars
   - All Cuisines:
     • Mix of herbs
     • Mix of spices
     • Mix of oils
     • Mix of vinegars
"""

# Complete Meals
COMPLETE_MEALS = """
**COMPLETE MEALS:**
- Include all components
- Balance nutrients
- Consider dietary needs
- Adapt to time constraints

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Low-sodium main
     • Potassium-rich sides
     • Heart-healthy fats
     • Fresh vegetables
   - Diabetes:
     • Low glycemic main
     • Fiber-rich sides
     • Healthy fats
     • Fresh vegetables
   - Heart Disease:
     • Heart-healthy main
     • Whole grain sides
     • Healthy fats
     • Fresh vegetables
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant-based main
     • Vegetarian sides
     • Plant fats
     • Fresh vegetables
   - Vegan:
     • Vegan main
     • Vegan sides
     • Plant fats
     • Fresh vegetables
   - Pescatarian:
     • Seafood main
     • Vegetarian sides
     • Healthy fats
     • Fresh vegetables
   - Mediterranean:
     • Mediterranean main
     • Mediterranean sides
     • Olive oil
     • Fresh vegetables
   - Paleo:
     • Paleo main
     • Paleo sides
     • Healthy fats
     • Fresh vegetables
   - Keto:
     • Keto main
     • Keto sides
     • High fats
     • Low-carb vegetables
   - Low-Carb:
     • Low-carb main
     • Low-carb sides
     • Healthy fats
     • Low-carb vegetables
   - Whole Food Plant-Based:
     • Plant-based main
     • Plant-based sides
     • Plant fats
     • Fresh vegetables
   - High-Protein:
     • High-protein main
     • Protein-rich sides
     • Healthy fats
     • Fresh vegetables
   - Diabetic-Friendly:
     • Low glycemic main
     • Fiber-rich sides
     • Healthy fats
     • Fresh vegetables

3. Budget Adaptation:
   - Tight ($3-$7):
     • Budget main
     • Basic sides
     • Basic fats
     • Basic vegetables
   - Moderate ($8-$15):
     • Standard main
     • Quality sides
     • Quality fats
     • Quality vegetables
   - High ($15+):
     • Premium main
     • Premium sides
     • Premium fats
     • Premium vegetables

4. Time Adaptation:
   - Busy (15 mins):
     • Quick main
     • Quick sides
     • Simple fats
     • Quick vegetables
   - Moderate (30 mins):
     • Standard main
     • Standard sides
     • Standard fats
     • Standard vegetables
   - Relaxed (45+ mins):
     • Complex main
     • Complex sides
     • Complex fats
     • Complex vegetables

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free main
     • Nut-free sides
     • Safe fats
     • Safe vegetables
   - Dairy Intolerance:
     • Dairy-free main
     • Dairy-free sides
     • Safe fats
     • Safe vegetables
   - Gluten Intolerance:
     • Gluten-free main
     • Gluten-free sides
     • Safe fats
     • Safe vegetables
   - Shellfish Allergy:
     • Shellfish-free main
     • Safe sides
     • Safe fats
     • Safe vegetables
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian main
     • Italian sides
     • Italian fats
     • Italian vegetables
   - Mexican:
     • Mexican main
     • Mexican sides
     • Mexican fats
     • Mexican vegetables
   - Chinese:
     • Chinese main
     • Chinese sides
     • Chinese fats
     • Chinese vegetables
   - Indian:
     • Indian main
     • Indian sides
     • Indian fats
     • Indian vegetables
   - Japanese:
     • Japanese main
     • Japanese sides
     • Japanese fats
     • Japanese vegetables
   - Thai:
     • Thai main
     • Thai sides
     • Thai fats
     • Thai vegetables
   - Mediterranean:
     • Mediterranean main
     • Mediterranean sides
     • Mediterranean fats
     • Mediterranean vegetables
   - Australian:
     • Local main
     • Local sides
     • Local fats
     • Local vegetables
   - All Cuisines:
     • Mix of mains
     • Mix of sides
     • Mix of fats
     • Mix of vegetables
"""

# Food Waste Prevention
FOOD_WASTE_PREVENTION = """
**FOOD WASTE PREVENTION:**
- Minimize waste
- Use leftovers
- Plan portions
- Store properly

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Fresh ingredients
     • Proper storage
     • Portion control
     • Leftover planning
   - Diabetes:
     • Fresh ingredients
     • Portion control
     • Storage planning
     • Leftover planning
   - Heart Disease:
     • Fresh ingredients
     • Proper storage
     • Portion control
     • Leftover planning
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - Vegan:
     • Plant storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - Pescatarian:
     • Seafood storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - Mediterranean:
     • Fresh storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - Paleo:
     • Fresh storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - Keto:
     • Fresh storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - Low-Carb:
     • Fresh storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - Whole Food Plant-Based:
     • Plant storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - High-Protein:
     • Protein storage
     • Portion planning
     • Leftover use
     • Waste reduction
   - Diabetic-Friendly:
     • Fresh storage
     • Portion planning
     • Leftover use
     • Waste reduction

3. Budget Adaptation:
   - Tight ($3-$7):
     • Basic storage
     • Exact portions
     • Leftover use
     • Minimal waste
   - Moderate ($8-$15):
     • Standard storage
     • Flexible portions
     • Leftover use
     • Controlled waste
   - High ($15+):
     • Premium storage
     • Flexible portions
     • Leftover use
     • Controlled waste

4. Time Adaptation:
   - Busy (15 mins):
     • Quick storage
     • Pre-portioned
     • Quick leftovers
     • Minimal waste
   - Moderate (30 mins):
     • Standard storage
     • Standard portions
     • Standard leftovers
     • Controlled waste
   - Relaxed (45+ mins):
     • Complex storage
     • Flexible portions
     • Complex leftovers
     • Controlled waste

5. Allergies/Intolerances:
   - Nut Allergies:
     • Safe storage
     • Safe portions
     • Safe leftovers
     • Safe waste
   - Dairy Intolerance:
     • Safe storage
     • Safe portions
     • Safe leftovers
     • Safe waste
   - Gluten Intolerance:
     • Safe storage
     • Safe portions
     • Safe leftovers
     • Safe waste
   - Shellfish Allergy:
     • Safe storage
     • Safe portions
     • Safe leftovers
     • Safe waste
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian storage
     • Italian portions
     • Italian leftovers
     • Italian waste
   - Mexican:
     • Mexican storage
     • Mexican portions
     • Mexican leftovers
     • Mexican waste
   - Chinese:
     • Chinese storage
     • Chinese portions
     • Chinese leftovers
     • Chinese waste
   - Indian:
     • Indian storage
     • Indian portions
     • Indian leftovers
     • Indian waste
   - Japanese:
     • Japanese storage
     • Japanese portions
     • Japanese leftovers
     • Japanese waste
   - Thai:
     • Thai storage
     • Thai portions
     • Thai leftovers
     • Thai waste
   - Mediterranean:
     • Mediterranean storage
     • Mediterranean portions
     • Mediterranean leftovers
     • Mediterranean waste
   - Australian:
     • Local storage
     • Local portions
     • Local leftovers
     • Local waste
   - All Cuisines:
     • Mix of storage
     • Mix of portions
     • Mix of leftovers
     • Mix of waste
"""

# Measurements
MEASUREMENTS = """
**MEASUREMENTS:**
- Use appropriate units
- Consider serving size
- Adapt to equipment
- Match cuisine style

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Precise measurements
     • Portion control
     • Salt-free options
     • Potassium-rich amounts
   - Diabetes:
     • Precise measurements
     • Portion control
     • Carb counting
     • Fiber amounts
   - Heart Disease:
     • Precise measurements
     • Portion control
     • Fat amounts
     • Fiber amounts
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant measurements
     • Protein amounts
     • Portion sizes
     • Alternative amounts
   - Vegan:
     • Plant measurements
     • Protein amounts
     • Portion sizes
     • Alternative amounts
   - Pescatarian:
     • Seafood measurements
     • Portion sizes
     • Alternative amounts
     • Balance amounts
   - Mediterranean:
     • Mediterranean measurements
     • Portion sizes
     • Balance amounts
     • Oil amounts
   - Paleo:
     • Paleo measurements
     • Portion sizes
     • Alternative amounts
     • Balance amounts
   - Keto:
     • Keto measurements
     • Portion sizes
     • Fat amounts
     • Carb amounts
   - Low-Carb:
     • Low-carb measurements
     • Portion sizes
     • Carb amounts
     • Alternative amounts
   - Whole Food Plant-Based:
     • Plant measurements
     • Portion sizes
     • Alternative amounts
     • Balance amounts
   - High-Protein:
     • Protein measurements
     • Portion sizes
     • Balance amounts
     • Alternative amounts
   - Diabetic-Friendly:
     • Precise measurements
     • Portion sizes
     • Carb amounts
     • Alternative amounts

3. Budget Adaptation:
   - Tight ($3-$7):
     • Basic measurements
     • Standard portions
     • Basic amounts
     • Simple units
   - Moderate ($8-$15):
     • Standard measurements
     • Flexible portions
     • Standard amounts
     • Standard units
   - High ($15+):
     • Premium measurements
     • Flexible portions
     • Premium amounts
     • Premium units

4. Time Adaptation:
   - Busy (15 mins):
     • Quick measurements
     • Pre-portioned
     • Simple amounts
     • Quick units
   - Moderate (30 mins):
     • Standard measurements
     • Standard portions
     • Standard amounts
     • Standard units
   - Relaxed (45+ mins):
     • Complex measurements
     • Flexible portions
     • Complex amounts
     • Complex units

5. Allergies/Intolerances:
   - Nut Allergies:
     • Safe measurements
     • Safe portions
     • Safe amounts
     • Safe units
   - Dairy Intolerance:
     • Safe measurements
     • Safe portions
     • Safe amounts
     • Safe units
   - Gluten Intolerance:
     • Safe measurements
     • Safe portions
     • Safe amounts
     • Safe units
   - Shellfish Allergy:
     • Safe measurements
     • Safe portions
     • Safe amounts
     • Safe units
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian measurements
     • Italian portions
     • Italian amounts
     • Italian units
   - Mexican:
     • Mexican measurements
     • Mexican portions
     • Mexican amounts
     • Mexican units
   - Chinese:
     • Chinese measurements
     • Chinese portions
     • Chinese amounts
     • Chinese units
   - Indian:
     • Indian measurements
     • Indian portions
     • Indian amounts
     • Indian units
   - Japanese:
     • Japanese measurements
     • Japanese portions
     • Japanese amounts
     • Japanese units
   - Thai:
     • Thai measurements
     • Thai portions
     • Thai amounts
     • Thai units
   - Mediterranean:
     • Mediterranean measurements
     • Mediterranean portions
     • Mediterranean amounts
     • Mediterranean units
   - Australian:
     • Local measurements
     • Local portions
     • Local amounts
     • Local units
   - All Cuisines:
     • Mix of measurements
     • Mix of portions
     • Mix of amounts
     • Mix of units
"""

# Ingredient Names
INGREDIENT_NAMES = """
**INGREDIENT NAMES:**
- Use common names
- Consider availability
- Match cuisine style
- Adapt to region

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Low-sodium options
     • Potassium-rich names
     • Heart-healthy terms
     • Fresh ingredients
   - Diabetes:
     • Low glycemic terms
     • Fiber-rich names
     • Healthy options
     • Fresh ingredients
   - Heart Disease:
     • Heart-healthy terms
     • Low-fat options
     • Fresh ingredients
     • Healthy names
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant-based terms
     • Protein alternatives
     • Fresh ingredients
     • Common names
   - Vegan:
     • Plant-based terms
     • Protein alternatives
     • Fresh ingredients
     • Common names
   - Pescatarian:
     • Seafood terms
     • Plant alternatives
     • Fresh ingredients
     • Common names
   - Mediterranean:
     • Mediterranean terms
     • Fresh ingredients
     • Common names
     • Regional options
   - Paleo:
     • Paleo terms
     • Natural names
     • Fresh ingredients
     • Common options
   - Keto:
     • Keto terms
     • Low-carb names
     • Fresh ingredients
     • Common options
   - Low-Carb:
     • Low-carb terms
     • Fresh names
     • Common ingredients
     • Healthy options
   - Whole Food Plant-Based:
     • Plant terms
     • Natural names
     • Fresh ingredients
     • Common options
   - High-Protein:
     • Protein terms
     • Fresh names
     • Common ingredients
     • Healthy options
   - Diabetic-Friendly:
     • Low glycemic terms
     • Fresh names
     • Common ingredients
     • Healthy options

3. Budget Adaptation:
   - Tight ($3-$7):
     • Basic terms
     • Common names
     • Budget options
     • Simple ingredients
   - Moderate ($8-$15):
     • Standard terms
     • Quality names
     • Mixed options
     • Standard ingredients
   - High ($15+):
     • Premium terms
     • Specialty names
     • Premium options
     • Premium ingredients

4. Time Adaptation:
   - Busy (15 mins):
     • Quick terms
     • Pre-cut names
     • Simple options
     • Quick ingredients
   - Moderate (30 mins):
     • Standard terms
     • Fresh names
     • Standard options
     • Standard ingredients
   - Relaxed (45+ mins):
     • Complex terms
     • Specialty names
     • Complex options
     • Complex ingredients

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free terms
     • Safe names
     • Alternative options
     • Safe ingredients
   - Dairy Intolerance:
     • Dairy-free terms
     • Safe names
     • Alternative options
     • Safe ingredients
   - Gluten Intolerance:
     • Gluten-free terms
     • Safe names
     • Alternative options
     • Safe ingredients
   - Shellfish Allergy:
     • Shellfish-free terms
     • Safe names
     • Alternative options
     • Safe ingredients
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian terms
     • Italian names
     • Italian options
     • Italian ingredients
   - Mexican:
     • Mexican terms
     • Mexican names
     • Mexican options
     • Mexican ingredients
   - Chinese:
     • Chinese terms
     • Chinese names
     • Chinese options
     • Chinese ingredients
   - Indian:
     • Indian terms
     • Indian names
     • Indian options
     • Indian ingredients
   - Japanese:
     • Japanese terms
     • Japanese names
     • Japanese options
     • Japanese ingredients
   - Thai:
     • Thai terms
     • Thai names
     • Thai options
     • Thai ingredients
   - Mediterranean:
     • Mediterranean terms
     • Mediterranean names
     • Mediterranean options
     • Mediterranean ingredients
   - Australian:
     • Local terms
     • Local names
     • Local options
     • Local ingredients
   - All Cuisines:
     • Mix of terms
     • Mix of names
     • Mix of options
     • Mix of ingredients
"""

# Instructions
INSTRUCTIONS = """
**INSTRUCTIONS:**
- Clear and concise steps
- Consider skill level
- Adapt to equipment
- Match time constraints

Adaptations Based on User Requirements:

1. Health Conditions:
   - Hypertension:
     • Low-sodium steps
     • Potassium-rich prep
     • Heart-healthy methods
     • Fresh preparation
   - Diabetes:
     • Low glycemic prep
     • Fiber-rich steps
     • Healthy methods
     • Fresh preparation
   - Heart Disease:
     • Heart-healthy steps
     • Low-fat prep
     • Healthy methods
     • Fresh preparation
   - Other Conditions:
     • Adapt based on specific needs

2. Diet Type:
   - Vegetarian:
     • Plant-based steps
     • Protein prep
     • Fresh methods
     • Common techniques
   - Vegan:
     • Plant-based steps
     • Protein prep
     • Fresh methods
     • Common techniques
   - Pescatarian:
     • Seafood steps
     • Plant prep
     • Fresh methods
     • Common techniques
   - Mediterranean:
     • Mediterranean steps
     • Fresh prep
     • Common methods
     • Regional techniques
   - Paleo:
     • Paleo steps
     • Natural prep
     • Fresh methods
     • Common techniques
   - Keto:
     • Keto steps
     • Low-carb prep
     • Fresh methods
     • Common techniques
   - Low-Carb:
     • Low-carb steps
     • Fresh prep
     • Common methods
     • Healthy techniques
   - Whole Food Plant-Based:
     • Plant steps
     • Natural prep
     • Fresh methods
     • Common techniques
   - High-Protein:
     • Protein steps
     • Fresh prep
     • Common methods
     • Healthy techniques
   - Diabetic-Friendly:
     • Low glycemic steps
     • Fresh prep
     • Common methods
     • Healthy techniques

3. Budget Adaptation:
   - Tight ($3-$7):
     • Basic steps
     • Simple prep
     • Common methods
     • Basic techniques
   - Moderate ($8-$15):
     • Standard steps
     • Quality prep
     • Mixed methods
     • Standard techniques
   - High ($15+):
     • Premium steps
     • Specialty prep
     • Premium methods
     • Premium techniques

4. Time Adaptation:
   - Busy (15 mins):
     • Quick steps
     • Pre-cut prep
     • Simple methods
     • Quick techniques
   - Moderate (30 mins):
     • Standard steps
     • Fresh prep
     • Standard methods
     • Standard techniques
   - Relaxed (45+ mins):
     • Complex steps
     • Specialty prep
     • Complex methods
     • Complex techniques

5. Allergies/Intolerances:
   - Nut Allergies:
     • Nut-free steps
     • Safe prep
     • Alternative methods
     • Safe techniques
   - Dairy Intolerance:
     • Dairy-free steps
     • Safe prep
     • Alternative methods
     • Safe techniques
   - Gluten Intolerance:
     • Gluten-free steps
     • Safe prep
     • Alternative methods
     • Safe techniques
   - Shellfish Allergy:
     • Shellfish-free steps
     • Safe prep
     • Alternative methods
     • Safe techniques
   - Other Allergies:
     • Adapt based on specific allergens

6. Cuisine-Specific Adaptations:
   - Italian:
     • Italian steps
     • Italian prep
     • Italian methods
     • Italian techniques
   - Mexican:
     • Mexican steps
     • Mexican prep
     • Mexican methods
     • Mexican techniques
   - Chinese:
     • Chinese steps
     • Chinese prep
     • Chinese methods
     • Chinese techniques
   - Indian:
     • Indian steps
     • Indian prep
     • Indian methods
     • Indian techniques
   - Japanese:
     • Japanese steps
     • Japanese prep
     • Japanese methods
     • Japanese techniques
   - Thai:
     • Thai steps
     • Thai prep
     • Thai methods
     • Thai techniques
   - Mediterranean:
     • Mediterranean steps
     • Mediterranean prep
     • Mediterranean methods
     • Mediterranean techniques
   - Australian:
     • Local steps
     • Local prep
     • Local methods
     • Local techniques
   - All Cuisines:
     • Mix of steps
     • Mix of prep
     • Mix of methods
     • Mix of techniques
"""

def get_budget_constraints(budget_type):
    constraints = {
        "Tight budget ($3-$7)": {
            "range": "$3-$7",
            "proteins": ["eggs", "canned tuna", "tofu", "lentils", "chickpeas"],
            "vegetables": ["frozen", "pre-cut", "seasonal"],
            "grains": ["rice", "oats", "wholemeal bread"],
            "avoid": ["puff pastry", "quinoa", "specialty items", "expensive cuts of meat"]
        },
        "Moderate budget ($8-$15)": {
            "range": "$8-$15",
            "proteins": ["chicken breast", "fish fillets", "lean beef", "tofu", "lentils"],
            "vegetables": ["fresh", "frozen", "pre-cut"],
            "grains": ["rice", "quinoa", "wholemeal bread", "pasta"],
            "avoid": ["premium cuts", "exotic ingredients"]
        },
        "Generous budget ($16-$30)": {
            "range": "$16-$30",
            "proteins": ["salmon", "prawns", "lean beef", "chicken breast", "tofu"],
            "vegetables": ["fresh", "organic", "pre-cut"],
            "grains": ["quinoa", "brown rice", "wholemeal pasta"],
            "avoid": []
        },
        "No budget constraints ($31+)": {
            "range": "$31+",
            "proteins": ["premium cuts", "seafood", "organic meats", "tofu"],
            "vegetables": ["organic", "fresh", "pre-cut"],
            "grains": ["quinoa", "brown rice", "wholemeal pasta"],
            "avoid": []
        }
    }
    return constraints.get(budget_type, constraints["Tight budget ($3-$7)"])

def get_time_constraints(time_constraint):
    constraints = {
        "Busy schedule (15 mins)": {
            "max_time": "15 minutes",
            "methods": ["stir-fry", "pan-fry", "boiling", "air-frying"],
            "avoid": ["baking", "roasting", "slow-cooking"],
            "prep": ["pre-cut", "canned", "frozen"],
            "steps": ["simple", "quick", "minimal"]
        },
        "Moderate schedule (30 mins)": {
            "max_time": "30 minutes",
            "methods": ["stir-fry", "pan-fry", "boiling", "baking", "air-frying"],
            "avoid": ["slow-cooking", "complex techniques"],
            "prep": ["fresh", "pre-cut", "canned"],
            "steps": ["moderate", "standard", "balanced"]
        },
        "Busy on some days (45 mins)": {
            "max_time": "45 minutes",
            "methods": ["all methods"],
            "avoid": ["slow-cooking"],
            "prep": ["fresh", "pre-cut", "canned"],
            "steps": ["detailed", "elaborate", "complex"]
        },
        "Flexible Schedule (60 mins)": {
            "max_time": "60 minutes",
            "methods": ["all methods"],
            "avoid": [],
            "prep": ["fresh", "pre-cut", "canned"],
            "steps": ["detailed", "elaborate", "complex"]
        },
        "No Constraints (Any duration)": {
            "max_time": "No limit",
            "methods": ["all methods"],
            "avoid": [],
            "prep": ["fresh", "pre-cut", "canned"],
            "steps": ["detailed", "elaborate", "complex"]
        }
    }
    return constraints[time_constraint]

def get_meal_prompt(meal_type, day, user_prefs, health_requirements, cuisine_requirements, available_ingredients=None):
    # Get budget and time constraints
    budget_constraints = get_budget_constraints(user_prefs['budget'])
    time_constraints = get_time_constraints(user_prefs['time_constraint'])

    # Add available ingredients to the prompt if provided
    ingredients_section = ""
    if available_ingredients:
        ingredients_section = f"""
Available Ingredients:
{', '.join(available_ingredients)}

Please use only these ingredients in your recipe. If you need additional ingredients, they should be common pantry staples or easily available in Australian supermarkets.
"""

    prompt = f"""Generate a recipe for {meal_type} for Day {day} that features {user_prefs['cuisine']} cuisine and adheres to the following criteria:

User Preferences:
- Diet Type: {user_prefs['diet']}
- Allergies: {user_prefs['allergies']}
- Health Conditions: {user_prefs['health_conditions']}
- Budget: {user_prefs['budget']}
- Time Constraint: {user_prefs['time_constraint']}
- Serving Size: {user_prefs['serving_size']}

Health Requirements:
{health_requirements}

Cuisine Requirements:
{cuisine_requirements}

{ingredients_section}

Budget Constraints:
- Price Range: {budget_constraints['range']}
- Recommended Proteins: {', '.join(budget_constraints['proteins'])}
- Recommended Vegetables: {', '.join(budget_constraints['vegetables'])}
- Recommended Grains: {', '.join(budget_constraints['grains'])}
- Avoid: {', '.join(budget_constraints['avoid'])}

Time Constraints:
- Maximum Time: {time_constraints['max_time']}

**RECIPE UNIQUENESS REQUIREMENTS:**
1. Recipe Name:
    - Must be completely different from all previous recipes
    - Should not use words from previous recipe names
    - Must reflect the unique characteristics of this dish

2. Description Style:
    - Must use a different writing style than previous descriptions
    - it should be 400-450 character wich will leads to 3-4 sentence engaging, fun, humorous, and creative introduction for a recipe.
    - Should not start with same phrases as other descriptions
    - Must highlight unique aspects of this specific dish
    - Should avoid common phrases used in other descriptions

3. Protein Selection:
    - Must use a different protein than the last 3 meals
    - If using same protein category, must use different cut/preparation
    - Must use different cooking method for the protein

4. Cooking Methods:
    - Must use different primary cooking method than previous 2 meals
    - Should combine techniques in unique ways
    - Must avoid repeating signature techniques

5. Vegetables and Aromatics:
    - Must use different vegetable combinations than previous 3 meals
    - Should introduce at least 2 vegetables not used in previous meals
    - Must use different aromatic combinations

6. Sauces and Seasonings:
    - Must create unique sauce combinations
    - Should not repeat primary seasoning profiles
    - Must use different ratios of sweet/salty/sour/spicy

7. Texture Combinations:
    - Must provide different textural experience than previous meals
    - Should incorporate unique crispy/soft/chewy elements
    - Must vary temperature and moisture content

8. Presentation Style:
    - Must use different plating approach than previous meals
    - Should incorporate unique garnishing elements
    - Must vary color combinations and arrangement

9. Flavor Profile:
    - Must develop distinct flavor profile from previous meals
    - Should balance flavors differently than other dishes
    - Must create unique taste progression

10. Cultural Elements:
     - Must highlight different aspects of Thai cuisine
     - Should draw from different regional influences
     - Must incorporate unique cultural techniques

The recipe should be formatted as follows:

**RECIPE FORMAT:**
**Day {day} - {meal_type} - [Generate a fun, unique, and creative name for a recipe based on the details above. The name should be playful, engaging, and make the dish sound irresistible. Use puns, alliteration, or intriguing phrases, but avoid generic or repetitive names. For example: 'Spicy Kimchi Fried Rice Delight' (Korean), 'Tuscan Herb-Crusted Salmon' (Italian)]**

**Description:**
[Choose one of the descriptions below as the foundation for the introduction, ensuring it aligns with the recipe without repeating it. Each introduction should be unique, so avoid using the same description style twice. Keep it engaging and concise, maintaining a single captivating paragraph without splitting it into multiple sections. The description should be 400-450 characters. For example: 'Embark on a culinary journey to the heart of Italy with this vibrant pasta dish...' (Italian), 'Experience the bold flavors of Korea with this spicy and savory rice dish...' (Korean)]

"Start your day with a meal that feels like a warm hug! Rich flavors and wholesome ingredients blend together, delivering the perfect balance of comfort and nutrition. Whether it's a crisp morning or a cozy evening, every bite brings home-cooked goodness that warms the soul. This dish is a reminder that food isn't just fuel—it's a connection to nostalgia, happiness, and the joy of simple pleasures.",

"Bursting with color and vibrancy, this dish is a celebration of freshness and flavor! Crisp vegetables, fragrant herbs, and zesty spices come together in perfect harmony, creating an energizing meal that awakens the senses. Every bite is light yet deeply satisfying, offering a refreshing balance that makes it a perfect choice for any time of day. Eat bright, feel light, and fuel yourself with pure goodness!",

"Get ready for a bold flavor explosion! This dish is a spicy kick, teasing your taste buds with just the right amount of intensity. If you love dishes that pack a punch and leave you craving more, this one's a must-try. Spicy, savory, and oh-so-satisfying—flavor lovers, rejoice!",

"Light, refreshing, and packed with flavor, this dish is as delightful as a summer breeze. A combination of fresh ingredients, subtle seasonings, and bright flavors makes every bite feel crisp and rejuvenating. It's perfect for those moments when you want something nourishing yet not too heavy. Enjoy a meal that satisfies without weighing you down, keeping you refreshed and ready for anything!",

"Indulge in pure decadence with this rich and luxurious dish! A true treat for the senses, this meal brings together velvety textures, deep flavors, and a touch of indulgence in every bite. Whether it's a luscious pasta, a silky soup, or a decadent dessert, this meal is pure comfort on a plate. Sometimes, a little bit of creaminess is all you need to turn an ordinary dish into something spectacular!",

"Satisfy your hunger with a hearty, filling meal that delivers comfort and sustenance in every bite. Packed with protein, fiber, and bold flavors, this dish keeps you fueled and energized. Whether you need a power-packed lunch or a satisfying dinner after a long day, it won't disappoint. Hearty, wholesome, and bursting with goodness, this is the kind of food that keeps you going strong!",

"Short on time but still craving something delicious? This dish is the answer! Made with simple, wholesome ingredients, it comes together effortlessly while delivering great flavor and nourishment. Perfect for busy days, it proves that quick meals don't have to sacrifice taste or quality. Whether you're rushing between meetings or need an easy dinner, this dish has you covered in minutes!",

"Some recipes stand the test of time, and this dish is one of them! Rooted in tradition and perfected over generations, it brings together flavors that feel familiar, comforting, and always satisfying. A timeless classic, it reminds us that the best meals don't need fancy reinventions—just great ingredients and a touch of nostalgia. Simple, delicious, and forever a favorite!",

"Elevate your dining experience with this sophisticated and elegant dish! Balanced flavors, delicate textures, and refined ingredients create a meal that feels like something straight out of a gourmet kitchen. Whether you're celebrating a special occasion or just want to add a touch of class to your day, this dish delivers in both taste and presentation. Fine dining, right from your own kitchen!",

"Cozy up with this warm, comforting dish that feels like a big hug on a chilly day! Slow-cooked flavors, aromatic spices, and nourishing ingredients come together to create a meal that soothes the soul. Whether you're looking to unwind after a long day or simply need a bowl of comfort, this dish delivers warmth and satisfaction in every bite. Grab a spoon and let the coziness begin!",

"Enjoy the perfect balance of sweet and savory flavors in this deliciously complex dish! The richness of umami ingredients meets a touch of natural sweetness, creating an irresistible contrast in every bite. It's a delightful experience for your palate, proving that sometimes, the best flavors come from unexpected pairings. Get ready for a dish that keeps your taste buds guessing and wanting more!",

"This dish is an ode to the beauty of simplicity, combining earthy, rustic flavors that feel wholesome and deeply satisfying. Inspired by nature's best, it brings together fresh, unprocessed ingredients for a meal that's as nourishing as it is flavorful. If you love dishes that taste like they came straight from a countryside kitchen, this one's for you—grounded, hearty, and utterly delicious.",

"Stay energized with this nutrient-dense, power-packed meal! Designed to fuel your day, this dish is rich in protein, healthy fats, and complex carbs, providing sustained energy without any crash. Whether you're starting a busy morning or refueling after a workout, this meal keeps you going strong. Nourish your body with ingredients that work for you—delicious, wholesome, and full of life!",

"Craving a meal with crunch? This dish is all about texture! Every bite delivers a satisfying contrast of crisp, crunchy, and savory elements that make it as fun to eat as it is delicious. Whether it's roasted nuts, crisp veggies, or a golden-brown crust, this meal proves that texture plays a big role in great food. A perfect way to add excitement to every mouthful!",

"Rich, aromatic, and deeply flavorful, this dish transforms simple ingredients into something spectacular. The combination of fragrant spices, slow-cooked depth, and layered flavors makes every bite a sensory experience. Whether it's a warming curry, a robust stew, or a spice-infused dish, this one fills the air with enticing aromas and leaves a lasting impression on your palate.",

"Good food nourishes both body and soul, and this dish does exactly that! Packed with essential nutrients, protein, fiber, and healthy fats, it's designed to keep you feeling your best while tasting amazing. Eat well, feel good, and enjoy every bite!",

"A tangy, zesty burst of flavor awaits! This dish is all about bright, citrusy notes that awaken your taste buds and add a refreshing twist to every bite. Whether it's a squeeze of lemon, a dash of vinegar, or a hint of spice, the flavors are bold and exciting. Perfect for when you need a meal that's light, fresh, and packed with just the right amount of zing!",

"Travel the world through flavors with this exotic and adventurous dish! Inspired by global cuisines, it brings together unique spices, bold flavors, and exciting textures for a meal that transports you beyond your kitchen. Whether it's fragrant Thai curry, a Moroccan tagine, or a Latin-inspired dish, this meal is a culinary passport to something extraordinary!",

"Indulge in the creamy, dreamy goodness of this comforting dish! Smooth textures, rich flavors, and a velvety finish make every bite a treat for the senses. Whether it's a luscious pasta, a silky soup, or a decadent dessert, this meal is pure comfort on a plate. Sometimes, a little bit of creaminess is all you need to turn an ordinary dish into something spectacular!",

"Fuel your body with this protein-packed powerhouse! Designed to keep you full and energized, this meal is loaded with high-quality protein, balanced nutrients, and incredible flavor. Whether you're hitting the gym, recovering from a workout, or just need a meal that sustains you through a busy day. Strong, satisfying, and seriously delicious!",

"Why should healthy food be boring? This dish is packed with playful textures, fun flavors, and creative twists that make every bite exciting. Whether it's a surprising ingredient, an unexpected pairing, or a vibrant presentation, this meal proves that good food should be as fun as it is nourishing. Get ready for a plate full of joy!"]

**Total Time**: {time_constraints['max_time']}\n
**Serves**: {user_prefs['serving_size']}

**Ingredients**:
[List all ingredients have to use Australian measurements. Do not use US measurements. Also, it has to use Australian terms, such as "capsicum" instead of "bell pepper." Ensure that units of measurement are relevant to the ingredient type and aligned with Australian supermarket packaging. Liquids should be measured in teaspoons, tablespoons, or millilitres (ml); solids should be measured in grams (g) or whole units (e.g., ½ avocado, 1 zucchini, ½ capsicum); garlic should be measured in cloves; and tomatoes should be measured in halves, quarters, etc. Where possible, reference Coles or Woolworths packaging sizes to ensure realistic portioning.]

**Instructions**:
Write comprehensive and user-friendly recipe instructions in UK English using the metric system. **Each instruction must be between 1350 and 1450 characters and there should be exactly 6 steps (can have 7 if absolutely necessary).** Each steps should flow logically, include practical cooking tips, cater to a basic skill level, use an engaging and conversational style, include sensory details, provide clear explanations. For example:

1.  [Set the stage! Begin by prepping your ingredients like a pro. If it's an Italian dish, finely mince the garlic and dice the tomatoes. If it's a Japanese dish, thinly slice the beef or prepare the sushi rice. Remember, no lazy chopping—we want even cuts so everything cooks perfectly. If it's something smells like it's burning, well… act quickly!]
2.  [Time to bring the magic to life! In a sizzling pan, add your base ingredients in the correct order—think of it as layering flavors like a symphony. If it's an Italian dish, sauté the garlic until fragrant. If it's a Japanese dish, sear the beef until browned. Stir things around, letting the aromas build. If it's something smells like it's burning, well… act quickly!]
3.  [This is where things get exciting, so pay attention! Add the main ingredients, but not too fast! We want everything to cook evenly, so take your time. If it's an Italian dish, add the cherry tomatoes and let them soften. If it's a Japanese dish, add the udon noodles and give it a gentle stir. Taste as you go—this is your dish, your masterpiece! Need a bit more salt? A squeeze of lemon? Make those flavor tweaks like a true kitchen artist.]
4.  [The multitasking challenge begins! If there's a side dish, now's the time to start. While your main dish simmers, prep your salad, toast your bread, or just take a victory sip of tea (or wine, I won't judge). Keep an eye on both elements—timing is everything! If something smells like it's burning, well… act quickly! If something smells like it's burning, well… act quickly!]
5.  [Final touch, the grand finale! Your dish is nearly done, so savor this moment. Maybe an extra pinch of herbs for freshness? A final drizzle of olive oil for that perfect finish? Plate it up like you're on a cooking show, and don't forget the garnish. Presentation matters—because we eat with our eyes first!]
6.  [Serving time! Arrange everything beautifully (or just dig in, I won't tell). Take a moment to appreciate your masterpiece before taking that first bite. And hey, if you snap a photo before eating, I totally understand—it's hard to resist when your food looks this good.]

"""
    return prompt