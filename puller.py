from bs4 import BeautifulSoup
import os
import logging
from pathlib import Path
from mysql.connector import Error



def pull_ingredients(folder):
    recipe_folder = Path.cwd() / folder
    recipe_list = []
    for file in os.listdir(recipe_folder):

        recipe_path = recipe_folder / Path(file)
        recipe = open(recipe_path, encoding="utf-8")
        try:
            soup = BeautifulSoup(recipe, 'html.parser')
            ingredients = soup.select('p[itemprop="recipeIngredient"]')
            recipe_ingredient_dict = {recipe_path.stem: ''}
            for ingredient in ingredients:
                recipe_ingredient_dict[recipe_path.stem] += f'\n- {ingredient.text}'
            recipe_list.append(recipe_ingredient_dict)
            recipe.close()
        except (AttributeError, KeyError) as ex:
            logging.exception("message")


    return recipe_list


def main():
    print(pull_ingredients('recipes'))

if __name__ == '__main__':
    main()