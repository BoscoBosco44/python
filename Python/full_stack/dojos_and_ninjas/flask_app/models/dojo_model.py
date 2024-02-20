from flask_app.config.mysqlconnection import connectToMySQL
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
    BD = 'dojos_and_ninjas'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ====================================

    @classmethod
    def get_all_dojos(cls):
        query = """
            SELECT *
            FROM dojos
        """
        results = connectToMySQL(cls.BD).query_db(query)
        dojos = []

        for row in results:
            dojos.append(cls(row))

        return dojos
    
    @classmethod
    def get_one_dojo(cls, id):
        query = """
            SELECT *
            FROM dojos
            WHERE id = %(id)s;
        """
        data = {'id': id}
        results = connectToMySQL(cls.BD).query_db(query, data)
        one_dojo = cls(results[0])
        print('ONE_DOJO = ', one_dojo)
        return one_dojo




