from dataclasses import dataclass, field
from .ingredient import add_ingredients_lists, Ingredient
from pathlib import Path
import json


@dataclass
class Recipe:
    name: str
    tags: list[str]
    will_need_ingredients: list[Ingredient]
    might_need_ingredients: list[Ingredient]

    def to_dict(self):
        return {
            "name": self.name,
            "tags": self.tags,
            "will_need_ingredients": [
                ing.to_dict() for ing in self.will_need_ingredients
            ],
            "might_need_ingredients": [
                ing.to_dict() for ing in self.might_need_ingredients
            ],
        }

    @classmethod
    def from_json(cls, f: str | Path) -> "Recipe":
        with open(f, "r") as file:
            data = json.load(file)
        return cls(
            data["name"],
            data["tags"],
            [Ingredient(**ing) for ing in data["will_need_ingredients"]],
            [Ingredient(**ing) for ing in data["might_need_ingredients"]],
        )


def add_recipes(recipe_1: Recipe, recipe_2: Recipe, new_name: str = "") -> Recipe:
    """
    Add two recipes together, combining ingredients where they are the same.
    :param recipe_1:    the first recipe
    :param recipe_2:    the second recipe
    :param new_name:    the name of the new recipe
    :return:            the combined recipe
    """

    return Recipe(
        name=new_name,
        tags=recipe_1.tags + recipe_2.tags,
        will_need_ingredients=add_ingredients_lists(
            recipe_1.will_need_ingredients, recipe_2.will_need_ingredients
        ),
        might_need_ingredients=add_ingredients_lists(
            recipe_1.might_need_ingredients, recipe_2.might_need_ingredients
        ),
    )
