import pandas as pd
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        pd_data_frame = pd.read_csv(source_path)

        self.dishes = set()

        dict_of_dishes = {}

        for dish, price, ingredient, recipe_amount in pd_data_frame.itertuples(
            index=False
        ):
            if dish not in dict_of_dishes:
                dict_of_dishes[dish] = Dish(dish, price)

            ingredient_instance = Ingredient(ingredient)

            dict_of_dishes[dish].add_ingredient_dependency(
                ingredient_instance, recipe_amount
            )

        for dish in dict_of_dishes.values():
            self.dishes.add(dish)
