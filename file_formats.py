import numpy as np
import pandas as pd
import json
from pprint import pprint


with open('recipes.json') as f:
    recipes = json.load(f)
# pprint(recipes)


for recipe in recipes:  # начинаем перебор всех рецептов
    if recipe['id'] == 13121:  # если id текущего рецепта равен искомому
        print(recipe['cuisine'])  # выводим на экран кухню, к которой относится блюдо
        break  # и прерываем цикл, т.к. нужное блюдо уже найдено


last_pos = len(recipes) - 1
recipe = recipes[last_pos]
res = recipe['cuisine']
print(res)
res = len(recipe['ingredients'])
print(res)


for recipe in recipes:
    if recipe['id'] == 17636:
        break
rec_list = recipe['ingredients']
check_list = [
    'tomato sauce',
    'spinach',
    'italian seasoning',
    'broccoli',
    'chopped onion',
    'skinless chicken thighs',
    'chopped green bell pepper'
]
rec_set = set(rec_list)
check_set = set(check_list)
intersection = rec_set.intersection(check_set)
print(intersection)
res_list = list(intersection)
pprint(res_list)


for recipe in recipes:
    if recipe['id'] == 42013:
        break
res = len(recipe['ingredients'])
print(res)


for recipe in recipes:
    if recipe['id'] == 23629:
        break
rec_list = recipe['ingredients']
check_list = [
    'eggs',
    'black beans',
    'black olives',
    'dry vermouth',
    'chicken livers',
    'olive oil'
]
rec_set = set(rec_list)
check_set = set(check_list)
diff = check_set - rec_set
res_list = list(diff)
pprint(res_list)


item_set = set()
for recipe in recipes:
    if recipe['cuisine'] == 'italian':
        rec_list = recipe['ingredients']
        for item in rec_list:
            item_set.add(item)
item_list = list(item_set)
res = len(item_list)
pprint(res)

