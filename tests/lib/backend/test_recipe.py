from lib.backend.recipe import Recipe, add_recipes
from lib.backend.ingredient import Ingredient


def test_add_recipe():
    r1 = Recipe(
        "name1",
        ["tag1"],
        [Ingredient("A", 1, "g")],
        [Ingredient("C", 1, "g")],
    )
    r2 = Recipe(
        "name2",
        ["tag2"],
        [Ingredient("A", 5, "g"), Ingredient("B", 2)],
        [Ingredient("D", 1)],
    )

    expected = Recipe(
        "name3",
        ["tag1", "tag2"],
        [Ingredient("A", 6, "g"), Ingredient("B", 2)],
        [Ingredient("C", 1, "g"), Ingredient("D", 1)],
    )
    result = add_recipes(r1, r2, "name3")
    assert result == expected
