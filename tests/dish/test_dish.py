import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    dish = Dish("prato teste", 11.5)
    dish_2 = Dish("prato teste", 11.5)
    dish_3 = Dish("prato teste 2", 20)

    assert dish.name == "prato teste"
    assert dish.price == 11.5

    ingredient_base = Ingredient("bacon")
    dish.add_ingredient_dependency(ingredient_base, 2)

    assert dish.get_ingredients() == {ingredient_base}

    assert dish == dish_2

    assert dish.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    assert hash(dish) != hash(dish_3)

    assert hash(dish) == hash(dish_2)

    assert repr(dish) == "Dish('prato teste', R$11.50)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("prato", "d")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("prato", -10.5)
