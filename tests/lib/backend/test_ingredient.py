import pytest

from lib.backend.ingredient import Ingredient, add_ingredients_lists


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


def test_add_ingredients_lists():
    l1 = [
        Ingredient("A", 1, "g"),
        Ingredient("B", 1, "g"),
        Ingredient("C", 1, "g"),
        Ingredient("A", 1, "lb"),
    ]

    l2 = [
        Ingredient("A", 5, "g"),
        Ingredient("B", 5, "g"),
        Ingredient("D", 5, "g"),
    ]

    expected = [
        Ingredient("A", 6, "g"),
        Ingredient("B", 6, "g"),
        Ingredient("C", 1, "g"),
        Ingredient("A", 1, "lb"),
        Ingredient("D", 5, "g"),
    ]

    # TODO warn users that they have the same ingredient with different units?
    sort_key = lambda x: (x.name, x.amount, x.unit)  # to ensure consistent ordering
    output = sorted(add_ingredients_lists(l1, l2), key=sort_key)
    expected = sorted(expected, key=sort_key)
    assert output == expected
