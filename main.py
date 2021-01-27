import mysql.connector
from mysql.connector import Error
from puller import *
from sql_query_functions import *

DB = "recipe_database"

create_recipe_table = """
CREATE TABLE Recipe (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(80)
 );
"""

alter_recipe_table = """
ALTER TABLE recipe 
ADD ingredients VARCHAR(1000);
"""


create_ingredient_table = """
CREATE TABLE Ingredient (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);
"""

create_recipe_ingredient_table = """
CREATE TABLE RecipeIngredient (
    recipe_id INT NOT NULL,
    ingredient_id INT NOT NULL
);
"""

alter_recipe_ingredient_table = """
ALTER TABLE recipeingredient
ADD FOREIGN KEY(recipe_id)
REFERENCES Recipe(id);
"""

alter_recipe_ingredient_table_again = """
ALTER TABLE RecipeIngredient
ADD FOREIGN KEY(ingredient_id)
REFERENCES Ingredient(id);
"""

add_recipe = """
INSERT INTO recipe (name)
VALUES ('Paneer')
"""


def add_recipes(recipe_list, c):
    for recipe in recipe_list:
        for key in recipe:
            try:
                query = f"""
                INSERT INTO recipe (name, ingredients)
                VALUES ('{key}', '{recipe[key]}');
                """

                execute_query(c, query)

            except Error as e:
                print(f"The error '{e}' for recipe '{name}' has occured.")

def main():
    connection = create_connection(HOST_NAME, USER_NAME, PASSWORD, DB)

    recipe_list = pull_ingredients('recipes')
    add_recipes(recipe_list, connection)


if __name__ == '__main__':
    main()