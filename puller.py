from bs4 import BeautifulSoup
import os
from pathlib import Path
from mysql.connector import Error



def pull_ingredients(folder):
    recipe_folder = Path.cwd() / folder
    recipe_list = []
    for file in os.listdir(recipe_folder):

        recipe_path = recipe_folder / Path(file)
        recipe = open(recipe_path)
        try:
            soup = BeautifulSoup(recipe, 'html.parser')
            ingredients = soup.select('p[itemprop="recipeIngredient"]')
            ingredient_list = {}
            ingredient_list[recipe_path.stem] = []
            for ingredient in ingredients:
                ingredient_list[recipe_path.stem].append(ingredient.text)
            recipe_list.append(ingredient_list)
            recipe.close()
        except:
            print(f"Uh-oh. A problem occurred with '{recipe_path.stem}'.")


    return recipe_list


def main():
    print(pull_ingredients('recipes'))

if __name__ == '__main__':
    main()