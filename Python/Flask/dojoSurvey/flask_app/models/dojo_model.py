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

class Dojo:
    DB = 'dojo_survey_schema'

    def __init__(self, data):
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos = []

#----------------------- Validator ------------------------
    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 char")
            is_valid = False
        if len(survey['location']) < 2:
            flash("You must live in one of these places")
            is_valid = False
        if len(survey['language']) < 3:
            flash("Plz choose a language")
            is_valid = False
        if len(survey['comment']) < 3:
            flash("Name must be at least 3 char")
            is_valid = False


    @classmethod
    def store_results(cls, data):
        query = """
            INSERT INTO dojos (name, location, language, comment)
            VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)

        return results
    
    @classmethod
    def get_last_survey(cls):
        query = """
            SELECT * FROM dojos
            ORDER BY id DESC
            LIMIT 1;
        """
        latest_survey = connectToMySQL(cls.DB).query_db(query)
        return latest_survey[0]
