from lib.backend.recipe import Recipe, add_recipes
from lib.backend.ingredient import Ingredient
import json

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

def test_to_dict():
    r = Recipe(
        "name1",
        ["tag1"],
        [Ingredient("A", 1, "g")],
        [Ingredient("C", 1, "g")],
    )

    expected = {
        "name": "name1",
        "tags": ["tag1"],
        "will_need_ingredients": [
            {"name": "A", "amount": 1, "unit": "g"}
        ],
        "might_need_ingredients": [
            {"name": "C", "amount": 1, "unit": "g"}
        ],
    }
    assert r.to_dict() == expected


def test_from_json(tmp_path):
    source_dict = {
        "name": "name1",
        "tags": ["tag1"],
        "will_need_ingredients": [
            {"name": "A", "amount": 1, "unit": "g"}
        ],
        "might_need_ingredients": [
            {"name": "C", "amount": 1, "unit": "g"}
        ],
    }

    expected = Recipe(
        "name1",
        ["tag1"],
        [Ingredient("A", 1, "g")],
        [Ingredient("C", 1, "g")],
    )

    source_file = tmp_path / "test.json"
    with open(source_file, "w") as f:
        json.dump(source_dict, f)

    r = Recipe.from_json(source_file)
    assert r == expected