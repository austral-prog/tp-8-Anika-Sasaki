from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    ingredients = set()
    for elem in dish_ingredients:
        if elem not in ingredients:
            ingredients.add(elem)
    clean = (dish_name, ingredients)
    return clean

def check_drinks(drink_name, drink_ingredients):
    for alcohol in ALCOHOLS:
        if alcohol in drink_ingredients:
            return str(drink_name) + " " + "Cocktail"
    return str(drink_name) + " " + "Mocktail"
