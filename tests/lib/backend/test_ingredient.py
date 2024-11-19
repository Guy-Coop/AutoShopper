import pytest

from lib.backend.ingredient import Ingredient


@pytest.mark.parametrize(
    "ingredient1, ingredient2, expected",
    [
        pytest.param(
            Ingredient("Chicken Breast", 200, "g"),
            Ingredient("Chicken Breast", 200, "g"),
            Ingredient("Chicken Breast", 400, "g"),
            id="int_g",
        ),
        pytest.param(
            Ingredient("Chicken Breast", 0.5, "lb"),
            Ingredient("Chicken Breast", 0.5, "lb"),
            Ingredient("Chicken Breast", 0.75, "lb"),
            id="float_lb",
        ),
    ],
)
def test_add_valid(ingredient1, ingredient2, expected):
    assert ingredient1 + ingredient2 == expected


@pytest.mark.parametrize(
    "ingredient1, ingredient2",
    [
        pytest.param(
            Ingredient("Chicken Breast", 200, "g"),
            Ingredient("Rice", 200, "g"),
            id="different_names",
        ),
        pytest.param(
            Ingredient("Chicken Breast", 200, "g"),
            Ingredient("Chicken Breast", 200, "lb"),
            id="different_units",
        ),
    ],
)
def test_add_invalid(ingredient1, ingredient2):
    with pytest.raises(ValueError):
        ingredient1 + ingredient2