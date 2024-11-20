from dataclasses import dataclass
from typing import Optional


@dataclass
class Ingredient:
    name: str
    amount: float = 1
    unit: Optional[str] = None

    def __post_init__(self):
        # ensure consistent capitalisation
        self.name = self.name.title()

    def __add__(self, other):
        if not isinstance(other, Ingredient):
            raise ValueError(f"Cannot add {self.__class__.__name__} and {type(other)}")
        if self.name != other.name:
            raise ValueError(f"Cannot add {self.name} and {other.name}")
        if self.unit != other.unit:
            raise ValueError(f"Cannot add {self.unit} and {other.unit}")

        return Ingredient(self.name, self.amount + other.amount, self.unit)


def add_ingredients_lists(
    ingredients1: list[Ingredient], ingredients2: list[Ingredient]
) -> list[Ingredient]:
    """
    Add two lists of ingredients together, combining amounts where ingredients are the same.
    :param ingredients1:    the first list of ingredients
    :param ingredients2:    the second list of ingredients
    :return:                the combined list of ingredients
    """

    combined = []
    ingredients1_dict = {(ing.name, ing.unit): ing for ing in ingredients1}
    ingredients2_dict = {(ing.name, ing.unit): ing for ing in ingredients2}
    shared_keys = set(ingredients1_dict.keys()) & set(ingredients2_dict.keys())

    for key in shared_keys:
        combined.append(ingredients1_dict[key] + ingredients2_dict[key])

    for key in set(ingredients1_dict.keys()) - shared_keys:
        combined.append(ingredients1_dict[key])

    for key in set(ingredients2_dict.keys()) - shared_keys:
        combined.append(ingredients2_dict[key])

    return combined
