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

# Dietary Requirements
DIETARY_REQUIREMENTS = {
    "None": {
        "allowed": ["all foods"],
        "restricted": [],
        "notes": "No specific dietary restrictions"
    },
    "Whole30": {
        "allowed": ["meat", "fish", "poultry", "eggs", "vegetables", "fruits", "natural fats", "herbs", "spices"],
        "restricted": ["grains", "legumes", "dairy", "added sugar (real or artificial)", "alcohol", "processed foods"],
        "notes": "Eliminates potentially inflammatory foods for 30 days"
    },
    "Paleo": {
        "allowed": ["meat", "fish", "poultry", "vegetables", "fruits", "nuts", "seeds"],
        "restricted": ["grains", "legumes", "dairy", "processed foods", "refined sugar"],
        "notes": "Focus on whole, unprocessed foods thought to be eaten by Paleolithic ancestors"
    },
    "Ketogenic (Keto)": {
        "allowed": ["meat", "fish", "poultry", "eggs", "low-carb vegetables", "healthy fats (oils, avocados, nuts, seeds)"],
        "restricted": ["grains", "sugars", "high-carb fruits", "legumes", "most dairy"],
        "notes": "Maintain high fat, moderate protein, very low carb to induce ketosis"
    },
    "Low-carb / High-protein": {
        "allowed": ["meat", "fish", "poultry", "eggs", "low-carb vegetables", "healthy fats"],
        "restricted": ["grains", "sugars", "high-carb fruits", "legumes", "starchy vegetables"],
        "notes": "Focus on protein and healthy fats while significantly limiting carbohydrates"
    },
    "High-carb / Low-fat": {
        "allowed": ["fruits", "vegetables", "whole grains", "legumes"],
        "restricted": ["oils", "fatty meats", "high-fat dairy", "processed fats"],
        "notes": "Emphasize carbohydrates as the primary energy source while minimizing fat intake"
    },
    "Plant-based": {
        "allowed": ["vegetables", "fruits", "grains", "legumes", "nuts", "seeds", "plant-based oils"],
        "restricted": ["meat", "fish", "poultry", "seafood", "dairy", "eggs", "honey (often)"],
        "notes": "Focus on foods derived from plants"
    },
    "Whole food plant-based": {
        "allowed": ["vegetables", "fruits", "whole grains", "legumes", "nuts", "seeds"],
        "restricted": ["meat", "fish", "poultry", "dairy", "eggs", "processed foods", "oils"],
        "notes": "Emphasize whole, unprocessed plant foods, often excluding added oils"
    },
    "Vegan": {
        "allowed": ["vegetables", "fruits", "grains", "legumes", "nuts", "seeds", "plant-based oils"],
        "restricted": ["meat", "fish", "poultry", "seafood", "dairy", "eggs", "honey", "gelatin", "some additives"],
        "notes": "Avoids all animal products and by-products"
    },
    "Vegetarian (Lacto-ovo)": {
        "allowed": ["vegetables", "fruits", "grains", "legumes", "dairy", "eggs", "plant-based oils"],
        "restricted": ["meat", "fish", "poultry", "seafood"],
        "notes": "Excludes meat, fish, and poultry; allows dairy and eggs"
    },
    "Vegetarian (Lacto)": {
        "allowed": ["vegetables", "fruits", "grains", "legumes", "dairy", "plant-based oils"],
        "restricted": ["meat", "fish", "poultry", "seafood", "eggs"],
        "notes": "Excludes meat, fish, poultry, seafood, and eggs; allows dairy"
    },
    "Vegetarian (Ovo)": {
        "allowed": ["vegetables", "fruits", "grains", "legumes", "eggs", "plant-based oils"],
        "restricted": ["meat", "fish", "poultry", "seafood", "dairy"],
        "notes": "Excludes meat, fish, poultry, seafood, and dairy; allows eggs"
    },
    "Pescatarian": {
        "allowed": ["vegetables", "fruits", "grains", "legumes", "dairy", "eggs", "fish", "seafood", "plant-based oils"],
        "restricted": ["meat", "poultry"],
        "notes": "Excludes meat and poultry; allows fish, seafood, dairy, and eggs"
    },
    "Flexitarian": {
        "allowed": ["mostly plant-based foods", "occasional meat, poultry, fish, dairy, and eggs"],
        "restricted": ["limits on animal products"],
        "notes": "Primarily vegetarian with occasional consumption of animal products"
    },
    "Pegan (Paleo + Vegan hybrid)": {
        "allowed": ["vegetables", "fruits", "nuts", "seeds", "some legumes (sparingly)", "fish (sustainably sourced)", "eggs (pasture-raised)", "small amounts of grass-fed meat"],
        "restricted": ["dairy", "grains", "most legumes", "processed foods", "refined sugar"],
        "notes": "Combines principles of Paleo and Vegan diets, emphasizing whole plant foods and limited animal products"
    },
    "DASH (Dietary Approaches to Stop Hypertension)": {
        "allowed": ["fruits", "vegetables", "whole grains", "lean proteins (fish, poultry)", "low-fat dairy"],
        "restricted": ["red meat", "sugary drinks and sweets", "high-sodium foods", "saturated and trans fats"],
        "notes": "Designed to help manage or prevent high blood pressure"
    },
    "MIND Diet (Mediterranean-DASH hybrid)": {
        "allowed": ["berries", "green leafy vegetables", "nuts", "olive oil", "whole grains", "fish", "poultry", "beans", "wine (in moderation)"],
        "restricted": ["red meat", "butter and stick margarine", "cheese", "pastries and sweets", "fried or fast food"],
        "notes": "Focuses on foods that benefit brain health"
    },
    "Intermittent Fasting (e.g. 16:8, 5:2)": {
        "allowed": ["all foods during eating windows"],
        "restricted": ["food consumption during fasting periods"],
        "notes": "Focuses on when you eat rather than what you eat"
    },
    "Kosher": {
        "allowed": ["foods meeting Kosher dietary laws (separate dairy and meat, no pork or shellfish, etc.)"],
        "restricted": ["non-Kosher foods and combinations"],
        "notes": "Follows Jewish dietary laws outlined in the Torah"
    },
    "Halal": {
        "allowed": ["foods meeting Halal dietary laws (no pork, alcohol, meat slaughtered according to Islamic law, etc.)"],
        "restricted": ["non-Halal foods and preparations"],
        "notes": "Follows Islamic dietary laws outlined in the Quran"
    },
    "Jain": {
        "allowed": ["fruits", "most vegetables (excluding root vegetables like potatoes, onions, garlic)", "grains", "legumes"],
        "restricted": ["root vegetables", "honey", "foods that may have involved violence against living beings"],
        "notes": "Emphasizes non-violence towards all living beings"
    },
    "Buddhist": {
        "allowed": ["varies greatly depending on the sect and individual; often vegetarian or vegan"],
        "restricted": ["often meat, sometimes dairy and eggs; avoidance of intoxicants"],
        "notes": "Dietary practices vary widely; emphasis on mindfulness and compassion"
    },
    "Seventh-day Adventist": {
        "allowed": ["often vegetarian or vegan diets rich in fruits, vegetables, whole grains, legumes, nuts, and seeds; some consume fish and poultry"],
        "restricted": ["pork, shellfish, alcohol, tobacco, caffeine, highly processed foods"],
        "notes": "Emphasizes a healthy lifestyle based on biblical principles"
    },
    "Rastafarian Ital": {
        "allowed": ["foods grown from the earth, often organic and unprocessed; fruits, vegetables, grains, legumes, herbs"],
        "restricted": ["meat, fish (some allow small fish), dairy, eggs, processed foods, salt, artificial additives"],
        "notes": "Focuses on natural, clean, and life-giving foods"
    }
}

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


9. Quality Checks:
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

