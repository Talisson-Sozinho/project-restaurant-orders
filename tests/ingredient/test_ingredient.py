from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    ingredient = Ingredient('bacon')
    ingredient_2 = Ingredient('bacon')
    ingredient_3 = Ingredient('manteiga')

    assert ingredient.restrictions == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED
    }
    assert ingredient == ingredient_2
    assert hash(ingredient) == ingredient.__hash__()
    assert hash(ingredient) != hash(ingredient_3)
    assert ingredient.name == 'bacon'
    assert repr(ingredient) == "Ingredient('bacon')"
