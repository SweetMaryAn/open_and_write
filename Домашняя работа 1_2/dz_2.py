import os
from pprint import pprint


with open(os.path.join(os.getcwd(), 'recipes.txt'), encoding='utf8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp_data = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            temp_data.append(
                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            )
        cook_book[dish_name] = temp_data
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dishe in dishes:
        for cook in cook_book:
            if cook == dishe:
                for ingredient in cook_book[cook]:
                    if ingredient['ingredient_name'] not in ingredients.keys():
                        temp_data_1 = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
                        ingredients.setdefault(ingredient['ingredient_name'], temp_data_1)
                    else:
                        ingredients[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    pprint(ingredients)



get_shop_list_by_dishes(['Фахитос', 'Омлет'],1)