AUTHENTIC_RECIPE_NAMES = {
    "Traditional Australian / British / American": [
    # --- Breakfast - Tight budget ($3-$7) - Busy schedule (15 mins) ---
    "Porridge with Berries and Honey",
    "Scrambled Eggs on Toast with Avocado",
    "Vegemite on Toast with Sliced Tomato",
    "Baked Beans on Toast",
    "Breakfast Burrito",
    "Fruit Salad with Yogurt",
    "Cheese on Toast",
    "Oatmeal with Brown Sugar",
    "Toast with Peanut Butter and Banana",
    "Crumpets with Butter",
    "Cinnamon Toast",
    "Toast with Honey",
    "Marmite and Cheese on Toast",
    "Breakfast Quesadilla (Simplified)",
    "Weet-Bix with Milk and Fruit",
    "Tea and Toast with Jam",
    "Grits with Butter",
    "Toast with Scrambled Eggs",
    "Fruit and Yogurt Bowl",
    "Cold Cereal with Milk",
    "Scrambled Egg and Cheese Muffin",
    "Toast with Veggie Spread",
    "Porridge with Salt and Butter",
    "Breakfast Tacos",
    "Toast with Ricotta and Honey",
    "Eggy Bread (French Toast)",
    "Yogurt Parfait with Granola",
    "Breakfast Smoothie",
    "Kedgeree (Simplified)",
    "Breakfast Quesadillas",
    "Toast with Peanut Butter and Banana",
    "Marmite on Toast",
    "Bagel with Cream Cheese and Lox (Simplified)",

    # --- Breakfast - Moderate budget ($8-$15) - Moderate schedule (30 mins) ---
    "Pancakes with Maple Syrup and Berries",
    "French Toast with Cinnamon and Fruit Compote",
    "Full English Breakfast (Simplified)",
    "Biscuits and Gravy",
    "Breakfast Frittata with Vegetables",
    "Kedgeree (Fish and Rice)",
    "Breakfast Quesadillas with Salsa and Guacamole",
    "Spinach and Ricotta Rolls with Tomato Relish",
    "Devilled Kidneys on Toast with Mushrooms",
    "Breakfast Hash with Sweet Potatoes and Peppers",
    "Breakfast Burrito Bowls",
    "Corn Fritters with Bacon and Avocado",
    "Smoked Salmon and Cream Cheese Bagel",
    "Huevos Rancheros",
    "Breakfast Bruschetta with Tomatoes and Basil",
    "Crumpets with Smoked Salmon and Cream Cheese",
    "Breakfast Tostadas",
    "Baked Beans with Chorizo and Eggs",
    "Black Pudding and Apple Stack",
    "Corned Beef Hash with Fried Eggs",
    "Breakfast Omelette with Cheese and Ham",
    "Breakfast Crepes with Nutella and Banana",
    "Full Irish Breakfast",
    "Steak and Egg Breakfast Wrap",
    "Breakfast Salad with Grilled Halloumi",
    "Eggs Florentine",
    "Breakfast Pizza with Bacon and Spinach",
    "Breakfast Burger with Bacon and Egg",
    "Smoked Salmon Scramble with Chives",
    "Breakfast Sandwich with Sausage and Peppers",

    # --- Breakfast - Generous budget ($16-$30) - Busy on some days (45 mins) ---
    "Eggs Benedict with Smoked Salmon and Avocado",
    "Steak and Eggs with Breakfast Potatoes and Peppers",
    "Breakfast Board with Avocado, Salmon, and Sourdough",
    "Full English Breakfast Platter",
    "Shrimp and Grits with Andouille Sausage and Creole Sauce",
    "Breakfast Pancakes with Berries and Mascarpone",
    "Eggs Royale with Asparagus and Hollandaise",
    "Crab Cake Benedict with Spicy Aioli",
    "Breakfast Pizza with Bacon and Spinach",
    "Kipper with Scrambled Eggs and Buttered Toast",
    "Chicken and Waffles with Maple Glaze",
    "Breakfast Ramen with Bacon and Soft-Boiled Egg",
    "Bubble and Squeak with Poached Eggs and Hollandaise",
    "Breakfast Tacos with Chorizo and Cilantro Lime Crema",
    "Breakfast Crepes with Berries and Lemon Ricotta",
    "Full Scottish Breakfast",
    "Monte Cristo Sandwich with Raspberry Jam",
    "Breakfast Bowl with Quinoa and Roasted Vegetables",
    "Crumpets with Mushrooms, Bacon, and Cheese",
    "Breakfast Pizza with Sausage, Peppers, and Onions",
    "Steak and Eggs with Hollandaise and Grilled Tomatoes",
    "Full Welsh Breakfast",
    "Breakfast Frittata with Smoked Salmon and Dill",
    "Breakfast Burger with Bacon Jam and Fried Egg",
    "Smoked Haddock Omelette with Cheese Sauce and Toast",
    "Breakfast Sandwich with Sausage and Peppers",

    # --- Breakfast - No budget constraints ($31+) - No Constraints (Any duration) ---
    "Full English Breakfast with All the Trimmings",
    "Steak and Lobster Benedict",
    "Seafood Breakfast Platter",
    "Eggs Royale with Caviar",
    "Crab and Asparagus Omelette with Truffle Oil",
    "Breakfast Tasting Menu",
    "Gamekeeper's Breakfast",
    "Lobster Benedict",
    "Breakfast Barramundi with Avocado and Greens",
    "Smoked Haddock Omelette with Cheese Sauce",
    "Breakfast Chilaquiles with Short Rib",
    "Breakfast Po'boys with Shrimp and Andouille and Creole Remoulade",
    "Breakfast Seafood Stew",
    "Crumpets with Smoked Eel and Horseradish Cream and Dill",

    # --- Lunch - Tight budget ($3-$7) - Busy schedule (15 mins) ---
    "Tuna Mayonnaise Sandwich",
    "Peanut Butter and Jelly Sandwich",
    "Cheese and Salad Wrap",
    "Egg Salad Sandwich",
    "Pasta Salad (simple)",
    "Chicken and Salad Roll",
    "Cheese and Pickle Sandwich",
    "Leftover Chili (reheated)",
    "2-Minute Noodles (upgraded)",
    "Soup and a Roll",
    "Tuna Salad Sandwich",
    "Ham and Cheese Sandwich",
    "Veggie Wrap",
    "Pasta with Tomato Sauce (quick)",
    "Rice and Beans (canned)",
    "Quesadilla (plain)",
    "Leftover Pizza",
    "Salad with Canned Tuna",
    "Baked Potato with Cheese",
    "Instant Ramen (upgraded)",
    "Chicken Caesar Wrap",
    "BLT Sandwich",
    "Soup and Crackers",
    "Hummus and Veggie Wrap",
    "Chicken Noodle Cup",
    "Mac and Cheese Cup",
    "Hard-Boiled Eggs and Fruit",
    "Yogurt and Granola",
    "Fruit Salad",
    "Trail Mix",

    # --- Lunch - Moderate budget ($8-$15) - Moderate schedule (30 mins) ---
    "Chicken Caesar Salad with Grilled Chicken",
    "Chef's Salad with Ham and Turkey",
    "Reuben Sandwich with Chips",
    "Club Sandwich with Fries",
    "Chicken Salad Sandwich on Croissant",
    "Tuna Nicoise Salad",
    "Greek Salad with Grilled Chicken",
    "Pasta Primavera (simple)",
    "Spaghetti with Meat Sauce (quick)",
    "Chicken Stir-Fry with Rice (quick)",
    "Beef Stir-Fry with Noodles (quick)",
    "Fish Tacos with Cabbage Slaw",
    "Shrimp Po'boy (simplified)",
    "Turkey and Avocado Wrap",
    "Quiche with Side Salad (pre-made quiche)",
    "Soup and Sandwich Combo (better quality soup)",
    "Baked Potato Bar",
    "Salad with Grilled Salmon (canned salmon)",
    "Chicken and Rice Soup (homemade)",
    "Tomato Basil Soup with Grilled Cheese (gourmet cheese)",
    "Chicken Fajitas (quick)",
    "Beef Burrito (quick)",
    "Chicken Quesadillas (with veggies)",
    "Ham and Swiss Panini",
    "Caprese Sandwich",
    "Pesto Chicken Sandwich",
    "Chicken and Broccoli Alfredo (quick)",
    "Shrimp Scampi with Linguine (quick)",
    "Chicken Gyro",
    "Falafel Wrap",

    # --- Lunch - Generous budget ($16-$30) - Busy on some days (45 mins) ---
    "Lobster Roll with Fries",
    "Steak Salad with Blue Cheese Dressing",
    "Salmon Caesar Salad",
    "Shrimp and Grits with Garlic Bread",
    "Chicken Parmesan Sandwich (gourmet bread)",
    "Beef Stroganoff with Egg Noodles (homemade sauce)",
    "French Dip Sandwich with Au Jus",
    "Cuban Sandwich with Plantain Chips and Black Beans",
    "Pulled Pork Sandwich with Coleslaw and BBQ Sauce",
    "Croque Monsieur with Salad (homemade Béchamel)",
    "Croque Madame with Salad (homemade Béchamel)",
    "Chicken Pot Pie with Biscuit Topping",
    "Beef Bourguignon with Crusty Bread (quick version)",
    "Lamb Gyro Platter with Tzatziki",
    "Shrimp and Avocado Tostadas with Lime Crema",
    "Grilled Swordfish Sandwich with Pesto Mayo",
    "Crab Cake Sandwich with Aioli",
    "Seafood Pasta Salad with Lemon Vinaigrette",
    "Spicy Tuna Melt with Onion Rings",
    "Chicken and Bacon Ranch Wrap with Avocado",
    "Chicken and Waffle Sandwich with Maple Glaze",
    "Steak Fajitas with All the Fixings",
    "Shrimp and Chorizo Paella (small portion)",
    "Chicken and Sausage Gumbo with Rice",
    "Beef and Barley Soup with Crusty Bread",
    "Lobster Bisque (canned, but with garnishes)",
    "Creamy Tomato Soup with Grilled Cheese Dippers (gourmet cheese)",
    "Chicken and Broccoli Stir-Fry with Brown Rice",
    "Shrimp and Vegetable Skewers with Quinoa",
    "Chicken and Spinach Salad with Citrus Vinaigrette",

    # --- Lunch - No budget constraints ($31+) - No Constraints (Any duration) ---
    "Lobster Salad Sandwich on Brioche with Truffle Aioli",
    "Steak Tartare with Crostini and Quail Egg",
    "Seared Foie Gras Salad with Balsamic Glaze and Fig Jam",
    "Pan-Seared Scallops with Lemon Risotto and White Wine Butter Sauce",
    "Grilled Halibut with Asparagus and Hollandaise",
    "Bouillabaisse with Rouille and Sourdough Bread",
    "Osso Buco with Saffron Risotto and Gremolata",
    "Rack of Lamb with Rosemary Potatoes and Red Wine Reduction",
    "Seafood Tower with Oysters, Shrimp, and Crab and Dipping Sauces",
    "Truffle Mac and Cheese with Lobster and Breadcrumbs",
    "Wagyu Beef Burger with Caramelized Onions and Truffle Fries",
    "Pan-Seared Duck Breast with Cherry Sauce and Wild Rice Pilaf",
    "Crispy Skin Salmon with Beurre Blanc and Roasted Root Vegetables",
    "Seafood Linguine with White Wine Sauce and Garlic Bread",
    "Tuna Tataki Salad with Sesame Dressing and Avocado",
    "Grilled Octopus Salad with Lemon Vinaigrette and Kalamata Olives",
    "Lobster Bisque with Cognac and Sherry",
    "French Onion Soup with Gruyere Croutons and Baguette",
    "Steak and Blue Cheese Salad with Candied Pecans and Balsamic Glaze",
    "Pan-Seared Chilean Sea Bass with Mango Salsa and Black Beans",
    "Lobster Ravioli with Brown Butter Sauce and Crispy Sage",
    "Crispy Duck Confit Salad with Fig Dressing and Goat Cheese",
    "Seafood Cioppino with Sourdough Bread and Garlic Toast",
    "Grilled Swordfish with Mediterranean Salsa and Couscous",
    "Veal Milanese with Arugula Salad and Lemon Vinaigrette",
    "Steak Frites with Béarnaise Sauce and Truffle Salt",
    "Seafood Paella with Saffron Aioli and Grilled Bread",
    "Grilled Lamb Chops with Mint Chimichurri and Roasted Vegetables",
    "Pan-Seared Ahi Tuna with Wasabi Aioli and Seaweed Salad",
    "Roasted Bone Marrow with Parsley Salad and Toasted Baguette",

    # --- Dinner - Tight budget ($3-$7) - Busy schedule (15 mins) ---
    "Spaghetti with Tomato Sauce",
    "Ramen Noodles with Egg",
    "Quesadillas with Beans and Cheese",
    "Tuna Pasta",
    "Rice and Beans",
    "Mac and Cheese",
    "Hot Dogs",
    "Hamburgers",
    "Bean Burritos",
    "Lentil Soup",
    "Tomato Soup",
    "Grilled Cheese and Tomato Soup",
    "Egg Fried Rice",
    "Pasta with Pesto",
    "Veggie Stir-Fry",
    "Chicken Noodle Soup",
    "Baked Potatoes",
    "Salad with Canned Tuna",
    "Scrambled Eggs and Toast",
    "Oatmeal with Veggies",
    "Spaghetti Aglio e Olio",
    "Black Bean Burgers",
    "Quesadillas with Veggies",
    "Rice and Lentils",
    "Veggie Burgers on Buns",
    "Noodle Soup with Tofu",
    "Baked Sweet Potatoes",
    "Salad with Chickpeas",
    "Pasta with Marinara Sauce",
    "Veggie Chili",

    # --- Dinner - Moderate budget ($8-$15) - Moderate schedule (30 mins) ---
    "Chicken Stir-Fry with Rice",
    "Beef Stir-Fry with Noodles",
    "Fish Tacos with Cabbage Slaw",
    "Chicken Fajitas with Peppers and Onions",
    "Beef Burrito Bowls with Guacamole",
    "Spaghetti with Meat Sauce",
    "Chicken Parmesan with Salad",
    "Meatloaf with Mashed Potatoes",
    "Shepherd's Pie",
    "Chicken Pot Pie",
    "Baked Salmon with Roasted Vegetables",
    "Shrimp Scampi with Linguine",
    "Chicken and Broccoli Alfredo",
    "Pork Chops with Applesauce",
    "Steak with Baked Potatoes",
    "Roasted Chicken with Root Vegetables",
    "Beef Stew",
    "Chicken Curry with Rice",
    "Vegetable Curry with Naan",
    "Fish and Chips",
    "Chicken Caesar Salad",
    "Chicken Noodle Soup",
    "Tomato Basil Soup with Grilled Cheese",
    "French Onion Soup",
    "Chili with Cornbread",
    "Lasagna",
    "Enchiladas",
    "Tuna Casserole",
    "Chicken and Rice Casserole",
    "Baked Ziti",

    # --- Dinner - Generous budget ($16-$30) - Busy on some days (45 mins) ---
    "Steak with Roasted Asparagus and Potatoes",
    "Salmon with Lemon Herb Sauce",
    "Shrimp Linguine with White Wine Sauce",
    "Chicken Marsala with Mushrooms",
    "Beef Wellington with Red Wine Reduction (simplified)",
    "Lamb Shanks with Rosemary and Garlic",
    "Pork Tenderloin with Cranberry Sauce",
    "Chicken and Sausage Gumbo",
    "Seafood Cioppino (quick version)",
    "Chicken Piccata with Capers",
    "Beef Stroganoff with Egg Noodles",
    "Chicken and Broccoli Alfredo",
    "Shrimp and Chorizo Paella (small portion)",
    "Fish Tacos with Mango Salsa",
    "Chicken Fajitas with Guacamole and Sour Cream",
    "Beef Burritos with Sour Cream and Rice",
    "Lamb Curry with Naan Bread",
    "Vegetable Curry with Rice and Chutney",
    "Salmon with Dill Sauce",
    "Baked Cod with Lemon Butter and Green Beans",
    "Chicken and Spinach Salad with Vinaigrette",
    "Caesar Salad with Grilled Shrimp and Croutons",
    "Waldorf Salad with Chicken and Walnuts",
    "Broccoli Salad with Bacon, Cheddar, and Raisins",
    "Pasta Primavera with Parmesan and Garlic Bread",
    "Chicken Cacciatore with Polenta",
    "Beef Bourguignon with Crusty Bread (quick version)",
    "Chicken and Mushroom Casserole with Noodles",
    "Roast Duck with Orange Sauce and Wild Rice",
    "Prawn and Chorizo Pasta with Linguine and Herbs",

    # --- Dinner - No budget constraints ($31+) - No Constraints (Any duration) ---
    "Lobster Thermidor with Asparagus and Hollandaise Sauce",
    "Rack of Lamb with Rosemary Potatoes and Mint Sauce",
    "Filet Mignon with Béarnaise Sauce and Truffle Fries",
    "Pan-Seared Scallops with Lemon Risotto and White Wine Butter Sauce",
    "Braised Short Ribs with Creamy Polenta and Gremolata",
    "Seafood Bouillabaisse with Saffron Rouille and Sourdough Bread",
    "Duck Confit with Cherry Sauce and Wild Rice Pilaf",
    "Grilled Swordfish with Mediterranean Salsa and Couscous",
    "Veal Milanese with Arugula Salad and Lemon Vinaigrette",
    "Beef Tournedos Rossini with Foie Gras and Madeira Sauce",
    "Lobster Ravioli with Brown Butter Sauce and Crispy Sage",
    "Pan-Seared Chilean Sea Bass with Mango Salsa and Black Beans",
    "Crispy Skin Salmon with Beurre Blanc and Roasted Root Vegetables",
    "Seafood Linguine with White Wine Sauce and Garlic Bread",
    "Tuna Tataki Salad with Sesame Dressing and Avocado",
    "Grilled Octopus Salad with Lemon Vinaigrette and Kalamata Olives",
    "Lobster Bisque with Cognac and Sherry",
    "French Onion Soup with Gruyere Croutons and Baguette",
    "Steak and Blue Cheese Salad with Candied Pecans and Balsamic Glaze",
    "Pan-Seared Ahi Tuna with Wasabi Aioli and Seaweed Salad",
    "Lobster Ravioli with Brown Butter Sauce and Crispy Sage",
    "Crispy Duck Confit Salad with Fig Dressing and Goat Cheese",
    "Seafood Cioppino with Sourdough Bread and Garlic Toast",
    "Grilled Swordfish with Mediterranean Salsa and Couscous",
    "Veal Milanese with Arugula Salad and Lemon Vinaigrette",
    "Steak Frites with Béarnaise Sauce and Truffle Salt",
    "Seafood Paella with Saffron Aioli and Grilled Bread",
    "Grilled Lamb Chops with Mint Chimichurri and Roasted Vegetables",
    "Pan-Seared Ahi Tuna with Wasabi Aioli and Seaweed Salad",
    "Roasted Bone Marrow with Parsley Salad and Toasted Baguette"
],
    "Italian": [
        # Classic Pasta Dishes
        "Spaghetti alla Carbonara (with Eggs, Pecorino Romano, Guanciale)",
        "Pasta all'Amatriciana (with Tomato, Guanciale, Pecorino)",
        "Spaghetti al Ragù alla Bolognese (with Meat Sauce)",
        "Lasagne al Forno (Baked Lasagna)",
        "Fettuccine Alfredo (with Butter and Parmesan)",
        "Pasta alla Norma (with Eggplant, Tomato, Ricotta Salata)",
        "Penne all'Arrabbiata (with Spicy Tomato Sauce)",
        "Linguine alle Vongole (with Clams)",
        "Spaghetti alle Cozze (with Mussels)",
        "Pasta al Forno (Baked Pasta)",
        "Orecchiette alle Cime di Rapa (with Broccoli Rabe)",
        "Trofie al Pesto (with Pesto)",
        "Tagliatelle ai Funghi Porcini (with Porcini Mushrooms)",
        "Ravioli di Magro (with Spinach and Ricotta)",
        "Tortellini in Brodo (Pasta in Broth)",
        "Cappelletti in Brodo (Small Stuffed Pasta in Broth)",
        "Pappardelle al Cinghiale (with Wild Boar Ragù)",
        "Gnocchi alla Sorrentina (Baked Gnocchi with Tomato and Mozzarella)",
        "Gnocchi al Pesto (Gnocchi with Pesto)",
        "Risotto alla Carbonara",

        # Pizza & Breads
        "Pizza Margherita (Tomato, Mozzarella, Basil)",
        "Pizza Marinara (Tomato, Garlic, Oregano)",
        "Pizza Napoletana (Neapolitan Pizza)",
        "Pizza Quattro Stagioni (Four Seasons Pizza)",
        "Pizza Capricciosa (with Ham, Mushrooms, Artichokes)",
        "Focaccia Genovese (Genoese Flatbread)",
        "Focaccia Barese (Bari-style Focaccia)",
        "Schiacciata (Tuscan Flatbread)",
        "Piadina Romagnola (Romagna Flatbread)",
        "Pane di Altamura (Altamura Bread)",

        # Soups & Stews
        "Minestrone (Vegetable Soup)",
        "Ribollita (Tuscan Bread Soup)",
        "Zuppa di Pesce (Fish Soup)",
        "Pasta e Fagioli (Pasta and Bean Soup)",
        "Acquacotta (Tuscan Bread and Vegetable Soup)",
        "Stracciatella (Roman Egg Drop Soup)",

        # Meat & Poultry
        "Osso Buco alla Milanese (Braised Veal Shanks)",
        "Saltimbocca alla Romana (Veal with Prosciutto and Sage)",
        "Pollo alla Cacciatora (Hunter's Style Chicken)",
        "Arrosto Misto (Mixed Roast Meat)",
        "Bollito Misto (Mixed Boiled Meat)",
        "Cotoletta alla Milanese (Milanese Cutlet)",
        "Scaloppine al Limone (Veal with Lemon Sauce)",
        "Involtini (Stuffed Meat Rolls)",
        "Spezzatino (Meat Stew)",
        "Porchetta (Roasted Pork)",

        # Seafood
        "Cacciucco (Tuscan Seafood Stew)",
        "Brodetto di Pesce (Adriatic Fish Stew)",
        "Baccalà alla Livornese (Cod with Tomato Sauce)",
        "Sarde a Beccafico (Stuffed Sardines)",
        "Impepata di Cozze (Peppered Mussels)",
        "Alici Marinati (Marinated Anchovies)",
        "Fritto Misto di Mare (Fried Seafood)",
        "Risotto alla Pescatora (Seafood Risotto)",

        # Vegetables & Side Dishes
        "Caponata (Sicilian Eggplant Stew)",
        "Carciofi alla Romana (Roman-style Artichokes)",
        "Carciofi alla Giudia (Jewish-style Artichokes)",
        "Melanzane alla Parmigiana (Eggplant Parmesan)",
        "Peperonata (Stewed Peppers)",
        "Patate al Forno (Roasted Potatoes)",
        "Insalata Caprese (Tomato, Mozzarella, Basil)",
        "Pinzimonio (Raw Vegetables with Olive Oil)",
        "Fagiolini all'Uccelletto (Beans with Tomato Sauce)",
        "Cicoria Ripassata (Sautéed Chicory)",

        # Rice Dishes
        "Risotto alla Milanese (with Saffron)",
        "Risotto ai Funghi (Mushroom Risotto)",
        "Risotto alla Marinara (Seafood Risotto)",
        "Arancini Siciliani (Fried Rice Balls)",
        "Suppli (Roman Rice Croquettes)",

        # Cheese & Charcuterie
        "Tagliere di Salumi e Formaggi (Charcuterie and Cheese Board)",
        "Burrata con Pomodorini (Burrata with Cherry Tomatoes)",
        "Mozzarella di Bufala Campana (Buffalo Mozzarella)",
        "Pecorino Romano (Roman Sheep's Milk Cheese)",
        "Prosciutto di Parma (Parma Ham)",
        "Salame Milano (Milan Salami)",
        "Mortadella di Bologna (Bologna Mortadella)",
        "Finocchiona (Fennel Salami)",

        # Desserts
        "Tiramisu (Coffee-Flavored Dessert)",
        "Panna Cotta (Cooked Cream Dessert)",
        "Cannoli Siciliani (Fried Pastry Shells with Sweet Ricotta)",
        "Gelato Artigianale (Artisan Ice Cream)",
        "Semifreddo (Semi-Frozen Dessert)",
        "Zuccotto (Florentine Dome Cake)",
        "Pastiera Napoletana (Neapolitan Easter Pie)",
        "Ricciarelli (Sienese Almond Cookies)",
        "Panettone (Sweet Bread)",
        "Pandoro (Sweet Star-Shaped Bread)",
        "Torta della Nonna (Grandmother's Tart)",
        "Sfogliatella (Shell-Shaped Pastry)",
        "Zeppole (Fried Doughnuts)",

        # Regional Specialties
        "Cacio e Pepe (Roman Pasta with Cheese and Pepper)",
        "Carbonara di Mare (Seafood Carbonara)",
        "Sarde in Saor (Venetian Sweet and Sour Sardines)",
        "Pizzoccheri (Valtellina Buckwheat Pasta)",
        "Casunziei (Venetian Beet Ravioli)",
        "Polenta Taragna (Lombard Cornmeal Dish)",
        "Torta Pasqualina (Ligurian Savory Pie)",
        "Vincisgrassi (Marche Lasagna)",
        "Timpano (Sicilian Baked Pasta Drum)",
        "Pane Cunzato (Sicilian Seasoned Bread)",
        "Cianfotta (Campanian Vegetable Stew)",
        "Puttanesca (Neapolitan Pasta with Olives and Capers)"
    ],
    "Latin American / Mexican": [
    # Mexican
    "Tacos al Pastor (Marinated Pork Tacos)",
    "Mole Poblano (Chocolate Chili Sauce)",
    "Chiles en Nogada (Stuffed Poblano Peppers with Walnut Sauce)",
    "Pozole Rojo (Hominy and Meat Stew)",
    "Tamales (Steamed Corn Dough with Fillings)",
    "Enchiladas Rojas (Corn Tortillas with Red Sauce and Cheese)",
    "Chiles Rellenos (Stuffed and Fried Chili Peppers)",
    "Carnitas (Slow-Cooked Pulled Pork)",
    "Birria de Chivo (Spicy Goat Stew)",
    "Quesadillas (Cheese-Filled Tortillas)",
    "Sopes (Thick Corn Tortillas with Toppings)",
    "Huaraches (Oblong Corn Tortillas with Toppings)",
    "Tostadas (Crispy Tortillas with Toppings)",
    "Menudo (Tripe Soup)",
    "Pambazos (Bread Dipped in Chili Sauce with Fillings)",
    "Flan (Custard Dessert)",
    "Churros con Chocolate (Fried Dough with Chocolate Sauce)",
    "Pastel de Tres Leches (Three Milks Cake)",
    "Arroz con Leche (Rice Pudding)",
    "Chocolate Caliente (Hot Chocolate)",
    "Esquites (Street Corn Salad)",
    "Cochinita Pibil (Yucatan-Style Slow-Roasted Pork)",
    "Sopa de Tortilla (Tortilla Soup)",
    "Guacamole con Totopos (Avocado Dip with Tortilla Chips)",
    "Ceviche (Seafood Marinated in Citrus)",
    "Barbacoa (Pit-Barbecued Meat)",
    "Tlayudas (Oaxacan Large Tortillas with Toppings)",
    "Picaditas (Veracruz Small Tortillas with Toppings)",
    "Chalupas (Anahuac Small Thick Tortillas with Toppings)",
    "Chilaquiles (Tortilla Chips Cooked in Salsa)",
    "Rajas Poblanos (Poblano Pepper Strips in Cream Sauce)",
    "Caldo de Pollo (Chicken Soup)",
    "Elote (Mexican Street Corn)",
    "Champurrado (Thick Chocolate Atole)",

    # Peruvian
    "Ceviche Peruano (Peruvian Ceviche)",
    "Lomo Saltado (Stir-Fried Beef with Vegetables)",
    "Ají de Gallina (Creamy Chicken Stew)",
    "Papa a la Huancaína (Potatoes with Cheese Sauce)",
    "Rocoto Relleno (Stuffed Rocoto Peppers)",
    "Anticuchos (Grilled Beef Heart Skewers)",
    "Causa Rellena (Layered Potato Casserole)",
    "Seco de Cabrito (Goat Stew)",
    "Arroz con Mariscos (Rice with Seafood)",
    "Suspiro Limeño (Peruvian Caramel Custard)",
    "Pollo a la Brasa (Peruvian Roasted Chicken)",
    "Tiradito (Peruvian Sashimi)",
    "Tacu Tacu (Rice and Beans Dish)",
    "Picarones (Peruvian Sweet Potato Doughnuts)",

    # Colombian
    "Bandeja Paisa (Colombian Platter)",
    "Ajiaco (Colombian Chicken and Potato Soup)",
    "Empanadas Colombianas (Colombian Empanadas)",
    "Arepas (Cornmeal Cakes)",
    "Sancocho (Colombian Stew)",
    "Mondongo (Colombian Tripe Soup)",
    "Lechona (Colombian Roasted Pig)",
    "Tamales Tolimenses (Tolima-Style Tamales)",
    "Frijoles Antioqueños (Antioquian Beans)",
    "Mazamorra (Colombian Corn Pudding)",
    "Buñuelos (Colombian Cheese Fritters)",

    # Argentinian
    "Asado (Argentinian Barbecue)",
    "Empanadas Argentinas (Argentinian Empanadas)",
    "Locro (Argentinian Stew)",
    "Milanesa a la Napolitana (Argentinian Breaded Meat with Toppings)",
    "Pastel de Papa (Shepherd's Pie)",
    "Choripán (Chorizo Sandwich)",
    "Provoleta (Grilled Provolone Cheese)",
    "Alfajores (Argentinian Sandwich Cookies)",
    "Dulce de Leche (Caramelized Milk)",
    "Humita en Chala (Corn Tamales)",

    # Brazilian
    "Feijoada (Brazilian Black Bean Stew)",
    "Moqueca (Brazilian Fish Stew)",
    "Pão de Queijo (Brazilian Cheese Bread)",
    "Coxinha (Brazilian Chicken Croquettes)",
    "Pastel (Brazilian Fried Pastries)",
    "Escondidinho (Brazilian Shepherd's Pie)",
    "Acarajé (Brazilian Black-Eyed Pea Fritters)",
    "Brigadeiro (Brazilian Chocolate Truffles)",
    "Quindim (Brazilian Coconut Custard)",
    "Caipirinha (Brazilian Cocktail)",

    # Caribbean (with Latin American Influences)
    "Mofongo (Puerto Rican Mashed Plantains)",
    "Ropa Vieja (Cuban Shredded Beef)",
    "Moros y Cristianos (Cuban Rice and Beans)",
    "Arroz Congrí (Cuban Rice and Beans)",
    "Tostones (Fried Plantains)",
    "Pernil (Puerto Rican Roasted Pork Shoulder)",
    "Pasteles (Puerto Rican Root Vegetable Tamales)",
    "Coquito (Puerto Rican Coconut Drink)",
    "Flan de Coco (Caribbean Coconut Flan)",
    "Guanime (Puerto Rican Cornmeal Dumplings)",

    # Central American
    "Pupusas (Salvadoran Stuffed Flatbreads)",
    "Gallo Pinto (Costa Rican Rice and Beans)",
    "Casado (Costa Rican Lunch Plate)",
    "Rondon (Caribbean Coast Seafood Stew)",
    "Baleadas (Honduran Folded Tortillas)",
    "Enchiladas Guatemaltecas (Guatemalan Enchiladas)",
    "Fiambre (Guatemalan Salad)",
    "Chuchitos (Guatemalan Small Tamales)",
    "Platanos en Gloria (Nicaraguan Sweet Plantains)",
    "Nacatamales (Nicaraguan Tamales)"
],
    "Indian": [
        # North Indian
    "Butter Chicken (Murgh Makhani)",
    "Chicken Biryani (Fragrant Rice with Chicken)",
    "Rogan Josh (Aromatic Kashmiri Lamb Curry)",
    "Palak Paneer (Spinach and Cottage Cheese Curry)",
    "Chana Masala (Chickpea Curry)",
    "Dal Makhani (Black Lentil and Kidney Bean Curry)",
    "Tandoori Chicken (Yogurt Marinated Roasted Chicken)",
    "Aloo Gobi (Potato and Cauliflower Curry)",
    "Saag Paneer (Mustard Greens and Cottage Cheese Curry)",
    "Rajma Chawal (Kidney Bean Curry with Rice)",
    "Matar Paneer (Peas and Cottage Cheese Curry)",
    "Navratan Korma (Vegetable and Nut Curry)",
    "Malai Kofta (Vegetable and Paneer Dumplings in Cream Sauce)",
    "Chole Bhature (Chickpea Curry with Fried Bread)",
    "Paneer Tikka Masala (Cottage Cheese in Tomato-Based Gravy)",
    "Chicken Tikka Masala (Chicken in Tomato-Based Gravy)",
    "Lamb Korma (Creamy Lamb Curry)",
    "Dal Tadka (Tempered Lentil Curry)",
    "Baingan Bharta (Smoked Eggplant Mash)",
    "Sarson ka Saag (Mustard Greens Curry)",
    "Makki di Roti (Corn Flour Flatbread)",
    "Naan (Oven-Baked Flatbread)",
    "Roti (Whole Wheat Flatbread)",
    "Paratha (Stuffed Flatbread)",
    "Lassi (Yogurt-Based Drink)",
    "Gulab Jamun (Milk Solid Dumplings in Sugar Syrup)",
    "Kheer (Rice Pudding)",
    "Jalebi (Fried Wheat Flour Spirals in Syrup)",
    "Rasmalai (Cheese Patties in Sweet Milk)",
    "Gajar ka Halwa (Carrot Pudding)",

    # South Indian
    "Masala Dosa (Crispy Crepe with Potato Filling)",
    "Idli Sambhar (Steamed Rice Cakes with Lentil Soup)",
    "Vada Sambhar (Fried Lentil Doughnuts with Lentil Soup)",
    "Uttapam (Thick Rice and Lentil Pancake)",
    "Rasam (Spicy Tomato Soup)",
    "Sambar (Vegetable Lentil Stew)",
    "Avial (Mixed Vegetable Curry with Coconut)",
    "Chettinad Chicken (Spicy Chicken Curry)",
    "Meen Moilee (Fish Curry with Coconut Milk)",
    "Hyderabadi Biryani (Fragrant Rice with Meat)",
    "Upma (Semolina Porridge)",
    "Pongal (Rice and Lentil Dish)",
    "Appam with Stew (Fermented Rice Pancake with Stew)",
    "Idiyappam (Rice Noodle Cakes)",
    "Korma (Coconut-Based Curry)",
    "Payasam (Sweet Milk Pudding)",
    "Mysore Pak (Sweet Fudge)",
    "Rava Kesari (Semolina Dessert)",
    "Coconut Chutney (Coconut Dip)",
    "Sambar Powder (Spice Blend)",

    # East Indian
    "Macher Jhol (Fish Curry)",
    "Aloo Posto (Potato Curry with Poppy Seeds)",
    "Shukto (Mixed Vegetable Curry)",
    "Daal Puri (Lentil Stuffed Bread)",
    "Chingri Malai Curry (Prawn Curry with Coconut Milk)",
    "Kosha Mangsho (Mutton Curry)",
    "Luchi (Fried Flatbread)",
    "Sandesh (Sweet Cheese Dessert)",
    "Roshogolla (Sweet Cheese Balls in Syrup)",
    "Momos (Dumplings)",
    "Thukpa (Noodle Soup)",
    "Poha (Flattened Rice Dish)",
    "Sattu Paratha (Roasted Gram Flour Flatbread)",

    # West Indian
    "Pav Bhaji (Vegetable Mash with Buttered Bread Rolls)",
    "Vada Pav (Potato Fritter Sandwich)",
    "Misal Pav (Spicy Sprout Curry with Bread)",
    "Dhokla (Steamed Chickpea Flour Cakes)",
    "Thepla (Spiced Flatbread)",
    "Undhiyu (Mixed Vegetable Curry)",
    "Bhel Puri (Savory Snack with Puffed Rice and Vegetables)",
    "Pani Puri (Crispy Semolina Shells with Spiced Water)",
    "Ragda Pattice (Potato Patties with Chickpea Curry)",
    "Shrikhand (Sweet Yogurt Dessert)",
    "Puran Poli (Sweet Stuffed Flatbread)",
    "Batata Vada (Potato Fritters)",
    "Sabudana Khichdi (Tapioca Pearl Dish)",

    # Snacks & Street Food
    "Samosas (Spiced Potato and Pea Pastries)",
    "Pakoras (Vegetable Fritters)",
    "Dahi Puri (Crispy Shells with Yogurt)",
    "Sev Puri (Crispy Crackers with Toppings)",
    "Papdi Chaat (Crispy Wafers with Toppings)",
    "Aloo Tikki (Potato Patties)",
    "Chaat Masala (Spice Blend)",
    "Tandoori Paneer Tikka (Roasted Cottage Cheese)",
    "Chicken 65 (Spicy Fried Chicken)",
    "Seekh Kebab (Minced Meat Skewers)",
    "Hara Bhara Kebab (Spinach and Pea Patties)",
    "Onion Bhaji (Onion Fritters)",
    "Papadum (Thin Crispy Flatbread)",

    # Pickles & Chutneys
    "Mango Pickle (Aam ka Achar)",
    "Lime Pickle (Nimbu ka Achar)",
    "Mint Chutney (Pudina Chutney)",
    "Tamarind Chutney (Imli Chutney)",
    "Coriander Chutney (Dhania Chutney)",
    "Garlic Chutney (Lahsun Chutney)",
],
    "Japanese": [
    # Sushi & Sashimi
    "Nigiri Sushi (Vinegared Rice with Toppings)",
    "Sashimi (Thinly Sliced Raw Fish)",
    "Maki Sushi (Rolled Sushi)",
    "Uramaki Sushi (Inside-Out Rolls)",
    "Temaki Sushi (Hand-Rolled Sushi)",
    "Gunkan Maki (Battleship Rolls)",
    "Chirashi Sushi (Scattered Sushi)",
    "Inari Sushi (Fried Tofu Pockets)",

    # Noodles
    "Ramen (Wheat Noodles in Broth)",
    "Udon (Thick Wheat Noodles)",
    "Soba (Buckwheat Noodles)",
    "Yakitori Ramen",
    "Tempura Udon/Soba",
    "Kitsune Udon/Soba (with Fried Tofu)",
    "Tsukemen (Dipping Noodles)",
    "Yakisoba (Stir-Fried Noodles)",
    "Yaki Udon (Stir-Fried Udon)",
    "Somen (Thin Wheat Noodles)",
    "Hiyamugi (Thin Wheat Noodles)",
    "Champon (Nagasaki Noodle Dish)",

    # Rice Dishes
    "Donburi (Rice Bowl Dishes)",
    "Gyudon (Beef Bowl)",
    "Oyakodon (Chicken and Egg Bowl)",
    "Katsudon (Pork Cutlet Bowl)",
    "Tendon (Tempura Bowl)",
    "Unadon (Eel Bowl)",
    "Curry Rice (Japanese Curry with Rice)",
    "Omurice (Omelette Rice)",
    "Takikomi Gohan (Mixed Rice)",
    "Okayu (Rice Porridge)",

    # Meat & Poultry
    "Teriyaki Chicken (Grilled Chicken with Sweet Soy Glaze)",
    "Yakitori (Grilled Chicken Skewers)",
    "Tonkatsu (Deep-Fried Pork Cutlet)",
    "Chicken Nanban (Fried Chicken with Tartar Sauce)",
    "Shogayaki (Ginger Pork)",
    "Nikujaga (Meat and Potato Stew)",
    "Hamburg Steak (Japanese-style Hamburger)",
    "Karaage (Japanese Fried Chicken)",
    "Toriten (Tempura Chicken)",
    "Buta no Kakuni (Braised Pork Belly)",

    # Seafood
    "Tempura (Deep-Fried Seafood and Vegetables)",
    "Sushi (Vinegared Rice with Toppings)",
    "Sashimi (Thinly Sliced Raw Fish)",
    "Shabu-Shabu (Thinly Sliced Meat Cooked in Broth)",
    "Sukiyaki (Hot Pot with Thinly Sliced Beef and Vegetables)",
    "Oden (Hot Pot Dish)",
    "Sanma no Shioyaki (Grilled Pacific Saury)",
    "Saba no Misoni (Mackerel Cooked in Miso)",
    "Takoyaki (Octopus Balls)",
    "Ebi Chili (Shrimp Chili)",

    # Savory Dishes
    "Okonomiyaki (Savory Pancake)",
    "Chawanmushi (Savory Egg Custard)",
    "Gyoza (Pan-Fried Dumplings)",
    "Edamame (Steamed Soybeans)",
    "Agedashi Tofu (Fried Tofu in Broth)",
    "Nimono (Simmered Dishes)",
    "Sunomono (Vinegared Salad)",
    "Miso Soup (Soybean Paste Soup)",
    "Dashimaki Tamago (Rolled Omelette)",
    "Tsukemono (Pickled Vegetables)",

    # Bread & Sandwiches
    "Sandos (Japanese Sandwiches)",
    "Katsu Sando (Pork Cutlet Sandwich)",
    "Tamago Sando (Egg Sandwich)",
    "Yakisoba Pan (Noodle Sandwich)",
    "Anpan (Sweet Bean Bun)",
    "Shokupan (Japanese Milk Bread)",

    # Desserts
    "Mochi (Rice Cakes)",
    "Daifuku (Stuffed Mochi)",
    "Dorayaki (Sweet Red Bean Pancakes)",
    "Taiyaki (Fish-Shaped Cake with Filling)",
    "Anmitsu (Agar Jelly Dessert)",
    "Matcha Ice Cream (Green Tea Ice Cream)",
    "Kakigori (Shaved Ice)",
    "Zenzai (Sweet Red Bean Soup)",
    "Castella (Japanese Sponge Cake)",
    "Purin (Japanese Pudding)",

    # Regional Specialties
    "Hiroshima-style Okonomiyaki",
    "Osaka-style Okonomiyaki",
    "Hakata Ramen",
    "Sapporo Ramen",
    "Nagoya-style Hitsumabushi (Grilled Eel)",
    "Okinawa Soba",
    "Goya Champuru (Okinawan Stir-Fry)",
    "Monjayaki (Tokyo Savory Pancake)",
    "Fugu Sashimi (Pufferfish Sashimi)",
    "Onigiri Cha-zuke (Rice Balls in Tea)",
    "Nabe (Hot Pot Dishes)",
    "Yosenabe (Mixed Hot Pot)",
    "Kimchi Nabe (Korean-influenced Hot Pot)",
    "Chanko Nabe (Sumo Wrestler Hot Pot)",
    "Ishikari Nabe (Salmon Hot Pot)"
],
    "Chinese": [
    # Cantonese Cuisine
    "Cantonese Char Siu (Barbecue Pork)",
    "Cantonese Dim Sum (Steamed and Fried Small Dishes)",
    "Har Gow (Shrimp Dumplings)",
    "Siu Mai (Pork and Shrimp Dumplings)",
    "Cheung Fun (Rice Noodle Rolls)",
    "Congee (Rice Porridge)",
    "Wonton Noodle Soup (Dumplings in Broth)",
    "Roast Duck (Cantonese Style)",
    "Roast Pork Belly (Siu Yuk)",
    "Clay Pot Rice (煲仔饭)",
    "Steamed Fish with Ginger and Scallions",
    "Chow Mein (Stir-Fried Noodles)",
    "Fried Rice (Cantonese Style)",
    "Lo Mein (Stir-Fried Noodles with Sauce)",
    "Cantonese Egg Tarts (Custard Tarts)",
    "Mango Pudding (Sweet Mango Dessert)",
    "Sweet and Sour Pork (Pork in Tangy Sauce)",
    "Beef Chow Fun (Stir-Fried Rice Noodles with Beef)",
    "Congee with Preserved Egg and Pork",
    "Steamed Spare Ribs with Black Bean Sauce",

    # Sichuan Cuisine
    "Mapo Tofu (Silken Tofu in Spicy Bean Sauce)",
    "Kung Pao Chicken (Spicy Stir-Fried Chicken with Peanuts)",
    "Sichuan Dan Dan Noodles (Spicy Noodle Dish)",
    "Twice Cooked Pork (回锅肉)",
    "Fish-Fragrant Eggplant (Yu Xiang Qie Zi)",
    "Sichuan Hot Pot (Spicy Broth with Ingredients)",
    "Mala Chicken (Spicy and Numbing Chicken)",
    "Shui Zhu Yu (Fish in Chili Oil)",
    "Dry Pot (干锅)",
    "Spicy Boiled Beef (水煮牛肉)",
    "Sichuan Cold Noodles (凉面)",
    "Fuqi Feipian (Spicy Beef Offal)",
    "La Zi Ji (Spicy Chicken Cubes)",
    "Chongqing Chicken (辣子鸡)",
    "Gong Bao Chicken (宫保鸡丁)",
    "Mao Xue Wang (毛血旺)",
    "Sichuan Pickled Vegetables (泡菜)",
    "Sichuan Hotpot (火锅)",
    "Sichuan Dumplings (钟水饺)",
    "Sichuan Liangfen (凉粉)",

    # Peking Cuisine
    "Peking Duck (Crispy Roasted Duck)",
    "Jiaozi (Boiled Dumplings)",
    "Baozi (Steamed Buns with Fillings)",
    "Zha Jiang Mian (Noodles with Soybean Paste Sauce)",
    "Jing Jiang Rou Si (Shredded Pork with Sweet Bean Sauce)",
    "Suan Cai Yu (Fish with Pickled Cabbage)",
    "Peking Roast Duck (北京烤鸭)",
    "Peking Style Noodles (老北京炸酱面)",
    "Peking Style Dumplings (老北京饺子)",
    "Peking Style Hot Pot (老北京涮羊肉)",

    # Shanghai Cuisine
    "Xiao Long Bao (Steamed Soup Dumplings)",
    "Shanghai Fried Noodles (上海炒面)",
    "Shanghai Style Spring Rolls (上海春卷)",
    "Lion's Head Meatballs (狮子头)",
    "Braised Pork Belly (Hong Shao Rou)",
    "Sweet and Sour Spare Ribs (糖醋排骨)",
    "Shanghai Bok Choy (上海青)",
    "Shanghai Style Dumplings (生煎包)",
    "Shanghai Rice Cakes (上海炒年糕)",
    "Shanghai Style Braised Fish (红烧鱼)",

    # Fujian Cuisine
    "Buddha Jumps Over the Wall (佛跳墙)",
    "Oyster Omelette (蚵仔煎)",
    "Fujian Fried Rice (福建炒饭)",
    "Fujian Noodles (福建面)",
    "Fujian Style Dumplings (扁肉)",
    "Fujian Style Fish Balls (鱼丸)",
    "Fujian Style Peanut Soup (花生汤)",

    # Xinjiang Cuisine
    "Big Plate Chicken (大盘鸡)",
    "Hand-Pulled Noodles (拉条子)",
    "Lamb Skewers (羊肉串)",
    "Pilaf (抓饭)",
    "Dapanji (大盘鸡)",
    "Xinjiang Style Noodles (拌面)",
    "Xinjiang Style Bread (馕)",

    # Desserts & Snacks
    "Mooncakes (Sweet Pastries for Mid-Autumn Festival)",
    "Red Bean Buns (Steamed Buns with Sweet Red Bean Paste)",
    "Tang Yuan (Sweet Rice Balls)",
    "Glutinous Rice Balls (汤圆)",
    "Almond Cookies (Crisp Almond Flavored Cookies)",
    "Sesame Balls (煎堆)",
    "Pineapple Buns (菠萝包)",
    "Egg Tarts (蛋挞)",
    "Sweet Rice Cake (年糕)",
    "Eight Treasure Rice (八宝饭)",
    "Candied Hawthorns (糖葫芦)",
    "Bing Tang Hulu (糖葫芦)",
    "Tangyuan with Sesame Filling (芝麻汤圆)",
    "Tangyuan with Peanut Filling (花生汤圆)",
    "Tangyuan with Red Bean Filling (豆沙汤圆)",

    # Other Dishes
    "Chow Mein (炒面)",
    "Spring Rolls (春卷)",
    "General Tso's Chicken (左宗棠鸡)",
    "Egg Drop Soup (蛋花汤)",
    "Wonton Soup (云吞汤)",
    "Hot and Sour Soup (酸辣汤)",
    "Dumplings (饺子)",
    "Fried Rice (炒饭)",
    "Sweet and Sour Ribs (糖醋里脊)",
    "Braised Pork Knuckles (红烧猪蹄)",
    "Stir-Fried Green Beans (干煸四季豆)",
    "Stir-Fried Cabbage (醋溜白菜)",
    "Spicy Cucumber Salad (拍黄瓜)",
    "Cold Sesame Noodles (麻酱凉面)",
    "Lion's Head (狮子头)"
],
    "Thai": [
    # Noodles
    "Pad Thai (ผัดไทย) - Stir-Fried Rice Noodles with Shrimp, Tofu, Peanuts",
    "Pad See Ew (ผัดซีอิ๊ว) - Stir-Fried Wide Rice Noodles with Soy Sauce",
    "Pad Kee Mao (ผัดขี้เมา) - Drunken Noodles",
    "Khao Soi (ข้าวซอย) - Northern Thai Curry Noodle Soup",
    "Rad Na (ราดหน้า) - Noodles with Gravy",
    "Guay Teow Kua Gai (ก๋วยเตี๋ยวคั่วไก่) - Stir-Fried Noodles with Chicken",
    "Ba Mee Kiew (บะหมี่เกี๊ยว) - Egg Noodles with Wonton",
    "Sen Lek Tom Yum (เส้นเล็กต้มยำ) - Rice Noodles in Tom Yum Soup",
    "Sen Yai Pad See Ew (เส้นใหญ่ผัดซีอิ๊ว) - Wide Rice Noodles Pad See Ew",
    "Sen Mee Pad Thai (เส้นหมี่ผัดไทย) - Thin Rice Noodles Pad Thai",

    # Rice Dishes
    "Khao Pad (ข้าวผัด) - Fried Rice",
    "Khao Pad Sapparot (ข้าวผัดสับปะรด) - Pineapple Fried Rice",
    "Khao Pad Krapow (ข้าวผัดกะเพรา) - Basil Fried Rice",
    "Khao Man Gai (ข้าวมันไก่) - Chicken Rice",
    "Khao Mok Gai (ข้าวหมกไก่) - Steamed Chicken and Rice in Banana Leaf",
    "Khao Chae (ข้าวแช่) - Rice Soaked in Jasmine Water with Condiments",
    "Khao Niao Mamuang (ข้าวเหนียวมะม่วง) - Mango Sticky Rice",
    "Khao Niao Sangkhaya (ข้าวเหนียวสังขยา) - Sticky Rice with Custard",
    "Khao Tom (ข้าวต้ม) - Rice Soup",
    "Khao Pad Poo (ข้าวผัดปู) - Crab Fried Rice",

    # Curries
    "Green Curry with Chicken (Gaeng Keow Wan Gai) (แกงเขียวหวานไก่)",
    "Red Curry (Gaeng Daeng) (แกงแดง)",
    "Massaman Curry with Beef (Gaeng Massaman Neua) (แกงมัสมั่นเนื้อ)",
    "Panaeng Curry (แกงพะแนง)",
    "Yellow Curry (Gaeng Kari) (แกงกะหรี่)",
    "Jungle Curry (Gaeng Pa) (แกงป่า)",
    "Sour Curry (Gaeng Som) (แกงส้ม)",
    "Hung Lay Curry (แกงฮังเล) - Northern Thai Pork Curry",
    "Gaeng Keow Wan Pla (แกงเขียวหวานปลา) - Green Curry with Fish",
    "Gaeng Daeng Ped Yang (แกงแดงเป็ดย่าง) - Red Curry with Roasted Duck",

    # Soups
    "Tom Yum Goong (ต้มยำกุ้ง) - Spicy Shrimp Soup",
    "Tom Kha Gai (ต้มข่าไก่) - Coconut Milk Soup with Chicken",
    "Tom Saap (ต้มแซ่บ) - Spicy Isan Soup",
    "Gaeng Jued Woon Sen (แกงจืดวุ้นเส้น) - Clear Noodle Soup",
    "Tom Yum Pla (ต้มยำปลา) - Spicy Fish Soup",
    "Tom Kha Pla (ต้มข่าปลา) - Coconut Milk Soup with Fish",
    "Tom Yum Talay (ต้มยำทะเล) - Spicy Seafood Soup",
    "Tom Kha Hed (ต้มข่าเห็ด) - Coconut Milk Soup with Mushrooms",
    "Tom Yum Kung Nam Sai (ต้มยำกุ้งน้ำใส) - Clear Tom Yum Soup",
    "Tom Yum Kung Nam Khon (ต้มยำกุ้งน้ำข้น) - Creamy Tom Yum Soup",

    # Salads
    "Som Tam (ส้มตำ) - Spicy Green Papaya Salad",
    "Larb (ลาบ) - Minced Meat Salad",
    "Yam Woon Sen (ยำวุ้นเส้น) - Glass Noodle Salad",
    "Yam Talay (ยำทะเล) - Seafood Salad",
    "Yam Pla Duk Foo (ยำปลาดุกฟู) - Crispy Catfish Salad",
    "Yam Moo Yor (ยำหมูยอ) - Vietnamese Sausage Salad",
    "Som Tum Pla Ra (ส้มตำปลาร้า) - Papaya Salad with Fermented Fish Sauce",
    "Larb Gai (ลาบไก่) - Minced Chicken Salad",
    "Yam Ma Muang (ยำมะม่วง) - Mango Salad",
    "Yam Nuea Yang (ยำเนื้อย่าง) - Grilled Beef Salad",

    # Appetizers
    "Satay (สะเต๊ะ) - Grilled Skewers with Peanut Sauce",
    "Tod Mun Pla (ทอดมันปลา) - Fish Cakes",
    "Spring Rolls (ปอเปี๊ยะ)",
    "Fried Wonton (เกี๊ยวทอด)",
    "Miang Kham (เมี่ยงคำ) - Leaf-Wrapped Bites",
    "Hoy Tod (หอยทอด) - Crispy Mussel Pancake",
    "Poh Pia Sod (เปาะเปี๊ยะสด) - Fresh Spring Rolls",
    "Peek Gai Tod (ปีกไก่ทอด) - Fried Chicken Wings",
    "Sai Krok Isaan (ไส้กรอกอีสาน) - Northeastern Thai Sausage",
    "Pla Meuk Yang (ปลาหมึกย่าง) - Grilled Squid",

    # Desserts
    "Mango Sticky Rice (ข้าวเหนียวมะม่วง) - Khao Niao Mamuang",
    "Tub Tim Grob (ทับทิมกรอบ) - Water Chestnuts in Coconut Milk",
    "Khanom Buang (ขนมเบื้อง) - Crispy Pancakes with Sweet and Savory Fillings",
    "Khao Niao Dam (ข้าวเหนียวดำ) - Black Sticky Rice",
    "Khanom Krok (ขนมครก) - Coconut Rice Pancakes",
    "Bua Loy (บัวลอย) - Rice Balls in Coconut Milk",
    "Lod Chong Nam Kathi (ลอดช่องน้ำกะทิ) - Pandan Jelly in Coconut Milk",
    "Ruam Mit (รวมมิตร) - Mixed Desserts in Coconut Milk",
    "Khanom Tuay (ขนมถ้วย) - Coconut Cream Dessert",
    "Fak Thong Gaeng Buat (ฟักทองแกงบวด) - Pumpkin in Coconut Milk",

    # Regional Specialties
    "Gaeng Hang Lei (แกงฮังเล) - Northern Thai Pork Curry",
    "Sai Oua (ไส้อั่ว) - Northern Thai Sausage",
    "Nam Prik Ong (น้ำพริกอ่อง) - Northern Thai Pork and Tomato Dip",
    "Nam Prik Noom (น้ำพริกหนุ่ม) - Northern Thai Roasted Chili Dip",
    "Kaeng Tai Pla (แกงไตปลา) - Southern Thai Fish Kidney Curry",
    "Kua Kling (คั่วกลิ้ง) - Southern Thai Dry Curry",
    "Massaman Curry with Chicken (แกงมัสมั่นไก่)",
    "Tom Yum Goong Nam Khon (ต้มยำกุ้งน้ำข้น) - Creamy Tom Yum Soup",
    "Gaeng Keow Wan Talay (แกงเขียวหวานทะเล) - Green Curry with Seafood",
    "Pad Prik King (ผัดพริกขิง) - Stir-Fried Green Beans with Curry Paste"
],
    "Mediterranean": [
    # Greek
    "Moussaka (Μουσακάς) - Eggplant and Meat Casserole",
    "Souvlaki (Σουβλάκι) - Grilled Meat Skewers",
    "Gyros (Γύρος) - Meat Cooked on a Vertical Rotisserie",
    "Dolmades (Ντολμάδες) - Stuffed Grape Leaves",
    "Spanakopita (Σπανακόπιτα) - Spinach and Feta Pie",
    "Pastitsio (Παστίτσιο) - Baked Pasta with Meat Sauce and Béchamel",
    "Gemista (Γεμιστά) - Stuffed Vegetables (Tomatoes, Peppers)",
    "Kleftiko (Κλέφτικο) - Slow-Baked Lamb",
    "Stifado (Στιφάδο) - Beef Stew with Onions",
    "Fasolada (Φασολάδα) - Greek Bean Soup",
    "Avgolemono (Αυγολέμονο) - Lemon and Egg Soup",
    "Tzatziki (Τζατζίκι) - Yogurt and Cucumber Dip",
    "Taramasalata (Ταραμοσαλάτα) - Fish Roe Dip",
    "Horiatiki Salata (Χωριάτικη Σαλάτα) - Greek Village Salad",
    "Keftedes (Κεφτέδες) - Greek Meatballs",
    "Loukoumades (Λουκουμάδες) - Honey-Dipped Doughnuts",
    "Baklava (Μπακλαβάς) - Sweet Pastry with Nuts and Syrup",
    "Galaktoboureko (Γαλακτομπούρεκο) - Custard Pie with Phyllo",
    "Kataifi (Καταΐφι) - Shredded Phyllo Pastry with Nuts and Syrup",
    "Saganaki (Σαγανάκι) - Fried Cheese",

    # Italian
    "Pasta alla Carbonara (with Eggs, Pecorino Romano, Guanciale)",
    "Lasagna alla Bolognese (with Ragù and Béchamel)",
    "Fettuccine Alfredo (with Butter and Parmesan)",
    "Spaghetti al Ragù alla Bolognese (with Meat Sauce)",
    "Penne all'Arrabbiata (with Spicy Tomato Sauce)",
    "Linguine alle Vongole (with Clams)",
    "Risotto alla Milanese (with Saffron)",
    "Gnocchi alla Sorrentina (Baked Gnocchi with Tomato and Mozzarella)",
    "Pizza Margherita (Tomato, Mozzarella, Basil)",
    "Osso Buco alla Milanese (Braised Veal Shanks)",
    "Saltimbocca alla Romana (Veal with Prosciutto and Sage)",
    "Minestrone (Vegetable Soup)",
    "Bruschetta al Pomodoro (with Tomatoes and Garlic)",
    "Caprese Salad (Tomato, Mozzarella, Basil)",
    "Pesto alla Genovese (Basil Pesto)",
    "Tiramisu (Coffee-Flavored Dessert)",
    "Panna Cotta (Cooked Cream Dessert)",
    "Cannoli Siciliani (Fried Pastry Shells with Sweet Ricotta)",
    "Arancini Siciliani (Fried Rice Balls)",
    "Focaccia (Flatbread)",

    # Spanish
    "Paella Valenciana (Rice Dish with Seafood and Meat)",
    "Gazpacho (Cold Tomato Soup)",
    "Tortilla Española (Spanish Potato and Egg Omelette)",
    "Tapas (Various Small Savory Dishes)",
    "Gambas al Ajillo (Garlic Shrimp)",
    "Patatas Bravas (Spicy Potatoes)",
    "Pulpo a la Gallega (Galician-Style Octopus)",
    "Fabada Asturiana (Asturian Bean Stew)",
    "Cocido Madrileño (Madrid-Style Chickpea Stew)",
    "Pisto (Spanish Vegetable Stew)",
    "Salmorejo (Thick Cold Tomato Soup)",
    "Churros con Chocolate (Fried Dough with Chocolate Sauce)",
    "Crema Catalana (Catalan Custard Dessert)",
    "Tarta de Santiago (Almond Cake from Santiago)",
    "Sangria (Spanish Wine Punch)",
    "Albondigas (Spanish Meatballs)",
    "Calamares a la Romana (Fried Squid)",
    "Croquetas (Spanish Croquettes)",
    "Empanadas (Spanish Empanadas)",
    "Flan (Spanish Custard Dessert)",

    # Turkish
    "Kebab (Various Grilled Meat Dishes)",
    "Şiş Kebap (Shish Kebab)",
    "Döner Kebap (Meat Cooked on a Vertical Rotisserie)",
    "Köfte (Meatballs or Patties)",
    "Dolma (Stuffed Vegetables or Leaves)",
    "Mantı (Turkish Dumplings)",
    "İskender Kebap (Meat with Tomato Sauce and Yogurt)",
    "Lahmacun (Turkish Pizza)",
    "Pide (Turkish Flatbread with Toppings)",
    "Meze (Various Small Dishes Served as Appetizers)",
    "Hummus (Chickpea Dip)",
    "Baba Ghanoush (Roasted Eggplant Dip)",
    "Tabbouleh (Parsley, Mint, Bulgur Salad)",
    "Baklava (Sweet Pastry with Nuts and Syrup)",
    "Kunefe (Sweet Cheese Pastry Soaked in Syrup)",
    "Sarma (Stuffed Cabbage Rolls)",
    "Imam Bayildi (Stuffed Eggplant)",
    "Mercimek Köftesi (Lentil Patties)",
    "Ezme Salata (Spicy Tomato Salad)",
    "Sütlaç (Rice Pudding)",

    # Levantine
    "Falafel (Fried Chickpea Balls)",
    "Shawarma (Grilled Meat in Pita)",
    "Kibbeh (Minced Meat and Bulgur Shells)",
    "Mujadara (Lentils and Rice with Fried Onions)",
    "Fattoush (Levantine Bread Salad)",
    "Ful Medames (Stewed Fava Beans)",
    "Shakshuka (Eggs Poached in Tomato Sauce)",
    "Maqluba (Upside-Down Rice and Meat Dish)",
    "Labneh (Strained Yogurt)",
    "Manakish (Levantine Flatbread with Toppings)",
    "Tabbouleh (Parsley, Mint, Bulgur Salad)",
    "Hummus (Chickpea Dip)",
    "Baba Ghanoush (Roasted Eggplant Dip)",
    "Knafeh (Sweet Cheese Pastry Soaked in Syrup)",
    "Kibbeh Nayeh (Raw Kibbeh)",
    "Fatteh (Layered Dish with Bread, Chickpeas, and Yogurt)",
    "Muhammara (Roasted Red Pepper Dip)",
    "Za'atar Bread (Flatbread with Sesame and Thyme)",
    "Halva (Sweet Confectionery)",
    "Arak (Levantine Distilled Alcoholic Drink - often enjoyed with Meze)",

    # North African
    "Tagine (Slow-Cooked Stew)",
    "Couscous (Steamed Semolina Dish)",
    "Pastilla (Moroccan Sweet and Savory Pie)",
    "Harira (Moroccan Tomato and Lentil Soup)",
    "Brik (Tunisian Thin Pastry with Filling)",
    "Mechoui (Roasted Lamb or Mutton)",
    "Rfissa (Moroccan Chicken and Lentil Dish)",
    "Chorba (North African Soup)",
    "Makroudh (Algerian Semolina Cookies)",
    "Tajine Mrouzia (Moroccan Sweet and Savory Tagine)",
    "Couscous Tfaya (Moroccan Sweet and Savory Couscous)",
    "Bastilla (Moroccan Savory Pie)",
    "Tagine Kefta (Moroccan Meatball Tagine)",
    "Bissara (Moroccan Bean Soup)",
    "Zaalouk (Moroccan Eggplant Dip)",
    "Merguez Tagine (North African Sausage Tagine)",
    "Pastilla au Pigeon (Moroccan Pigeon Pie)",
    "Harira Soup (Moroccan Lentil Soup)",
    "Briouats (Moroccan Stuffed Pastries)",
    "Baghrir (Moroccan Pancakes)"
],
    "Korean": [
    # Main Courses (Meat & Seafood)
    "Bulgogi (불고기) - Marinated Grilled Beef",
    "Galbi (갈비) - Marinated Beef Short Ribs",
    "Samgyeopsal (삼겹살) - Grilled Pork Belly",
    "Dakgalbi (닭갈비) - Spicy Stir-Fried Chicken",
    "Jeyuk Bokkeum (제육볶음) - Spicy Stir-Fried Pork",
    "Galbi Jjim (갈비찜) - Braised Beef Short Ribs",
    "Andong Jjimdak (안동찜닭) - Braised Chicken with Vegetables",
    "Haemul Jjim (해물찜) - Braised Seafood",
    "Agujjim (아귀찜) - Braised Monkfish",
    "Maeuntang (매운탕) - Spicy Fish Stew",
    "Hoe (회) - Raw Fish",
    "Sannakji (산낙지) - Live Octopus",
    "Jangeo Gui (장어구이) - Grilled Eel",
    "Godeungeo Jorim (고등어조림) - Braised Mackerel",
    "Ojingeo Bokkeum (오징어볶음) - Spicy Stir-Fried Squid",
    "Bulgogi Jeongol (불고기전골) - Bulgogi Hot Pot",
    "Dak Bulgogi (닭불고기) - Grilled Marinated Chicken",
    "Tteokgalbi (떡갈비) - Grilled Short Rib Patties",
    "Bossam (보쌈) - Boiled Pork Wraps",
    "Gamjatang (감자탕) - Spicy Pork Bone Stew",

    # Main Courses (Vegetarian)
    "Bibimbap (비빔밥) - Mixed Rice with Meat and Vegetables",
    "Dolsot Bibimbap (돌솥 비빔밥) - Hot Stone Pot Bibimbap",
    "Japchae (잡채) - Glass Noodles with Vegetables and Meat",
    "Tteokbokki (떡볶이) - Spicy Rice Cakes",
    "Rabokki (라볶이) - Tteokbokki with Ramen",
    "Sundubu Jjigae (순두부찌개) - Soft Tofu Stew",
    "Doenjang Jjigae (된장찌개) - Soybean Paste Stew",
    "Kimchi Jjigae (김치찌개) - Kimchi Stew",
    "Kongbiji Jjigae (콩비지찌개) - Soybean Pulp Stew",
    "Bibim Guksu (비빔국수) - Spicy Mixed Noodles",
    "Jjajangmyeon (짜장면) - Black Bean Noodles",
    "Naengmyeon (냉면) - Cold Buckwheat Noodles",
    "Kalguksu (칼국수) - Knife-Cut Noodles",
    "Janchi Guksu (잔치국수) - Feast Noodles",
    "Kong Guksu (콩국수) - Cold Soybean Noodle Soup",
    "Kimchi Fried Rice (김치볶음밥) - Kimchi Bokkeumbap",
    "Gimbap (김밥) - Seaweed Rice Rolls",
    "Yubu Gimbap (유부김밥) - Fried Tofu Skin Gimbap",
    "Bibim Naengmyeon (비빔냉면) - Spicy Cold Buckwheat Noodles",
    "Ramyeon (라면) - Korean Ramen",

    # Appetizers & Side Dishes
    "Kimchi (김치) - Fermented Cabbage",
    "Pajeon (파전) - Scallion Pancake",
    "Haemul Pajeon (해물파전) - Seafood Pancake",
    "Kimchi Pajeon (김치파전) - Kimchi Pancake",
    "Goguma Mattang (고구마 맛탕) - Candied Sweet Potatoes",
    "Tteok Kkochi (떡꼬치) - Skewered Rice Cakes",
    "Odeng Tang (어묵탕) - Fish Cake Soup",
    "Gyeran Jjim (계란찜) - Steamed Eggs",
    "Hobakjeon (호박전) - Zucchini Pancakes",
    "Dubu Kimchi (두부김치) - Tofu with Kimchi",
    "Kongnamul Muchim (콩나물무침) - Seasoned Soybean Sprouts",
    "Sigeumchi Namul (시금치나물) - Seasoned Spinach",
    "Musaengchae (무생채) - Spicy Radish Salad",
    "Oi Sobagi (오이소박이) - Stuffed Cucumber Kimchi",
    "Gyeran Mari (계란말이) - Rolled Omelette",
    "Japchae Bap (잡채밥) - Japchae with Rice",
    "Yachae Jeon (야채전) - Vegetable Pancakes",
    "Gamja Jorim (감자조림) - Braised Potatoes",
    "Miyeok Guk (미역국) - Seaweed Soup",
    "Yukgaejang (육개장) - Spicy Beef Soup",

    # Desserts & Snacks
    "Bingsu (빙수) - Shaved Ice Dessert",
    "Patbingsu (팥빙수) - Shaved Ice with Red Beans",
    "Hotteok (호떡) - Sweet Pancakes",
    "Hoddeok (호떡) - Sweet Filled Pancakes",
    "Yakgwa (약과) - Honey Cookies",
    "Yaksik (약식) - Sweet Rice with Nuts and Jujubes",
    "Gangjeong (강정) - Fried Rice Puffs",
    "Dasik (다식) - Tea Cookies",
    "Sujeonggwa (수정과) - Cinnamon Ginger Drink",
    "Sikhye (식혜) - Sweet Rice Drink",
    "Tteok (떡) - Rice Cakes",
    "Injeolmi (인절미) - Rice Cakes with Soybean Powder",
    "Songpyeon (송편) - Half-Moon Rice Cakes",
    "Jeungpyeon (증편) - Steamed Rice Cakes",
    "Ggul Tteok (꿀떡) - Honey Rice Cakes",
    "Bungeoppang (붕어빵) - Fish-Shaped Pastries",
    "Gyeranppang (계란빵) - Egg Bread",
    "Hwangnamppang (황남빵) - Red Bean Pastries",
    "Chalboribbang (찰보리빵) - Barley Bread",
    "Mandu Guk (만두국) - Dumpling Soup"
],
    "Vietnamese": [
    # Noodles
    "Pho Bo (Phở Bò) - Beef Noodle Soup",
    "Pho Ga (Phở Gà) - Chicken Noodle Soup",
    "Bun Cha (Bún Chả) - Grilled Pork with Vermicelli Noodles",
    "Bun Bo Hue (Bún Bò Huế) - Spicy Beef Noodle Soup",
    "Bun Rieu (Bún Riêu) - Tomato-Based Crab Noodle Soup",
    "Cao Lau (Cao Lầu) - Hoi An Noodles with Pork and Greens",
    "Mi Quang (Mì Quảng) - Turmeric Noodles with Meat and Herbs",
    "Bun Thit Nuong (Bún Thịt Nướng) - Grilled Pork with Vermicelli Noodles",
    "Bun Mang Vit (Bún Măng Vịt) - Duck and Bamboo Shoot Noodle Soup",
    "Banh Canh (Bánh Canh) - Thick Noodle Soup",
    "Hu Tieu (Hủ Tiếu) - Pork and Seafood Noodle Soup",
    "My Quang (Mỳ Quảng) - Turmeric Noodles",
    "Bun Ca (Bún Cá) - Fish Noodle Soup",
    "Bun Moc (Bún Mọc) - Pork Ball Noodle Soup",
    "Banh Da Cua (Bánh Đa Cua) - Crab Noodle Soup",
    "Mien Ga (Miến Gà) - Glass Noodle Soup with Chicken",
    "Mien Xao Cua (Miến Xào Cua) - Stir-Fried Glass Noodles with Crab",
    "Banh Hoi Thit Nuong (Bánh Hỏi Thịt Nướng) - Fine Vermicelli Noodles with Grilled Pork",
    "Bun Thang (Bún Thang) - Hanoi Noodle Soup",
    "Bun Moc Chao (Bún Mọc Cháo) - Pork Ball Noodle Soup",

    # Rice Dishes
    "Com Tam (Cơm Tấm) - Broken Rice with Grilled Pork",
    "Com Ga (Cơm Gà) - Chicken Rice",
    "Com Suon Nuong (Cơm Sườn Nướng) - Grilled Pork Chop Rice",
    "Com Chien Duong Chau (Cơm Chiên Dương Châu) - Yangzhou Fried Rice",
    "Com Nieu (Cơm Niêu) - Clay Pot Rice",
    "Xoi Ga (Xôi Gà) - Sticky Rice with Chicken",
    "Xoi Xeo (Xôi Xéo) - Sticky Rice with Mung Bean and Fried Onion",
    "Com Chay (Cơm Cháy) - Crispy Rice",
    "Com Lam (Cơm Lam) - Rice Cooked in Bamboo Tubes",
    "Com Hen (Cơm Hến) - Clam Rice",

    # Sandwiches & Rolls
    "Banh Mi (Bánh Mì) - Vietnamese Sandwich",
    "Goi Cuon (Gỏi Cuốn) - Fresh Spring Rolls",
    "Banh Cuon (Bánh Cuốn) - Steamed Rice Rolls",
    "Banh Trang Nuong (Bánh Tráng Nướng) - Grilled Rice Paper",
    "Banh Xeo (Bánh Xèo) - Crispy Savory Crepes",
    "Banh Khot (Bánh Khọt) - Mini Savory Pancakes",
    "Banh Trang Tron (Bánh Tráng Trộn) - Mixed Rice Paper Salad",
    "Nem Nuong Cuon (Nem Nướng Cuốn) - Grilled Pork Sausage Rolls",
    "Bo La Lot (Bò Lá Lốt) - Grilled Beef in Betel Leaf Rolls",
    "Cha Gio (Chả Giò) - Fried Spring Rolls",

    # Soups & Stews
    "Canh Chua (Canh Chua) - Sour Fish Soup",
    "Canh Ga La Giang (Canh Gà Lá Giang) - Chicken Sour Soup",
    "Canh Bi Dao (Canh Bí Đao) - Winter Melon Soup",
    "Canh Bun (Canh Bún) - Thick Noodle Soup with Crab Paste",
    "Lau (Lẩu) - Hot Pot",
    "Lau Ca Keo (Lẩu Cá Kèo) - Dwarf Goby Hot Pot",
    "Lau Mam (Lẩu Mắm) - Fermented Fish Hot Pot",
    "Bo Kho (Bò Kho) - Beef Stew",
    "Ca Kho To (Cá Kho Tộ) - Braised Fish in Clay Pot",
    "Thit Kho Trung (Thịt Kho Trứng) - Braised Pork with Eggs",

    # Salads & Appetizers
    "Goi Ga (Gỏi Gà) - Chicken Salad",
    "Goi Du Du (Gỏi Đu Đủ) - Green Papaya Salad",
    "Goi Cuon Tom Thit (Gỏi Cuốn Tôm Thịt) - Shrimp and Pork Spring Rolls",
    "Goi Ngo Sen (Gỏi Ngó Sen) - Lotus Stem Salad",
    "Nom Bo Kho (Nộm Bò Khô) - Beef Jerky Salad",
    "Goi Ca Trich (Gỏi Cá Trích) - Herring Salad",
    "Banh Trang Cuon Thit Heo (Bánh Tráng Cuốn Thịt Heo) - Rice Paper Rolls with Pork",
    "Goi Cuon Chay (Gỏi Cuốn Chay) - Vegetarian Spring Rolls",
    "Goi Ca Mai (Gỏi Cá Mai) - Sardine Salad",
    "Goi Bap Chuoi (Gỏi Bắp Chuối) - Banana Flower Salad",

    # Grilled & Roasted
    "Ga Nuong Sa (Gà Nướng Sả) - Lemongrass Grilled Chicken",
    "Thit Nuong (Thịt Nướng) - Grilled Pork",
    "Bo Nuong La Lot (Bò Nướng Lá Lốt) - Grilled Beef in Betel Leaf",
    "Ca Nuong Giay Bac (Cá Nướng Giấy Bạc) - Grilled Fish in Foil",
    "Vit Quay (Vịt Quay) - Roast Duck",
    "Heo Quay (Heo Quay) - Roast Pork",
    "Ga Roti (Gà Roti) - Roast Chicken",
    "Bo Ne (Bò Né) - Sizzling Beef Steak",
    "Ca Loc Nuong Trui (Cá Lóc Nướng Trui) - Grilled Snakehead Fish",
    "Muc Nuong Sa Te (Mực Nướng Sa Tế) - Grilled Squid with Satay Sauce",

    # Desserts & Drinks
    "Che Ba Mau (Chè Ba Màu) - Three-Color Dessert",
    "Che Chuoi Nuong (Chè Chuối Nướng) - Grilled Banana Dessert",
    "Che Dau Xanh (Chè Đậu Xanh) - Mung Bean Dessert",
    "Banh Flan (Bánh Flan) - Vietnamese Caramel Custard",
    "Rau Cau (Rau Câu) - Jelly Dessert",
    "Che Thai (Chè Thái) - Thai Dessert",
    "Sinh To Bo (Sinh Tố Bơ) - Avocado Smoothie",
    "Ca Phe Sua Da (Cà Phê Sữa Đá) - Vietnamese Iced Coffee with Milk",
    "Tra Da (Trà Đá) - Iced Tea",
    "Nuoc Mia (Nước Mía) - Sugarcane Juice",

    # Regional Specialties
    "Bun Bo Giong (Bún Bò Giò Heo) - Hue Beef Noodle Soup with Pork Knuckle",
    "Banh Can (Bánh Căn) - Mini Savory Pancakes",
    "Banh Trang Cuon Thit Heo (Bánh Tráng Cuốn Thịt Heo) - Rice Paper Rolls with Pork",
    "Com Ga Hoi An (Cơm Gà Hội An) - Hoi An Chicken Rice",
    "My Quang Ech (Mỳ Quảng Ếch) - Quang Noodles with Frog",
    "Banh Dap (Bánh Đập) - Crispy Rice Paper with Wet Rice Paper",
    "Bun Mam (Bún Mắm) - Fermented Fish Noodle Soup",
    "Banh Trang Me (Bánh Tráng Mè) - Sesame Rice Crackers",
    "Banh Tet (Bánh Tét) - Savory Sticky Rice Cake",
    "Banh It Tran (Bánh Ít Trần) - Savory Rice Dumplings"
],
    "Middle Eastern": [
    # Appetizers & Meze
    "Hummus (حمص) - Chickpea Dip",
    "Baba Ghanoush (بابا غنوج) - Roasted Eggplant Dip",
    "Tabbouleh (تبولة) - Parsley, Mint, Bulgur Salad",
    "Fattoush (فتوش) - Levantine Bread Salad",
    "Muhammara (محمرة) - Roasted Red Pepper Dip",
    "Labneh (لبنة) - Strained Yogurt",
    "Kibbeh Nayeh (كبة نيئة) - Raw Kibbeh",
    "Sambusak (سمبوسك) - Savory Pastries",
    "Falafel (فلافل) - Fried Chickpea Balls",
    "Dolma (دولمة) - Stuffed Grape Leaves or Vegetables",
    "Waraq Enab (ورق عنب) - Stuffed Grape Leaves",
    "Mezze Platter (مزة) - Assortment of Small Dishes",
    "Moutabal (متبل) - Eggplant Dip",
    "Tzatziki (تزاتزيكي) - Yogurt and Cucumber Dip",
    "Olives and Pickles (زيتون ومخلل)",
    "Feta Cheese (جبنة فيتا)",
    "Halloumi Cheese (جبنة حلوم)",
    "Stuffed Vine Leaves (محشي ورق عنب)",
    "Spicy Potatoes (بطاطا حارة)",
    "Foul Medames (فول مدمس) - Stewed Fava Beans",

    # Main Courses (Meat & Poultry)
    "Shawarma (شاورما) - Grilled Meat in Pita or Wrap",
    "Kebab (كباب) - Grilled Meat Skewers",
    "Shish Kebab (شيش كباب)",
    "Kofta Kebab (كفتة كباب)",
    "Adana Kebab (أضنة كباب)",
    "Urfa Kebab (أورفة كباب)",
    "Döner Kebap (دونر كباب) - Meat Cooked on a Vertical Rotisserie",
    "Mansaf (منسف) - Lamb Cooked in Fermented Dried Yogurt Sauce with Rice",
    "Kibbeh (كبة) - Minced Meat and Bulgur Shells",
    "Kofta (كفتة) - Spiced Meatballs or Patties",
    "Tagine (طاجن) - Slow-Cooked Stew",
    "Lamb Tagine with Apricots (طاجن لحم بالمشمش)",
    "Chicken Tagine with Olives and Lemons (طاجن دجاج بالزيتون والليمون)",
    "Kefta Tagine (طاجن كفتة)",
    "Maqluba (مقلوبة) - Upside-Down Rice and Meat Dish",
    "Kabsa (كبسة) - Spiced Rice with Meat",
    "Biryani (برياني) - Spiced Rice with Meat",
    "Quzi (قوزي) - Slow-Cooked Lamb with Rice",
    "Machboos (مجبوس) - Spiced Meat and Rice Dish",
    "Mandi (مندي) - Pit-Cooked Meat and Rice",

    # Main Courses (Vegetarian)
    "Mujadara (مجدرة) - Lentils and Rice with Fried Onions",
    "Falafel (فلافل) - Fried Chickpea Balls",
    "Tabbouleh (تبولة) - Parsley, Mint, Bulgur Salad",
    "Fattoush (فتوش) - Levantine Bread Salad",
    "Ful Medames (فول مدمس) - Stewed Fava Beans",
    "Shakshuka (شكشوكة) - Eggs Poached in Tomato Sauce",
    "Kushari (كشري) - Egyptian Lentils, Rice, and Pasta Dish",
    "Dolma (دولمة) - Stuffed Vegetables or Leaves",
    "Yalanji (يالنجي) - Vegetarian Stuffed Grape Leaves",
    "Molokhia (ملوخية) - Jute Leaf Stew",
    "Bamya (بامية) - Okra Stew",
    "Fasolia (فاصوليا) - Green Bean Stew",
    "Makloubeh (مقلوبة خضار) - Vegetarian Upside-Down Rice Dish",
    "Kibbeh Nabulsieh (كبة نابلسية) - Vegetarian Kibbeh",
    "Vegetarian Tagine (طاجن خضار)",
    "Tabbouleh with Quinoa (تبولة بالكينوا)",
    "Vegetarian Couscous (كسكس بالخضار)",
    "Lentil Soup (شوربة العدس)",
    "Chickpea Stew (يخنة حمص)",
    "Stuffed Peppers (محشي فلفل)",

    # Breads & Grains
    "Pita Bread (خبز بيتا) - Flatbread",
    "Lavash (لواش) - Thin Flatbread",
    "Naan (نان) - Oven-Baked Flatbread",
    "Taboon Bread (خبز طابون) - Pit-Baked Flatbread",
    "Barbari Bread (بربری) - Persian Flatbread",
    "Sangak (سنگک) - Persian Sourdough Flatbread",
    "Khubz (خبز) - Arabic Flatbread",
    "Manakish (مناقيش) - Levantine Flatbread with Toppings",
    "Za'atar Manakish (مناقيش زعتر)",
    "Cheese Manakish (مناقيش جبنة)",
    "Lahmacun (لحم عجین) - Turkish Pizza",
    "Pide (پیده) - Turkish Flatbread with Toppings",
    "Couscous (كسكس) - Steamed Semolina Dish",
    "Bulgur Pilaf (برغل بيلاف)",
    "Freekeh Pilaf (فريكة بيلاف)",
    "Rice Pilaf (رز بيلاف)",
    "Ma'amoul (معمول) - Shortbread Cookies",
    "Qatayef (قطايف) - Sweet Dumplings",
    "Kanafeh (كنافة) - Sweet Cheese Pastry Soaked in Syrup",
    "Baklava (بقلاوة) - Sweet Pastry with Nuts and Syrup",

    # Desserts
    "Baklava (بقلاوة)",
    "Kanafeh (كنافة)",
    "Basbousa (بسبوسة) - Semolina Cake Soaked in Syrup",
    "Qatayef (قطايف)",
    "Ma'amoul (معمول)",
    "Halva (حلاوة)",
    "Muhalabia (مهلبية) - Milk Pudding",
    "Umm Ali (ام علي) - Egyptian Bread Pudding",
    "Luqaimat (لقيمات) - Sweet Dumplings",
    "Zalabia (زلابية) - Fried Sweet Dough",
    "Faloodeh (فالوده) - Persian Frozen Dessert",
    "Rosewater Pudding (مهلبية بماء الورد)",
    "Orange Blossom Cake (كعكة ماء الزهر)",
    "Date Cookies (كعك بالتمر)",
    "Semolina Halva (حلاوة سميد)",
    "Rice Pudding (رز بلبن)",
    "Turkish Delight (راحة الحلقوم)",
    "Ghorayebah (غريبة) - Shortbread Cookies",
    "Barazek (برازق) - Sesame and Pistachio Cookies",
    "Mamoul with Pistachios (معمول بالفستق)"
],
    
    "African": [
    # West African
    "Jollof Rice (West African One-Pot Rice Dish)",
    "Egusi Soup (West African Melon Seed Soup)",
    "Fufu with Groundnut Soup (West African Staple with Peanut Soup)",
    "Suya (West African Grilled Spicy Skewers)",
    "Thieboudienne (Senegalese Fish and Rice Dish)",
    "Yassa Poulet (Senegalese Lemon Chicken)",
    "Maafe (West African Peanut Stew)",
    "Akara (West African Bean Fritters)",
    "Banku and Tilapia (Ghanaian Fermented Corn and Cassava Dough with Fish)",
    "Kenkey (Ghanaian Fermented Corn Dough)",
    "Waakye (Ghanaian Rice and Beans)",
    "Jollof Rice with Chicken (Nigerian)",
    "Egusi Soup with Fufu (Nigerian)",
    "Pepper Soup (Nigerian)",
    "Nkwobi (Nigerian Spiced Cow Foot)",
    "Banga Soup (Nigerian Palm Fruit Soup)",
    "Efo Riro (Nigerian Spinach Stew)",
    "Moi Moi (Nigerian Bean Pudding)",
    "Chin Chin (West African Fried Dough)",
    "Zobo Drink (West African Hibiscus Tea)",

    # East African
    "Injera with Wat (Ethiopian Flatbread with Stew)",
    "Doro Wat (Ethiopian Chicken Stew with Berbere Spice)",
    "Kitfo (Ethiopian Minced Raw Beef)",
    "Gored Gored (Ethiopian Cubed Raw Beef)",
    "Tibs (Ethiopian Stir-Fried Meat)",
    "Shiro (Ethiopian Chickpea Stew)",
    "Ful Medames (Sudanese Stewed Fava Beans)",
    "Kachumbari (East African Fresh Salad)",
    "Ugali with Sukuma Wiki (East African Cornmeal Staple with Collard Greens)",
    "Nyama Choma (East African Grilled Meat)",
    "Pilau (East African Spiced Rice)",
    "Chapati (East African Flatbread)",
    "Mandazi (East African Sweet Doughnut)",
    "Maharagwe (East African Coconut Beans)",
    "Matoke (East African Steamed Plantains)",
    "Irio (Kenyan Mashed Potatoes and Peas)",
    "Mukimo (Kenyan Mashed Potatoes, Corn, and Beans)",
    "Githeri (Kenyan Corn and Beans Stew)",
    "Kuku Paka (Kenyan Coconut Chicken)",
    "Uji (East African Porridge)",

    # North African
    "Tagine with Lamb and Apricots (North African Stew)",
    "Couscous (North African Steamed Semolina Dish)",
    "Pastilla (Moroccan Sweet and Savory Pie)",
    "Harira (Moroccan Tomato and Lentil Soup)",
    "Brik (Tunisian Thin Pastry with Filling)",
    "Mechoui (North African Roasted Lamb or Mutton)",
    "Rfissa (Moroccan Chicken and Lentil Dish)",
    "Chorba (North African Soup)",
    "Makroudh (Algerian Semolina Cookies)",
    "Tajine Mrouzia (Moroccan Sweet and Savory Tagine)",
    "Couscous Tfaya (Moroccan Sweet and Savory Couscous)",
    "Bastilla au Pigeon (Moroccan Pigeon Pie)",
    "Tagine Kefta (Moroccan Meatball Tagine)",
    "Zaalouk (Moroccan Eggplant Dip)",
    "Couscous with Seven Vegetables (Moroccan)",
    "Chermoula (North African Marinade)",
    "Msemen (Moroccan Flatbread)",
    "Sfenj (Moroccan Doughnuts)",
    "Ma'amoul (North African Date-Filled Cookies)",
    "Mint Tea (North African)",

    # Southern African
    "Bobotie (South African Spiced Minced Meat Casserole)",
    "Bunny Chow (South African Bread Bowl Curry)",
    "Piri Piri Chicken (Mozambican/South African Spicy Grilled Chicken)",
    "Biltong (South African Dried Cured Meat)",
    "Boerewors (South African Farmer's Sausage)",
    "Chakalaka (South African Spicy Vegetable Relish)",
    "Pap (South African Maize Porridge)",
    "Samp and Beans (South African Crushed Corn and Bean Dish)",
    "Malva Pudding (South African Spongy Caramel Pudding)",
    "Koeksisters (South African Syrup-Soaked Dough Twists)",
    "Melktert (South African Milk Tart)",
    "Vetkoek (South African Fried Dough Cakes)",
    "Sosaties (South African Meat Skewers)",
    "Potjiekos (South African Stew Cooked in a Pot)",
    "Bredie (South African Meat and Vegetable Stew)",
    "Umngqusho (South African Samp and Beans)",
    "Amagwinya (South African Fat Cakes)",
    "Koesisters (Cape Malay Spiced Doughnuts)",
    "Waterblommetjie Bredie (Cape Malay Waterblommetjie Stew)",
    "Peppermint Crisp Tart (South African Dessert)",

    # Central African
    "Moambe Chicken (Congolese Palm Butter Chicken)",
    "Fufu with Moambe Sauce (Congolese)",
    "Saka Saka (Congolese Cassava Leaf Stew)",
    "Poulet DG (Cameroonian Plantain and Chicken Dish)",
    "Ndolé (Cameroonian Bitter Leaf Stew)",
    "Egusi Soup (Cameroonian Melon Seed Soup)",
    "Eru (Cameroonian Vegetable Soup)",
    "Mbongo Tchobi (Cameroonian Black Stew)",
    "Kanda (Congolese Maize Bread)",
    "Mikate (Congolese Fried Bread)",
    "Beignets (Central African Doughnuts)",
    "Plantains (Central African)",
    "Cassava (Central African)",
    "Palm Wine (Central African)",
    "Peanut Stew (Central African)",
    "Fish Stew (Central African)",
    "Spiced Rice (Central African)",
    "Sweet Potato Leaves (Central African)",
    "Okra Stew (Central African)",
    "Groundnut Soup (Central African)"
],
    "Nordic / Scandinavian": [
    # Danish
    "Smørrebrød (Danish Open-Faced Sandwiches)",
    "Frikadeller (Danish Meatballs)",
    "Stegt Flæsk med Persillesovs (Danish Fried Pork with Parsley Sauce)",
    "Hakkebøf med Løg (Danish Chopped Steak with Onions)",
    "Boller i Karry (Danish Meatballs in Curry Sauce)",
    "Æbleskiver (Danish Apple Fritters)",
    "Rødgrød med fløde (Danish Red Berry Pudding with Cream)",
    "Risengrød (Danish Rice Pudding)",
    "Koldskål (Danish Cold Buttermilk Soup)",
    "Kartoffelsuppe (Danish Potato Soup)",
    "Fiskefrikadeller (Danish Fish Cakes)",
    "Skipperlabskovs (Danish Sailor's Stew)",
    "Kransekage (Danish Marzipan Ring Cake)",
    "Fastelavnsboller (Danish Shrove Buns)",
    "Brunede Kartofler (Danish Caramelized Potatoes)",
    "Gravad Laks (Danish Cured Salmon)",
    "Sild (Danish Pickled Herring)",
    "Rugbrød (Danish Rye Bread)",
    "Wienerbrød (Danish Pastries)",
    "Flæskesteg (Danish Roast Pork)",

    # Swedish
    "Köttbullar (Swedish Meatballs)",
    "Pyttipanna (Swedish Hash)",
    "Gravlax (Swedish Cured Salmon)",
    "Inlagd Sill (Swedish Pickled Herring)",
    "Janssons Frestelse (Swedish Potato and Anchovy Casserole)",
    "Ärtsoppa med Pannkakor (Swedish Pea Soup with Pancakes)",
    "Semla (Swedish Cream-Filled Cardamom Bun)",
    "Kanelbullar (Swedish Cinnamon Buns)",
    "Prinsesstårta (Swedish Princess Cake)",
    "Kladdkaka (Swedish Sticky Chocolate Cake)",
    "Raggmunk (Swedish Potato Pancakes)",
    "Kroppkakor (Swedish Potato Dumplings)",
    "Surströmming (Swedish Fermented Herring)",
    "Pepparkakor (Swedish Gingerbread Cookies)",
    "Lussebullar (Swedish Saffron Buns)",
    "Smörgåstårta (Swedish Sandwich Cake)",
    "Toast Skagen (Swedish Shrimp Toast)",
    "Pickled Beetroot (Swedish)",
    "Pickled Cucumber (Swedish)",
    "Lingonberry Jam (Swedish)",

    # Norwegian
    "Fårikål (Norwegian Lamb and Cabbage Stew)",
    "Lutefisk (Norwegian Dried Whitefish Soaked in Lye)",
    "Raspeballer (Norwegian Potato Dumplings)",
    "Rømmegrøt (Norwegian Sour Cream Porridge)",
    "Lefse (Norwegian Soft Flatbread)",
    "Brunost (Norwegian Brown Cheese)",
    "Pinnekjøtt (Norwegian Steamed Ribs)",
    "Smalahove (Norwegian Sheep's Head)",
    "Sodd (Norwegian Meat and Dumpling Soup)",
    "Lapskaus (Norwegian Stew)",
    "Fiskesuppe (Norwegian Fish Soup)",
    "Krumkaker (Norwegian Thin Waffles)",
    "Vaffler (Norwegian Waffles)",
    "Multekrem (Norwegian Cloudberry Cream)",
    "Riskrem (Norwegian Rice Cream)",
    "Solbærtoddy (Norwegian Blackcurrant Toddy)",
    "Aquavit (Norwegian Spirit)",
    "Pickled Herring (Norwegian)",
    "Lox (Norwegian Cured Salmon)",
    "Lutefisk with Mustard Sauce (Norwegian)",

    # Finnish
    "Karjalanpiirakka (Finnish Karelian Pies)",
    "Kalakukko (Finnish Fish Pie)",
    "Lihapullat (Finnish Meatballs)",
    "Lohikeitto (Finnish Salmon Soup)",
    "Hernekeitto (Finnish Pea Soup)",
    "Mämmi (Finnish Easter Pudding)",
    "Ruisleipä (Finnish Rye Bread)",
    "Korvapuustit (Finnish Cinnamon Buns)",
    "Pulla (Finnish Sweet Bread)",
    "Mustikkapiirakka (Finnish Blueberry Pie)",
    "Leipäjuusto (Finnish Bread Cheese)",
    "Sillisalaatti (Finnish Herring Salad)",
    "Graavilohi (Finnish Cured Salmon)",
    "Lanttulaatikko (Finnish Rutabaga Casserole)",
    "Maksalaatikko (Finnish Liver Casserole)",
    "Kalakeitto (Finnish Fish Soup)",
    "Karjalanpaisti (Finnish Karelian Stew)",
    "Rönttönen (Finnish Rye Pastry)",
    "Sultsina (Finnish Rice Pastry)",
    "Vispipuuro (Finnish Whipped Berry Porridge)",

    # Icelandic
    "Hangikjöt (Icelandic Smoked Lamb)",
    "Skyr (Icelandic Cultured Dairy Product)",
    "Harðfiskur (Icelandic Dried Fish)",
    "Plokkfiskur (Icelandic Fish Stew)",
    "Rúgbrauð (Icelandic Hot Spring Bread)",
    "Kleinur (Icelandic Twisted Doughnuts)",
    "Vinarterta (Icelandic Layer Cake)",
    "Brennivín (Icelandic Spirit)",
    "Lamb Soup (Icelandic)",
    "Fish Soup (Icelandic)",
    "Saltfiskur (Icelandic Salted Fish)",
    "Hákarl (Icelandic Fermented Shark)",
    "Hangikjöt with Bechamél (Icelandic)",
    "Skyr Cake (Icelandic)",
    "Pönnukökur (Icelandic Pancakes)",
    "Rúgbrauð with Butter (Icelandic)",
    "Laufabrauð (Icelandic Thin Fried Bread)",
    "Slátur (Icelandic Blood Pudding and Liver Sausage)",
    "Svið (Icelandic Singed Sheep's Head)",
    "Hangikjöt with Flatkaka (Icelandic)"
],
    "Eastern European": [
    # Polish
    "Pierogi (Polish Dumplings)",
    "Bigos (Polish Hunter's Stew)",
    "Golabki (Polish Cabbage Rolls)",
    "Kielbasa (Polish Sausage)",
    "Żurek (Polish Sour Rye Soup)",
    "Barszcz (Polish Beetroot Soup)",
    "Kotlet Schabowy (Polish Breaded Pork Cutlet)",
    "Placki Ziemniaczane (Polish Potato Pancakes)",
    "Pyzy (Polish Potato Dumplings)",
    "Kaszanka (Polish Blood Sausage)",
    "Ogórkowa (Polish Pickle Soup)",
    "Kapuśniak (Polish Cabbage Soup)",
    "Pierogi Ruskie (Polish Potato and Cheese Pierogi)",
    "Makowiec (Polish Poppy Seed Roll)",
    "Sernik (Polish Cheesecake)",
    "Pączki (Polish Doughnuts)",
    "Rosół (Polish Chicken Soup)",
    "Zrazy (Polish Beef Rolls)",
    "Bigos Staropolski (Old Polish Hunter's Stew)",
    "Krupnik (Polish Barley Soup)",

    # Russian
    "Borscht (Russian Beet Soup)",
    "Pelmeni (Russian Meat Dumplings)",
    "Blini (Russian Pancakes)",
    "Pirozhki (Russian Stuffed Buns)",
    "Solyanka (Russian Sour and Spicy Soup)",
    "Beef Stroganoff (Russian Beef Dish)",
    "Golubtsy (Russian Cabbage Rolls)",
    "Olivier Salad (Russian Potato Salad)",
    "Kholodets (Russian Meat Jelly)",
    "Ukha (Russian Fish Soup)",
    "Kasha (Russian Buckwheat Groats)",
    "Blinchiki (Thin Russian Crepes)",
    "Syrniki (Russian Cheese Pancakes)",
    "Medovik (Russian Honey Cake)",
    "Napoleon Cake (Layered Pastry Cream Cake)",
    "Paskha (Russian Easter Dessert)",
    "Kutia (Russian Sweet Grain Pudding)",
    "Pelmeni v Gorshochkah (Russian Pelmeni Baked in Pots)",
    "Vareniki (Russian Dumplings)",
    "Kisel (Russian Berry Dessert)",

    # Ukrainian
    "Varenyky (Ukrainian Dumplings)",
    "Borshch (Ukrainian Beet Soup)",
    "Holubtsi (Ukrainian Cabbage Rolls)",
    "Chicken Kyiv (Ukrainian Stuffed Chicken Breast)",
    "Deruny (Ukrainian Potato Pancakes)",
    "Salo (Ukrainian Cured Pork Fat)",
    "Pampushky (Ukrainian Garlic Bread Rolls)",
    "Nalysnyky (Ukrainian Crepes)",
    "Kutia (Ukrainian Sweet Grain Pudding)",
    "Paska (Ukrainian Easter Bread)",
    "Kapustnyak (Ukrainian Cabbage Soup)",
    "Pyrizhky (Ukrainian Stuffed Buns)",
    "Krovyanka (Ukrainian Blood Sausage)",
    "Verhuny (Ukrainian Fried Pastries)",
    "Medivnyk (Ukrainian Honey Cake)",
    "Syrniki (Ukrainian Cheese Pancakes)",
    "Uzvar (Ukrainian Dried Fruit Drink)",
    "Lvivskyi Syrnyk (Lviv Cheesecake)",
    "Banosh (Ukrainian Cornmeal Dish)",
    "Kovbasa (Ukrainian Sausage)",

    # Hungarian
    "Goulash (Hungarian Meat Stew)",
    "Paprikash (Hungarian Stew with Paprika)",
    "Halászlé (Hungarian Fisherman's Soup)",
    "Lángos (Hungarian Fried Flatbread)",
    "Töltött Káposzta (Hungarian Stuffed Cabbage)",
    "Pörkölt (Hungarian Meat Stew)",
    "Paprikás Csirke (Hungarian Chicken Paprikash)",
    "Hortobágyi Palacsinta (Hungarian Savory Crepes)",
    "Dobos Torta (Hungarian Drum Torte)",
    "Eszterházy Torta (Hungarian Esterházy Torte)",
    "Gulyásleves (Hungarian Goulash Soup)",
    "Lecsó (Hungarian Vegetable Stew)",
    "Tökfőzelék (Hungarian Zucchini Stew)",
    "Főzelék (Hungarian Vegetable Stew)",
    "Somlói Galuska (Hungarian Somló Dumplings)",
    "Bejgli (Hungarian Poppy Seed or Walnut Roll)",
    "Kürtőskalács (Hungarian Chimney Cake)",
    "Pogácsa (Hungarian Scones)",
    "Túrós Csusza (Hungarian Pasta with Cottage Cheese and Bacon)",
    "Csirkepaprikás (Hungarian Chicken Paprikash)",

    # Czech & Slovak
    "Svíčková na Smetaně (Czech Beef Sirloin in Cream Sauce)",
    "Vepřo-knedlo-zelo (Czech Roast Pork with Dumplings and Cabbage)",
    "Guláš (Czech and Slovak Goulash)",
    "Knedlíky (Czech and Slovak Dumplings)",
    "Trdelník (Czech and Slovak Sweet Pastry)",
    "Bramboračka (Czech Potato Soup)",
    "Česnečka (Czech Garlic Soup)",
    "Kulajda (Czech Creamy Mushroom Soup)",
    "Rajská omáčka (Czech Tomato Sauce with Meat)",
    "Moravský vrabec (Czech Roast Pork)",
    "Tatarák (Czech Steak Tartare)",
    "Palačinky (Czech and Slovak Crepes)",
    "Štrúdľa (Czech and Slovak Strudel)",
    "Medovník (Czech Honey Cake)",
    "Makové rezance (Slovak Poppy Seed Noodles)",
    "Bryndzové halušky (Slovak Sheep Cheese Dumplings)",
    "Kapustnica (Slovak Cabbage Soup)",
    "Žemľovka (Slovak Bread Pudding)",
    "Vianočka (Czech and Slovak Christmas Bread)",
    "Ovocné knedlíky (Czech and Slovak Fruit Dumplings)",

    # Balkan
    "Ćevapi (Balkan Grilled Minced Meat)",
    "Burek (Balkan Flaky Pastry with Filling)",
    "Sarma (Balkan Stuffed Cabbage or Grape Leaves)",
    "Moussaka (Balkan Layered Dish with Eggplant and Meat)",
    "Pljeskavica (Balkan Grilled Meat Patty)",
    "Grah (Balkan Bean Stew)",
    "Ajvar (Balkan Roasted Red Pepper Relish)",
    "Baklava (Balkan Sweet Pastry with Nuts and Syrup)",
    "Tufahije (Balkan Stuffed Apples)",
    "Ćevapčići (Balkan Grilled Minced Meat)",
    "Grah sa suvim mesom (Balkan Bean Stew with Smoked Meat)",
    "Šopska salata (Balkan Shopska Salad)",
    "Krempita (Balkan Custard Slice)",
    "Palacinke (Balkan Pancakes)",
    "Gibanica (Balkan Cheese Pie)",
    "Sutlijash (Balkan Rice Pudding)",
    "Tulumbe (Balkan Fried Dough Soaked in Syrup)",
    "Trilece (Balkan Three Milk Cake)",
    "Ćevapi sa kajmakom (Balkan Ćevapi with Cream)",
    "Punjene paprike (Balkan Stuffed Peppers)"
],
    "Caribbean": [
    # Jamaican
    "Jerk Chicken (Jamaican Spicy Grilled Chicken)",
    "Ackee and Saltfish (Jamaican National Dish)",
    "Rice and Peas (Jamaican Coconut Rice and Beans)",
    "Curry Goat (Jamaican Spiced Goat Stew)",
    "Escovitch Fish (Jamaican Pickled Fish)",
    "Bammy (Jamaican Cassava Flatbread)",
    "Festival (Jamaican Sweet Fried Dough)",
    "Patties (Jamaican Savory Pastries)",
    "Callaloo Soup (Jamaican Leafy Green Soup)",
    "Mannish Water (Jamaican Goat Soup)",
    "Stamp and Go (Jamaican Saltfish Fritters)",
    "Oxtail Stew (Jamaican Braised Oxtail)",
    "Brown Stew Chicken (Jamaican Braised Chicken)",
    "Run Down (Jamaican Coconut Stew with Fish)",
    "Gizzada (Jamaican Coconut Tart)",
    "Toto (Jamaican Coconut Cake)",
    "Bun and Cheese (Jamaican Easter Treat)",
    "Sorrel Drink (Jamaican Hibiscus Drink)",
    "Rum Punch (Jamaican Rum Cocktail)",
    "Jamaican Fruit Cake (Black Cake)",

    # Trinidadian & Tobagonian
    "Doubles (Trinidadian Street Food - Fried Flatbread with Chickpea Curry)",
    "Roti (Trinidadian Flatbread)",
    "Curry Crab and Dumplings (Trinidadian)",
    "Oil Down (Grenadian One-Pot Breadfruit Stew)",
    "Pelau (Trinidadian One-Pot Rice Dish with Meat and Vegetables)",
    "Callaloo (Trinidadian Leafy Green Stew)",
    "Bake and Shark (Trinidadian Fried Shark Sandwich)",
    "Pholourie (Trinidadian Split Pea Fritters)",
    "Aloo Pie (Trinidadian Potato-Filled Pastry)",
    "Souse (Trinidadian Pickled Pork)",
    "Crab and Callaloo (Trinidadian)",
    "Macaroni Pie (Trinidadian Baked Macaroni and Cheese)",
    "Dhal and Rice (Trinidadian)",
    "Saheena (Trinidadian Spinach and Chickpea Fritters)",
    "Buss Up Shut (Trinidadian Roti with Curry)",
    "Coconut Bake (Trinidadian Coconut Bread)",
    "Sweet Bread (Trinidadian)",
    "Ponche de Creme (Trinidadian Christmas Drink)",
    "Mauby (Caribbean Bark-Based Drink)",
    "Trinidadian Rum Cake",

    # Barbadian
    "Cou-Cou and Flying Fish (Barbadian National Dish)",
    "Macaroni Pie (Barbadian Baked Macaroni and Cheese)",
    "Jug Jug (Barbadian Pigeon Peas and Guinea Corn Dish)",
    "Pudding 'n' Souse (Barbadian Pickled Pork and Sweet Potato)",
    "Conkies (Barbadian Cornmeal Dumplings)",
    "Fish Cakes (Barbadian)",
    "Cutters (Barbadian Sandwiches)",
    "Sweet Bread (Barbadian)",
    "Great Cake (Barbadian Fruitcake)",
    "Bajan Pepperpot (Barbadian Meat Stew)",
    "Barbadian Sweet Bread Pudding",

    # Puerto Rican
    "Mofongo (Puerto Rican Mashed Plantains)",
    "Arroz con Gandules (Puerto Rican Rice with Pigeon Peas)",
    "Pasteles (Puerto Rican Root Vegetable Tamales)",
    "Pernil (Puerto Rican Roasted Pork Shoulder)",
    "Tostones (Puerto Rican Fried Plantains)",
    "Alcapurrias (Puerto Rican Fritters)",
    "Bacalaítos (Puerto Rican Codfish Fritters)",
    "Mojo Criollo (Puerto Rican Garlic Sauce)",
    "Sancocho (Puerto Rican Stew)",
    "Asopao (Puerto Rican Rice Soup)",
    "Habichuelas Guisadas (Puerto Rican Stewed Beans)",
    "Piononos (Puerto Rican Sweet Plantain Casserole)",
    "Tembleque (Puerto Rican Coconut Pudding)",
    "Coquito (Puerto Rican Coconut Drink)",
    "Piña Colada (Puerto Rican Cocktail)",
    "Arroz con Dulce (Puerto Rican Rice Pudding)",
    "Flan de Coco (Puerto Rican Coconut Flan)",
    "Mallorcas (Puerto Rican Sweet Bread)",
    "Mamposteao (Puerto Rican Rice and Beans)",
    "Pastelón (Puerto Rican Sweet Plantain Lasagna)",

    # Dominican Republic
    "La Bandera Dominicana (Dominican Republic's National Dish)",
    "Mangu (Dominican Mashed Plantains)",
    "Tostones (Dominican Republic Fried Plantains)",
    "Sancocho (Dominican Republic Stew)",
    "Moro de Guandules (Dominican Republic Rice and Pigeon Peas)",
    "Habichuelas con Dulce (Dominican Republic Sweet Beans)",
    "Pasteles en Hoja (Dominican Republic Root Vegetable Tamales)",
]
}

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

