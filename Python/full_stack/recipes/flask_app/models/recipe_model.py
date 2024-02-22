from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# Have import from mysqlconnection on every model for DB interactions
# Import the model's python file as a module, not the class directly so you avoid circular import errors!
# For example: from flask_app.models import table2_model

'''
! Note: If you are working with tables that are related to each other, 
!       you'll want to import the other table's class here for when you need to create objects with that class. 

! Example: importing pets so we can make pet objects for our users that own them.

Class should match the data table exactly that's in your DB.

REMEMBER TO PARSE DATA INTO OBJECTS BEFORE SENDING TO PAGES!

'''

class Recipe:
    DB = 'recipes'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated-at']
        self.user_id = data['user_id']
        self.recipes = []


    @classmethod
    def add_recipe_to_DB(cls, data, user_id):
        query = """
            INSERT INTO recipes (name, description, instructions, under_30_min, user_id)
            VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30_min)s, %(user_id)s);
        """
        recipe_id = connectToMySQL(cls.DB).query_db(query, data)
        return recipe_id
    
    @classmethod
    def get_all_by_id(cls, id):
        query = """
            SELECT *
            FROM recipes
        """
        list_of_dic_of_recipes = connectToMySQL(cls.DB).query_db(query)
        recipe_list = cls(list_of_dic_of_recipes[0])

        for row_from_db in list_of_dic_of_recipes:
            recipe_data = {
                'id':row_from_db['recipe.id'],
                'name':row_from_db['recipe.name'],
                'description':row_from_db['recipe.description']
            }
            recipe_list.recipes.append( Recipe( recipe_data ))
        return recipe_list