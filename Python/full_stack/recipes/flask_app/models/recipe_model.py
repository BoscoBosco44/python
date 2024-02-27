from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user_model

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
        self.under_30_min = ['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.recipe_poster = []


    @staticmethod
    def validate_recipe(new_recipe):
        is_valid = True
        if len(new_recipe['name']) < 1:
            flash('Must be filled in')
            is_valid = False
        if len(new_recipe['description']) < 1:
            flash('Must be filled in')
            is_valid = False
        if len(new_recipe['instructions']) < 1:
            flash('Must be filled in')
            is_valid = False
        if 'under_30_min' not in new_recipe:
            flash('Must be filled in')
            is_valid = False
        if len(new_recipe['created_at']) < 1:
            flash('Must be filled in')
            is_valid = False
        return is_valid

    @classmethod
    def add_recipe_to_DB(cls, data):
        query = """
            INSERT INTO recipes (name, description, instructions, under_30_min, user_id)
            VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30_min)s, %(user_id)s);
        """
        recipe_id = connectToMySQL(cls.DB).query_db(query, data)
        print("RECIPE ID : ", recipe_id)
        return recipe_id
    
    @classmethod
    def get_all_recipies(cls):
        query = """
            SELECT *
            FROM recipes
            JOIN users ON users.id = recipes.user_id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        print("GET ALL RESULTS : ", results)
        all_recipies = []

        for row in results:
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            one_recipe = cls(row)
            one_recipe.recipe_poster = user_model.User(user_data)

            all_recipies.append(one_recipe)


        return all_recipies