def filter_authentic_recipes(authentic_recipes, user_prefs, health_requirements):
    """
    Filter authentic recipe names based on user preferences and health requirements.
    Returns a list of suitable recipe names.
    """
    filtered_recipes = []
    
    # Get dietary restrictions
    diet_type = user_prefs.get('diet', 'None')
    allergies = user_prefs.get('allergies', [])
    health_conditions = user_prefs.get('health_conditions', [])
    time_constraint = user_prefs.get('time_constraint', 'No Constraints')
    budget = user_prefs.get('budget', 'No budget constraints ($31+)')
    
    # Define restrictions based on diet type
    diet_restrictions = {
        "Vegetarian": ["meat", "fish", "poultry", "seafood"],
        "Vegan": ["meat", "fish", "poultry", "seafood", "dairy", "eggs", "honey"],
        "Pescatarian": ["meat", "poultry"],
        "Gluten-Free": ["wheat", "barley", "rye", "flour"],
        "Dairy-Free": ["milk", "cheese", "butter", "cream", "yogurt"],
        "Nut-Free": ["nuts", "peanuts", "almonds", "cashews", "walnuts"],
        "Egg-Free": ["eggs", "egg whites", "egg yolks"],
        "Soy-Free": ["soy", "soybeans", "tofu", "soy sauce"],
        "Shellfish-Free": ["shrimp", "crab", "lobster", "shellfish"],
        "Halal": ["pork", "alcohol", "gelatin"],
        "Kosher": ["pork", "shellfish", "mixing meat and dairy"],
        "Low-Carb": ["rice", "pasta", "bread", "potatoes", "sugar"],
        "Low-Fat": ["butter", "oil", "cream", "fatty meats"],
        "Low-Sodium": ["salt", "soy sauce", "processed foods"],
        "Diabetic-Friendly": ["sugar", "honey", "syrup", "white flour"],
        "Paleo": ["grains", "legumes", "dairy", "processed foods"],
        "Keto": ["grains", "sugar", "high-carb vegetables", "fruits"],
        "Whole30": ["grains", "legumes", "dairy", "sugar", "alcohol"],
        "Mediterranean": ["processed foods", "red meat", "sugar"],
        "DASH": ["red meat", "sugar", "high-sodium foods"],
        "Low-FODMAP": ["onions", "garlic", "wheat", "dairy", "certain fruits"],
        "Anti-Inflammatory": ["processed foods", "sugar", "red meat", "dairy"],
        "Low-Purine": ["organ meats", "seafood", "red meat", "alcohol"],
        "Renal": ["high-potassium foods", "high-phosphorus foods", "high-sodium foods"],
        "Low-Fiber": ["whole grains", "raw vegetables", "nuts", "seeds"],
        "Low-Residue": ["whole grains", "raw vegetables", "nuts", "seeds", "dairy"],
        "Low-Oxalate": ["spinach", "rhubarb", "beets", "nuts", "chocolate"],
        "Low-Histamine": ["fermented foods", "aged cheeses", "processed meats", "alcohol"],
        "Low-Tyramine": ["aged cheeses", "processed meats", "fermented foods", "alcohol"],
        "Low-Salicylate": ["berries", "citrus", "tomatoes", "spices"],
        "Low-Sulfur": ["cruciferous vegetables", "eggs", "meat", "dairy"],
        "Low-Iodine": ["iodized salt", "seafood", "dairy", "eggs"],
        "Low-Copper": ["organ meats", "shellfish", "nuts", "chocolate"],
        "Low-Omega-6": ["vegetable oils", "nuts", "seeds", "processed foods"],
        "Low-Phytate": ["whole grains", "legumes", "nuts", "seeds"],
        "Low-Lectin": ["legumes", "grains", "nightshades", "dairy"],
        "Low-Oxalate": ["spinach", "rhubarb", "beets", "nuts", "chocolate"],
        "Low-FODMAP": ["onions", "garlic", "wheat", "dairy", "certain fruits"],
        "Low-Glycemic": ["sugar", "white flour", "processed foods", "high-GI foods"],
        "Low-Fat": ["butter", "oil", "cream", "fatty meats"],
        "Low-Protein": ["meat", "fish", "poultry", "dairy", "eggs", "legumes"],
        "Low-Calorie": ["high-calorie foods", "sugar", "fat", "processed foods"],
        "Low-Cholesterol": ["egg yolks", "organ meats", "shellfish", "fatty meats"],
        "Low-Sugar": ["sugar", "honey", "syrup", "processed foods"],
        "Low-Salt": ["salt", "soy sauce", "processed foods"],
        "Low-Acid": ["citrus", "tomatoes", "vinegar", "coffee"],
        "Low-Alkaline": ["dairy", "meat", "fish", "eggs"],
        "Low-Potassium": ["bananas", "potatoes", "tomatoes", "oranges"],
        "Low-Phosphorus": ["dairy", "meat", "fish", "nuts", "seeds"],
        "Low-Magnesium": ["nuts", "seeds", "whole grains", "dark chocolate"],
        "Low-Calcium": ["dairy", "leafy greens", "fortified foods"],
        "Low-Iron": ["red meat", "organ meats", "shellfish", "legumes"],
        "Low-Zinc": ["meat", "shellfish", "nuts", "seeds"],
        "Low-Selenium": ["seafood", "meat", "nuts", "seeds"],
        "Low-Vitamin-A": ["liver", "dairy", "eggs", "orange vegetables"],
        "Low-Vitamin-D": ["fatty fish", "egg yolks", "fortified foods"],
        "Low-Vitamin-E": ["nuts", "seeds", "vegetable oils"],
        "Low-Vitamin-K": ["leafy greens", "vegetable oils", "meat"],
        "Low-Vitamin-C": ["citrus", "berries", "tomatoes", "peppers"],
        "Low-Vitamin-B12": ["meat", "fish", "dairy", "eggs"],
        "Low-Folate": ["leafy greens", "legumes", "fortified foods"],
        "Low-Niacin": ["meat", "fish", "nuts", "seeds"],
        "Low-Riboflavin": ["dairy", "meat", "eggs", "leafy greens"],
        "Low-Thiamine": ["whole grains", "meat", "fish", "legumes"],
        "Low-Pantothenic-Acid": ["meat", "fish", "whole grains", "vegetables"],
        "Low-Biotin": ["egg yolks", "organ meats", "nuts", "seeds"],
        "Low-Choline": ["eggs", "meat", "fish", "dairy"],
        "Low-Copper": ["organ meats", "shellfish", "nuts", "seeds"],
        "Low-Manganese": ["whole grains", "nuts", "seeds", "leafy greens"],
        "Low-Molybdenum": ["legumes", "whole grains", "nuts", "seeds"],
        "Low-Chromium": ["whole grains", "meat", "fish", "vegetables"],
        "Low-Fluoride": ["tea", "seafood", "fluoridated water"],
        "Low-Iodine": ["iodized salt", "seafood", "dairy", "eggs"],
        "Low-Selenium": ["seafood", "meat", "nuts", "seeds"],
        "Low-Zinc": ["meat", "shellfish", "nuts", "seeds"],
        "Low-Iron": ["red meat", "organ meats", "shellfish", "legumes"],
        "Low-Calcium": ["dairy", "leafy greens", "fortified foods"],
        "Low-Magnesium": ["nuts", "seeds", "whole grains", "dark chocolate"],
        "Low-Phosphorus": ["dairy", "meat", "fish", "nuts", "seeds"],
        "Low-Potassium": ["bananas", "potatoes", "tomatoes", "oranges"],
        "Low-Sodium": ["salt", "soy sauce", "processed foods"],
        "Low-Chloride": ["salt", "processed foods"],
        "Low-Sulfur": ["cruciferous vegetables", "eggs", "meat", "dairy"],
        "Low-Boron": ["fruits", "vegetables", "nuts", "legumes"],
        "Low-Silicon": ["whole grains", "vegetables", "fruits"],
        "Low-Vanadium": ["mushrooms", "shellfish", "grains", "vegetables"],
        "Low-Nickel": ["chocolate", "nuts", "legumes", "whole grains"],
        "Low-Lithium": ["vegetables", "grains", "meat", "fish"],
        "Low-Strontium": ["dairy", "seafood", "grains", "vegetables"],
        "Low-Tin": ["canned foods", "processed foods"],
        "Low-Aluminum": ["processed foods", "baking powder", "antacids"],
        "Low-Arsenic": ["rice", "seafood", "poultry"],
        "Low-Cadmium": ["organ meats", "shellfish", "grains", "vegetables"],
        "Low-Lead": ["organ meats", "shellfish", "grains", "vegetables"],
        "Low-Mercury": ["large fish", "shellfish"],
        "Low-Uranium": ["seafood", "grains", "vegetables"],
        "Low-Plutonium": ["seafood", "grains", "vegetables"],
        "Low-Thorium": ["seafood", "grains", "vegetables"],
        "Low-Radium": ["seafood", "grains", "vegetables"],
        "Low-Polonium": ["seafood", "grains", "vegetables"],
        "Low-Actinium": ["seafood", "grains", "vegetables"],
        "Low-Protactinium": ["seafood", "grains", "vegetables"],
        "Low-Neptunium": ["seafood", "grains", "vegetables"],
        "Low-Americium": ["seafood", "grains", "vegetables"],
        "Low-Curium": ["seafood", "grains", "vegetables"],
        "Low-Berkelium": ["seafood", "grains", "vegetables"],
        "Low-Californium": ["seafood", "grains", "vegetables"],
        "Low-Einsteinium": ["seafood", "grains", "vegetables"],
        "Low-Fermium": ["seafood", "grains", "vegetables"],
        "Low-Mendelevium": ["seafood", "grains", "vegetables"],
        "Low-Nobelium": ["seafood", "grains", "vegetables"],
        "Low-Lawrencium": ["seafood", "grains", "vegetables"],
        "Low-Rutherfordium": ["seafood", "grains", "vegetables"],
        "Low-Dubnium": ["seafood", "grains", "vegetables"],
        "Low-Seaborgium": ["seafood", "grains", "vegetables"],
        "Low-Bohrium": ["seafood", "grains", "vegetables"],
        "Low-Hassium": ["seafood", "grains", "vegetables"],
        "Low-Meitnerium": ["seafood", "grains", "vegetables"],
        "Low-Darmstadtium": ["seafood", "grains", "vegetables"],
        "Low-Roentgenium": ["seafood", "grains", "vegetables"],
        "Low-Copernicium": ["seafood", "grains", "vegetables"],
        "Low-Nihonium": ["seafood", "grains", "vegetables"],
        "Low-Flerovium": ["seafood", "grains", "vegetables"],
        "Low-Moscovium": ["seafood", "grains", "vegetables"],
        "Low-Livermorium": ["seafood", "grains", "vegetables"],
        "Low-Tennessine": ["seafood", "grains", "vegetables"],
        "Low-Oganesson": ["seafood", "grains", "vegetables"]
    }
    
    # Define time constraints
    time_restrictions = {
        "Busy schedule (15 mins)": ["slow-cooked", "roasted", "braised", "simmered", "baked"],
        "Moderate schedule (30 mins)": ["slow-cooked", "braised", "simmered"],
        "Busy on some days (45 mins)": ["slow-cooked"],
        "Flexible Schedule (60 mins)": [],
        "No Constraints": []
    }
    
    # Define budget constraints
    budget_restrictions = {
        "Tight budget ($3-$7)": ["lobster", "caviar", "truffle", "wagyu", "foie gras"],
        "Moderate budget ($8-$15)": ["lobster", "caviar", "truffle", "wagyu"],
        "Generous budget ($16-$30)": ["caviar", "truffle"],
        "No budget constraints ($31+)": []
    }
    
    # Combine all restrictions
    all_restrictions = []
    if diet_type in diet_restrictions:
        all_restrictions.extend(diet_restrictions[diet_type])
    all_restrictions.extend(allergies)
    all_restrictions.extend(health_conditions)
    if time_constraint in time_restrictions:
        all_restrictions.extend(time_restrictions[time_constraint])
    if budget in budget_restrictions:
        all_restrictions.extend(budget_restrictions[budget])
    
    # Filter recipes
    for recipe in authentic_recipes:
        # Check if recipe contains any restricted ingredients or methods
        recipe_lower = recipe.lower()
        if not any(restriction.lower() in recipe_lower for restriction in all_restrictions):
            filtered_recipes.append(recipe)
    
    return filtered_recipes

