from dataclasses import dataclass, field

from lib.backend.ingredient import Ingredient

@dataclass
class Recipe:
    name: str
    tags: list[str]
    will_need_ingredients: list[Ingredient]
    might_need_ingredients: list[Ingredient]


def add_recipes(recipe_1: Recipe, recipe_2: Recipe, new_name: str = "") -> Recipe:
