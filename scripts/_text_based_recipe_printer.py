from lib.backend.recipe import load_all_recipes, Recipe, sum_recipes

THIS_WEEKS_RECIPES = [
    "Chicken and Rice Peri Peri",
    "Healthy Fish and Chips",
    #"Salmon with Black Beans",
    "Vegan Biryani",
]


def recipe_to_text(recipe: Recipe) -> str:
    def ingredients_to_string(ingredients, indent=4):
        return f"\n{' ' * indent}".join([f"{ing.name}: {ing.amount} {ing.unit if ing.unit else ''}" for ing in ingredients])

    return f"""
    {recipe.name}
        Will Need Ingredients: 
            {ingredients_to_string(sorted(recipe.will_need_ingredients, key=lambda ing: ing.name), indent=4*3)}
        Might Need Ingredients: 
            {ingredients_to_string(sorted(recipe.might_need_ingredients, key=lambda ing: ing.name), indent=4*3)}
    """


def main():
    all_recipes = load_all_recipes()
    this_weeks_recipes = [all_recipes[recipe] for recipe in THIS_WEEKS_RECIPES]
    meals_str = "Meals:\n     "+"\n     ".join([recipe.name for recipe in this_weeks_recipes])+ "\n"
    combined_recipe = sum_recipes(this_weeks_recipes, meals_str)
    print(recipe_to_text(combined_recipe))
    # write it to a file
    with open("./this_weeks_recipes.txt", "w") as file:
        file.write(recipe_to_text(combined_recipe))

if __name__ == "__main__":
    main()
