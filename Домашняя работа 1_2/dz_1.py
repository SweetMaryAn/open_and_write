import os
from pprint import pprint


path = os.path.join(os.getcwd(), 'recipes.txt')


with open(path, encoding='utf8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp_data = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp_data.append(
                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            )
        cook_book[dish_name] = temp_data
        file.readline()

pprint(cook_book)
