
# Recipe Cabinet

A desktop recipe manager built with Python, Tkinter, and SQLite. Comes pre-loaded with 50 recipes across cakes, cupcakes, cookies, bread, and pastries.

## Features

- Browse, search, and filter recipes by category
- Add, edit, and delete recipes (name, category, ingredients, method)
- View full recipe details in-app
- Export the recipe collection to CSV
- Auto-seeds the database with 50 starter recipes on first run

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

No external dependencies — uses only the standard library (`sqlite3`, `csv`, `tkinter`).

## Getting Started

```bash
git clone https://github.com/your-username/recipe-cabinet.git
cd recipe-cabinet
python recipe_cabinet.py
```

A `recipes.db` SQLite database is created automatically in the project folder on first launch.

## Usage

- **Add a recipe:** Click "+ Add recipe" and fill in the form
- **Edit a recipe:** Double-click a row, or select it and click "Edit selected"
- **Delete a recipe:** Select a recipe and click "Delete selected" (or delete from the edit form)
- **Search:** Type in the search bar to filter by name, category, ingredients, or method
- **Filter by category:** Use the category dropdown
- **Export:** Click "Export CSV" to save all recipes to `recipes.csv`

## Project Structure

```
recipe-cabinet/
├── recipe_cabinet.py   # Main application (database setup + Tkinter UI)
├── recipes.db          # SQLite database (created on first run)
└── recipes.csv         # Generated on export
```



