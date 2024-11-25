from lib.backend.recipe import load_all_recipes, Recipe, sum_recipes

THIS_WEEKS_RECIPES = [
    "Chicken and Rice Peri Peri",
    "Salmon with Black Beans",
]


def recipe_to_text(recipe: Recipe) -> str:
    """
    Convert a recipe to a string.
    :param recipe:    the recipe
    :return:            the recipe as a string
    """

    def ingredients_to_string(ingredients, indent=4):
        return f"\n{' ' * indent}".join([f"{ing.name}: {ing.amount} {ing.unit if ing.unit else ''}" for ing in ingredients])

    return f"""
    {recipe.name}
        Will Need Ingredients: 
            {ingredients_to_string(recipe.will_need_ingredients, indent=4*3)}
        Might Need Ingredients: 
            {ingredients_to_string(recipe.might_need_ingredients, indent=4*3)}
    """


def main():
    all_recipes = load_all_recipes()
    this_weeks_recipes = [all_recipes[recipe] for recipe in THIS_WEEKS_RECIPES]
    combined_recipe = sum_recipes(this_weeks_recipes, "This Weeks Recipes")
    print(recipe_to_text(combined_recipe))
    # write it to a file
    with open("./this_weeks_recipes.txt", "w") as file:
        file.write(recipe_to_text(combined_recipe))

if __name__ == "__main__":
    main()
