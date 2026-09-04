import sqlite3

# Connect to database
conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()


# Create recipes table
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    ingredients TEXT,
    method TEXT
)
""")


# Initial 50 recipes
recipes = [

    # CAKES
    ("Vanilla Cake", "Cake", "Flour, sugar, eggs, milk, butter, vanilla, baking powder",
     "Mix ingredients and bake at 180°C for 30 minutes."),

    ("Chocolate Cake", "Cake", "Flour, sugar, cocoa powder, eggs, milk, oil",
     "Mix ingredients and bake at 180°C for 35 minutes."),

    ("Red Velvet Cake", "Cake", "Flour, sugar, eggs, cocoa, buttermilk, red colouring",
     "Mix ingredients and bake at 180°C for 30 minutes."),

    ("Carrot Cake", "Cake", "Flour, sugar, carrots, eggs, oil, cinnamon",
     "Mix ingredients and bake at 180°C for 40 minutes."),

    ("Lemon Cake", "Cake", "Flour, sugar, eggs, lemon juice, milk, butter",
     "Mix ingredients and bake at 180°C for 35 minutes."),

    ("Banana Cake", "Cake", "Flour, sugar, bananas, eggs, butter, baking powder",
     "Mash bananas, mix ingredients and bake at 180°C for 35 minutes."),

    ("Strawberry Cake", "Cake", "Flour, sugar, strawberries, eggs, milk, butter",
     "Mix ingredients and bake at 180°C for 35 minutes."),

    ("Coffee Cake", "Cake", "Flour, sugar, eggs, milk, butter, coffee",
     "Mix ingredients and bake at 180°C for 35 minutes."),

    ("Black Forest Cake", "Cake", "Flour, sugar, cocoa, eggs, milk, cherries, cream",
     "Bake chocolate cake and decorate with cream and cherries."),

    ("Fruit Cake", "Cake", "Flour, sugar, eggs, dried fruits, butter, cinnamon",
     "Mix ingredients and bake at 180°C for 45 minutes."),


    # CUPCAKES
    ("Vanilla Cupcakes", "Cupcake", "Flour, sugar, eggs, milk, butter, vanilla",
     "Mix ingredients and bake at 180°C for 20 minutes."),

    ("Chocolate Cupcakes", "Cupcake", "Flour, sugar, cocoa, eggs, milk, oil",
     "Mix ingredients and bake at 180°C for 20 minutes."),

    ("Red Velvet Cupcakes", "Cupcake", "Flour, sugar, cocoa, eggs, buttermilk, red colouring",
     "Mix ingredients and bake at 180°C for 20 minutes."),

    ("Strawberry Cupcakes", "Cupcake", "Flour, sugar, strawberries, eggs, milk, butter",
     "Mix ingredients and bake at 180°C for 20 minutes."),

    ("Lemon Cupcakes", "Cupcake", "Flour, sugar, eggs, lemon juice, butter",
     "Mix ingredients and bake at 180°C for 20 minutes."),

    ("Banana Cupcakes", "Cupcake", "Flour, sugar, bananas, eggs, butter",
     "Mash bananas, mix ingredients and bake at 180°C for 20 minutes."),

    ("Coffee Cupcakes", "Cupcake", "Flour, sugar, eggs, milk, butter, coffee",
     "Mix ingredients and bake at 180°C for 20 minutes."),

    ("Coconut Cupcakes", "Cupcake", "Flour, sugar, eggs, coconut, milk, butter",
     "Mix ingredients and bake at 180°C for 20 minutes."),

    ("Carrot Cupcakes", "Cupcake", "Flour, sugar, carrots, eggs, oil, cinnamon",
     "Mix ingredients and bake at 180°C for 20 minutes."),

    ("Chocolate Chip Cupcakes", "Cupcake",
     "Flour, sugar, eggs, milk, butter, chocolate chips",
     "Mix ingredients, add chocolate chips and bake at 180°C for 20 minutes."),


    # COOKIES
    ("Chocolate Chip Cookies", "Cookie",
     "Flour, sugar, butter, eggs, chocolate chips",
     "Mix ingredients, form cookies and bake at 180°C for 12 minutes."),

    ("Sugar Cookies", "Cookie",
     "Flour, sugar, butter, eggs, vanilla",
     "Mix ingredients, shape cookies and bake at 180°C for 10 minutes."),

    ("Oatmeal Cookies", "Cookie",
     "Oats, flour, sugar, butter, eggs",
     "Mix ingredients, shape cookies and bake at 180°C for 12 minutes."),

    ("Peanut Butter Cookies", "Cookie",
     "Peanut butter, flour, sugar, eggs, butter",
     "Mix ingredients and bake at 180°C for 12 minutes."),

    ("Coconut Cookies", "Cookie",
     "Flour, sugar, coconut, butter, eggs",
     "Mix ingredients and bake at 180°C for 12 minutes."),

    ("Ginger Cookies", "Cookie",
     "Flour, sugar, butter, ginger, eggs",
     "Mix ingredients and bake at 180°C for 12 minutes."),

    ("Shortbread Cookies", "Cookie",
     "Flour, sugar, butter",
     "Mix ingredients, shape cookies and bake at 170°C for 15 minutes."),

    ("Lemon Cookies", "Cookie",
     "Flour, sugar, butter, eggs, lemon",
     "Mix ingredients and bake at 180°C for 12 minutes."),

    ("Double Chocolate Cookies", "Cookie",
     "Flour, sugar, cocoa, butter, eggs, chocolate",
     "Mix ingredients and bake at 180°C for 12 minutes."),

    ("Almond Cookies", "Cookie",
     "Flour, sugar, almonds, butter, eggs",
     "Mix ingredients and bake at 180°C for 12 minutes."),


    # BREAD
    ("White Bread", "Bread",
     "Flour, yeast, sugar, salt, water, butter",
     "Mix dough, let it rise and bake at 180°C for 30 minutes."),

    ("Brown Bread", "Bread",
     "Whole wheat flour, yeast, salt, water, sugar",
     "Knead dough, let it rise and bake at 180°C for 35 minutes."),

    ("Banana Bread", "Bread",
     "Flour, bananas, sugar, eggs, butter",
     "Mix ingredients and bake at 180°C for 45 minutes."),

    ("Garlic Bread", "Bread",
     "Bread flour, yeast, garlic, butter, parsley",
     "Prepare dough, add garlic butter and bake at 180°C."),

    ("Cinnamon Bread", "Bread",
     "Flour, yeast, sugar, cinnamon, milk, butter",
     "Prepare dough, add cinnamon and bake at 180°C for 35 minutes."),

    ("Cheese Bread", "Bread",
     "Flour, yeast, milk, butter, cheese",
     "Prepare dough, add cheese and bake at 180°C for 30 minutes."),

    ("Milk Bread", "Bread",
     "Flour, milk, sugar, yeast, butter",
     "Knead dough, let it rise and bake at 180°C for 30 minutes."),

    ("French Bread", "Bread",
     "Flour, yeast, salt, water",
     "Knead dough, allow it to rise and bake at 200°C."),

    ("Dinner Rolls", "Bread",
     "Flour, yeast, milk, sugar, butter",
     "Make dough, form rolls and bake at 180°C for 20 minutes."),

    ("Focaccia", "Bread",
     "Flour, yeast, olive oil, salt, herbs",
     "Prepare dough, add herbs and oil, then bake at 200°C."),


    # PASTRIES
    ("Apple Pie", "Pastry",
     "Flour, butter, apples, sugar, cinnamon",
     "Prepare pastry, add apples and bake at 180°C for 40 minutes."),

    ("Fruit Tart", "Pastry",
     "Flour, butter, sugar, eggs, mixed fruits",
     "Prepare pastry, add fruit and bake at 180°C."),

    ("Croissant", "Pastry",
     "Flour, butter, yeast, milk, sugar",
     "Prepare dough, fold with butter, shape and bake at 200°C."),

    ("Cinnamon Rolls", "Pastry",
     "Flour, yeast, sugar, cinnamon, butter, milk",
     "Prepare dough, add cinnamon filling and bake at 180°C."),

    ("Danish Pastry", "Pastry",
     "Flour, butter, yeast, sugar, milk, eggs",
     "Prepare laminated dough, shape and bake at 190°C."),

    ("Blueberry Muffins", "Pastry",
     "Flour, sugar, blueberries, eggs, milk, butter",
     "Mix ingredients, add blueberries and bake at 180°C for 25 minutes."),

    ("Apple Turnovers", "Pastry",
     "Puff pastry, apples, sugar, cinnamon",
     "Fill pastry with apples and bake at 190°C for 20 minutes."),

    ("Cream Puffs", "Pastry",
     "Flour, eggs, butter, water, cream",
     "Prepare pastry, bake until golden and fill with cream."),

    ("Chocolate Eclairs", "Pastry",
     "Flour, eggs, butter, water, chocolate, cream",
     "Bake pastry shells, fill with cream and cover with chocolate."),

    ("Puff Pastry", "Pastry",
     "Flour, butter, water, salt",
     "Prepare laminated dough and bake at 200°C until golden.")
]


# Add the 50 recipes 
cursor.execute("SELECT COUNT(*) FROM recipes")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany("""
        INSERT INTO recipes (name, category, ingredients, method)
        VALUES (?, ?, ?, ?)
    """, recipes)

    conn.commit()
    print("50 recipes added successfully!")


# ADD RECIPE
def add_recipe():
    name = input("Recipe name: ")
    category = input("Category: ")
    ingredients = input("Ingredients: ")
    method = input("Method: ")

    cursor.execute("""
        INSERT INTO recipes (name, category, ingredients, method)
        VALUES (?, ?, ?, ?)
    """, (name, category, ingredients, method))

    conn.commit()
    print("Recipe added successfully!")


# VIEW ALL RECIPES
def view_recipes():
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()

    print("\n--- ALL RECIPES ---")

    for recipe in recipes:
        print("\nID:", recipe[0])
        print("Name:", recipe[1])
        print("Category:", recipe[2])
        print("Ingredients:", recipe[3])
        print("Method:", recipe[4])


# UPDATE RECIPE
def update_recipe():
    recipe_id = input("Enter recipe ID to update: ")

    name = input("New recipe name: ")
    category = input("New category: ")
    ingredients = input("New ingredients: ")
    method = input("New method: ")

    cursor.execute("""
        UPDATE recipes
        SET name = ?, category = ?, ingredients = ?, method = ?
        WHERE id = ?
    """, (name, category, ingredients, method, recipe_id))

    conn.commit()
    print("Recipe updated successfully!")


# DELETE RECIPE
def delete_recipe():
    recipe_id = input("Enter recipe ID to delete: ")

    cursor.execute("""
        DELETE FROM recipes
        WHERE id = ?
    """, (recipe_id,))

    conn.commit()
    print("Recipe deleted successfully!")


# MAIN MENU
while True:

    print("\n====================")
    print("    RECIPE APP")
    print("====================")

    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. Update Recipe")
    print("4. Delete Recipe")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_recipe()

    elif choice == "2":
        view_recipes()

    elif choice == "3":
        update_recipe()

    elif choice == "4":
        delete_recipe()

    elif choice == "5":
        conn.close()
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")