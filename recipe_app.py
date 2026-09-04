import csv
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


import tkinter as tk
from tkinter import messagebox, ttk


class RecipeForm(tk.Toplevel):
    def __init__(self, parent, categories, recipe=None, on_save=None, on_delete=None):
        super().__init__(parent)
        self.on_save = on_save
        self.on_delete = on_delete
        self.recipe_id = recipe[0] if recipe else None
        self.title("Edit recipe" if recipe else "Add recipe")
        self.geometry("500x560")
        self.resizable(False, False)
        self.configure(bg="#f7f8fa")
        self.transient(parent)
        self.grab_set()

        content = tk.Frame(self, bg="#f7f8fa", padx=28, pady=24)
        content.pack(fill="both", expand=True)
        tk.Label(content, text=self.title(), font=("Georgia", 22, "bold"),
                 bg="#f7f8fa", fg="#17212b").pack(anchor="w")
        tk.Label(content, text="Keep the details clear and easy to cook from.",
                 font=("Segoe UI", 10), bg="#f7f8fa", fg="#697586").pack(anchor="w", pady=(4, 20))

        self.fields = {}
        values = [("Recipe name", recipe[1] if recipe else ""),
                  ("Category", recipe[2] if recipe else ""),
                  ("Ingredients", recipe[3] if recipe else ""),
                  ("Method", recipe[4] if recipe else "")]
        for label, value in values:
            tk.Label(content, text=label.upper(), font=("Segoe UI", 9, "bold"),
                     bg="#f7f8fa", fg="#697586").pack(anchor="w", pady=(0, 5))
            if label in ("Ingredients", "Method"):
                field = tk.Text(content, height=4, font=("Segoe UI", 10), relief="flat",
                                bg="white", fg="#17212b", padx=10, pady=8)
                field.insert("1.0", value)
            elif label == "Category":
                field = ttk.Combobox(content, values=categories, state="readonly", font=("Segoe UI", 10))
                field.set(value)
            else:
                field = ttk.Entry(content, font=("Segoe UI", 10))
                field.insert(0, value)
            field.pack(fill="x", pady=(0, 14))
            self.fields[label] = field

        buttons = tk.Frame(content, bg="#f7f8fa")
        buttons.pack(fill="x", pady=(4, 0))
        ttk.Button(buttons, text="Cancel", command=self.destroy).pack(side="right", padx=(8, 0))
        ttk.Button(buttons, text="Save recipe", style="Accent.TButton", command=self.save).pack(side="right")
        if self.recipe_id:
            ttk.Button(buttons, text="Delete recipe", style="Danger.TButton", command=self.delete).pack(side="left")
        self.fields["Recipe name"].focus_set()

    def save(self):
        values = []
        for label in ("Recipe name", "Category", "Ingredients", "Method"):
            field = self.fields[label]
            values.append(field.get("1.0", "end-1c").strip() if isinstance(field, tk.Text) else field.get().strip())
        if not all(values):
            messagebox.showwarning("Missing details", "Please complete every field.", parent=self)
            return
        self.on_save(self.recipe_id, values)
        self.destroy()

    def delete(self):
        recipe_name = self.fields["Recipe name"].get().strip()
        if messagebox.askyesno("Delete recipe", f"Delete {recipe_name}?", parent=self):
            self.on_delete(self.recipe_id)
            self.destroy()


class RecipeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recipe Cabinet")
        self.geometry("1100x700")
        self.minsize(850, 560)
        self.configure(bg="#f7f8fa")
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.setup_styles()
        self.build_ui()
        self.refresh()

    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=(12, 8), background="#e8edf2", foreground="#17212b", borderwidth=0)
        style.map("TButton", background=[("active", "#d8e1e9")])
        style.configure("Accent.TButton", background="#d86b45", foreground="white")
        style.map("Accent.TButton", background=[("active", "#bc5434")])
        style.configure("Danger.TButton", background="#f3d9d5", foreground="#a33b2e")
        style.map("Danger.TButton", background=[("active", "#e9beb7")])
        style.configure("Treeview", rowheight=42, font=("Segoe UI", 10), background="white", fieldbackground="white", foreground="#24313d", borderwidth=0)
        style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"), background="#edf1f4", foreground="#52606d", relief="flat", padding=8)
        style.map("Treeview", background=[("selected", "#f6d8ca")], foreground=[("selected", "#17212b")])

    def build_ui(self):
        sidebar = tk.Frame(self, bg="#17212b", width=230)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)
        tk.Label(sidebar, text="RECIPE\nCABINET", justify="left", font=("Georgia", 25, "bold"),
                 bg="#17212b", fg="#f7c7a8").pack(anchor="w", padx=28, pady=(38, 8))
        tk.Label(sidebar, text="Your everyday collection", font=("Segoe UI", 10),
                 bg="#17212b", fg="#aeb9c4").pack(anchor="w", padx=29)
        self.stats = tk.Label(sidebar, text="", justify="left", font=("Segoe UI", 10),
                              bg="#17212b", fg="#d5dde4")
        self.stats.pack(anchor="w", padx=29, pady=(55, 0))

        main = tk.Frame(self, bg="#f7f8fa", padx=34, pady=30)
        main.pack(side="left", fill="both", expand=True)
        top = tk.Frame(main, bg="#f7f8fa")
        top.pack(fill="x")
        tk.Label(top, text="All recipes", font=("Georgia", 27, "bold"), bg="#f7f8fa", fg="#17212b").pack(side="left")
        ttk.Button(top, text="Export CSV", command=self.export_csv).pack(side="right", padx=(0, 10))
        ttk.Button(top, text="+  Add recipe", style="Accent.TButton", command=self.add).pack(side="right")

        controls = tk.Frame(main, bg="#f7f8fa")
        controls.pack(fill="x", pady=(24, 18))
        self.search = ttk.Entry(controls, font=("Segoe UI", 11))
        self.search.insert(0, "Search recipes...")
        self.search.pack(side="left", fill="x", expand=True, ipady=7)
        self.search.bind("<FocusIn>", self.clear_search_hint)
        self.search.bind("<KeyRelease>", lambda event: self.refresh())
        self.category = ttk.Combobox(controls, state="readonly", width=17, font=("Segoe UI", 10))
        self.category.pack(side="left", padx=(12, 0), ipady=6)
        self.category.bind("<<ComboboxSelected>>", lambda event: self.refresh())

        table_frame = tk.Frame(main, bg="white")
        table_frame.pack(fill="both", expand=True)
        columns = ("name", "category", "ingredients", "method")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        self.table.heading("name", text="RECIPE")
        self.table.heading("category", text="CATEGORY")
        self.table.heading("ingredients", text="INGREDIENTS")
        self.table.heading("method", text="METHOD")
        self.table.column("name", width=220, anchor="w")
        self.table.column("category", width=125, anchor="w")
        self.table.column("ingredients", width=330, anchor="w")
        self.table.column("method", width=380, anchor="w")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.table.bind("<<TreeviewSelect>>", self.show_selected)
        self.table.bind("<Double-1>", lambda event: self.edit())

        self.details = tk.Label(main, text="Select a recipe to see the method.", justify="left", anchor="nw",
                                font=("Segoe UI", 10), bg="#f7f8fa", fg="#697586", wraplength=800)
        self.details.pack(fill="x", pady=(18, 0))
        actions = tk.Frame(main, bg="#f7f8fa")
        actions.pack(fill="x", pady=(10, 0))
        ttk.Button(actions, text="Edit selected", command=self.edit).pack(side="left")
        ttk.Button(actions, text="Delete selected", command=self.delete).pack(side="left", padx=8)

    def clear_search_hint(self, event):
        if self.search.get() == "Search recipes...":
            self.search.delete(0, "end")

    def refresh(self):
        query = self.search.get().strip().lower()
        if query == "search recipes...":
            query = ""
        selected_category = self.category.get()
        cursor.execute("SELECT * FROM recipes ORDER BY name")
        rows = cursor.fetchall()
        categories = sorted({row[2] for row in rows})
        self.category["values"] = ["All categories"] + categories
        if selected_category not in self.category["values"]:
            self.category.set("All categories")
        visible = [row for row in rows if (not query or query in " ".join(map(str, row[1:])).lower())
                   and (self.category.get() == "All categories" or row[2] == self.category.get())]
        self.table.delete(*self.table.get_children())
        for row in visible:
            self.table.insert("", "end", iid=str(row[0]), values=(row[1], row[2], row[3], row[4]))
        self.stats.config(text=f"{len(rows)} recipes\n\n{len(categories)} categories")
        self.details.config(text=f"Showing {len(visible)} recipe{'s' if len(visible) != 1 else ''}")

    def selected(self):
        selection = self.table.selection()
        if not selection:
            messagebox.showinfo("Select a recipe", "Choose a recipe first.", parent=self)
            return None
        cursor.execute("SELECT * FROM recipes WHERE id = ?", (selection[0],))
        return cursor.fetchone()

    def show_selected(self, event=None):
        recipe = self.selected_row()
        if recipe:
            self.details.config(text=f"{recipe[1]}  |  {recipe[2]}\n\n{recipe[4]}", fg="#24313d")

    def selected_row(self):
        selection = self.table.selection()
        if not selection:
            return None
        cursor.execute("SELECT * FROM recipes WHERE id = ?", (selection[0],))
        return cursor.fetchone()

    def add(self):
        RecipeForm(self, self.get_categories(), on_save=self.save_recipe)

    def edit(self):
        recipe = self.selected()
        if recipe:
            RecipeForm(self, self.get_categories(), recipe, self.save_recipe, self.delete_recipe)

    def get_categories(self):
        cursor.execute("SELECT DISTINCT category FROM recipes WHERE category IS NOT NULL AND category != '' ORDER BY category")
        return [row[0] for row in cursor.fetchall()]

    def save_recipe(self, recipe_id, values):
        if recipe_id:
            cursor.execute("UPDATE recipes SET name = ?, category = ?, ingredients = ?, method = ? WHERE id = ?", (*values, recipe_id))
        else:
            cursor.execute("INSERT INTO recipes (name, category, ingredients, method) VALUES (?, ?, ?, ?)", values)
        conn.commit()
        self.refresh()

    def delete(self):
        recipe = self.selected()
        if recipe and messagebox.askyesno("Delete recipe", f"Delete {recipe[1]}?", parent=self):
            self.delete_recipe(recipe[0])

    def delete_recipe(self, recipe_id):
        cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
        conn.commit()
        self.refresh()

    def export_csv(self):
        cursor.execute("SELECT id, name, category, ingredients, method FROM recipes ORDER BY id ASC")
        rows = cursor.fetchall()
        with open("recipes.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(("ID", "Name", "Category", "Ingredients", "Method"))
            writer.writerows(rows)
        messagebox.showinfo("Export complete", f"Exported {len(rows)} recipes to recipes.csv.", parent=self)

    def close(self):
        conn.close()
        self.destroy()


if __name__ == "__main__":
    RecipeApp().mainloop()
        