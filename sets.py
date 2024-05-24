from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    ingredients = set()
    for elem in dish_ingredients:
        if elem not in ingredients:
            ingredients.add(elem)
    clean = (dish_name, ingredients)
    return clean

def check_drinks(drink_name, drink_ingredients):
    if ALCOHOLS in drink_ingredients:
        return str(drink_name) + " " + "Mocktail"
    else:
        return str(drink_name) + " " + "Cocktail"