def get_meal_prompt(meal_type, day, user_prefs, health_requirements, cuisine_requirements, available_ingredients=None, authentic_recipes=None):
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

    # Get authentic recipe names for the cuisine
    if authentic_recipes is None:
        authentic_recipes = AUTHENTIC_RECIPE_NAMES.get(user_prefs['cuisine'], [])
    
    # Filter recipe names based on user preferences
    filtered_recipes = filter_authentic_recipes(authentic_recipes, user_prefs, health_requirements)
    
    # If no recipes remain after filtering, use a default list
    if not filtered_recipes:
        filtered_recipes = ["Custom Recipe"]  # Fallback option

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
**Day {day} - {meal_type} - [MUST USE ONE OF THESE EXACT RECIPE NAMES: {', '.join(authentic_recipes)}]**

**Description:**
[Choose one of the descriptions below as the foundation for the introduction, ensuring it aligns with the recipe without repeating it. Each introduction should be unique, so avoid using the same description style twice. Keep it engaging and concise, maintaining a single captivating paragraph without splitting it into multiple sections. The description should be 400-450 characters. Check the below descriptions and choose one that is not similar to the ones already used: 

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
[List all ingredients have to use Australian measurements. Do not use US measurements. Also, it has to use Australian terms, such as "capsicum" instead of "bell pepper." Ensure that units of measurement are relevant to the ingredient type and aligned with Australian supermarket packaging. Liquids should be measured in teaspoons, tablespoons, or millilitres (ml); solids should be measured in grams (g) or whole units (e.g., ½ avocado, 1 zucchini, ½ capsicum); garlic should be measured in cloves; and tomatoes should be measured in halves, quarters, etc. Where possible, reference Coles or Woolworths packaging sizes to ensure realistic portioning. List all ingredients in a single list without subheadings]

**Instructions**:
Write comprehensive and user-friendly recipe instructions in UK English using the metric system. **IMPORTANT: The total length of all instructions combined must be between 1350 and 1450 characters. There must be exactly 6 steps (7 steps only if absolutely necessary).** Each step should be approximately 200-250 characters long and include:
- Detailed preparation instructions with specific measurements and timings
- Exact cooking temperatures and heat levels
- Visual and sensory cues (e.g., "until golden brown", "when fragrant")
- Safety tips and common mistakes to avoid
- Specific ingredient handling instructions
- Tips for achieving the best results
- Serving suggestions and presentation tips
- Explanations of cooking techniques and why they're important

Example format (each step should be similar in length and detail):

1. Begin by preparing your mise en place - this French term means having all your ingredients prepped and ready to go. Heat 2 tablespoons of extra virgin olive oil in a large, heavy-bottomed pan over medium heat. While the oil warms, finely dice 1 large brown onion and mince 3 cloves of garlic. When the oil shimmers and a small piece of onion sizzles upon contact, add the diced onion and sauté, stirring frequently with a wooden spoon, until it turns translucent and begins to soften, about 3-4 minutes. Add the minced garlic and continue cooking for another 30 seconds until fragrant, being careful not to let it burn as this will make the dish bitter.

2. Now it's time to build the base flavors of your paella. Add 1 diced red capsicum to the pan along with 1 teaspoon of smoked paprika. Stir continuously for about 1 minute to toast the spices and release their aromatic oils. The kitchen should fill with the warm, smoky scent of the paprika. If the mixture starts to stick to the bottom of the pan, add a splash of water or vegetable broth to deglaze, scraping up any browned bits with your wooden spoon as these add depth of flavor to the dish.

3. The main ingredients come together now. Add 200g of Arborio rice to the pan, stirring to coat each grain with the flavorful oil and spices. This toasting step helps the rice maintain its structure during cooking. Next, add 400g of drained and rinsed chickpeas, distributing them evenly throughout the pan. Sprinkle in a generous pinch of saffron threads (about ½ teaspoon) and pour in 500ml of warm vegetable broth. Gently stir to combine all ingredients, then increase the heat to bring the mixture to a simmer. The liquid should bubble gently around the edges of the pan.

4. Once the paella reaches a simmer, reduce the heat to low and cover the pan with a tight-fitting lid. Set your timer for 15 minutes and resist the temptation to lift the lid - this steam is crucial for even cooking. While the paella simmers, prepare your garnishes: finely chop a generous handful of fresh flat-leaf parsley and set aside. You can also prepare a simple green salad or slice some crusty bread to serve alongside the paella.

5. After 15 minutes, carefully remove the lid and check the rice for doneness. The grains should be tender but still have a slight bite (al dente), and all the liquid should be absorbed. If the rice needs more time, cover and cook for an additional 2-3 minutes. If you notice the rice sticking to the bottom, don't worry - this is normal and actually desirable in traditional paella, creating the prized "socarrat" or crispy bottom layer.

6. The final touches make all the difference. Remove the pan from heat and let it rest, covered, for 5 minutes. This allows the flavors to meld and the rice to settle. When ready to serve, fluff the paella gently with a fork, being careful not to break the rice grains. Sprinkle the chopped parsley over the top for a fresh, vibrant finish. Serve the paella directly from the pan at the table, allowing everyone to admire the beautiful presentation before digging in. The combination of smoky paprika, aromatic saffron, and hearty chickpeas creates a dish that's both comforting and sophisticated.

"""
    return prompt