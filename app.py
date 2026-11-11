from version import __version__

from flask import Flask, render_template, request

from recipes import suggest_recipes

from shopping_list import ShoppingList 

app = Flask(__name__)

# Все продукты, которые могут быть в холодильнике (для чекбоксов)
ALL_INGREDIENTS = sorted(
    {
        ing
        for r in __import__("recipes").RECIPES
        for ing in r["ingredients"]
    }
)


@app.route("/", methods=["GET", "POST"])
def index():
    selected = []
    suggestions = []
    if request.method == "POST":
        selected = request.form.getlist("ingredients")
        suggestions = suggest_recipes(selected, top_n=3)
    return render_template(
        "index.html",
        all_ingredients=ALL_INGREDIENTS,
        selected=selected,
        suggestions=suggestions,
    )


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/version")
def version():
    return {"version": __version__}

@app.route("/shopping-list", methods=["POST"])
def shopping_list_endpoint():
    data = request.get_json(silent=True) or {}
    suggestions = data.get("suggestions", [])
    sl = ShoppingList.from_recipe_suggestions(suggestions)
    return sl.to_dict()


if __name__ == "__main__":
    app.run(debug=True)
