from lib.backend.recipe import Recipe
from lib.backend.ingredient import Ingredient
from pathlib import Path
import json


def _ingredient_from_input(user_input: str) -> Ingredient:
    values = user_input.split(",")
    name = values[0].strip()
    if len(values) == 1:
        return Ingredient(name)

    amount = float(values[1])
    if len(values) == 2:
        return Ingredient(name, amount)

    unit = values[2].strip()
    return Ingredient(name, amount, unit)


def main():
    # get user input for recipe name
    recipe_name = input("Enter recipe name: ")
    # get user input for recipe tags use "next" to stop
    recipe_tags = []
    while (tag := input("Enter recipe tag (hit enter to move on): ")) != "":
        recipe_tags.append(tag)

    # get user input for ingredients
    will_need_ingredients = []
    print("Enter 'will need' ingredients")
    print(
        "comma separated values for name, amount, unit (amount and unit are optional)"
    )
    while (user_input := input("Enter ingredient (hit enter to move on): ")) != "":
        will_need_ingredients.append(_ingredient_from_input(user_input))

    # get user input for optional ingredients
    might_need_ingredients = []
    print("Enter 'might need' ingredients")
    print(
        "comma separated values for name, amount, unit (amount and unit are optional)"
    )
    while (user_input := input("Enter ingredient (hit enter to move on): ")) != "":
        might_need_ingredients.append(_ingredient_from_input(user_input))

    # create recipe object
    recipe = Recipe(
        recipe_name, recipe_tags, will_need_ingredients, might_need_ingredients
    )

    # get filename
    default_filename = recipe_name.replace(" ", "_").lower()
    filename = (
        input(f"Enter filename (default: {default_filename}): ") or default_filename
    )
    filename = f"{filename}.json"

    # write recipe to json file
    file_path = Path(__file__).parent.parent / "recipes" / filename
    with open(file_path, "w") as f:
        json.dump(recipe.to_dict(), f, indent=4)

    print(f"Recipe saved to {file_path}")


if __name__ == "__main__":
    main()
