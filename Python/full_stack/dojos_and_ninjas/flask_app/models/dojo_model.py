from flask_app.config.mysqlconnection import connectToMySQL
# Have import from mysqlconnection on every model for DB interactions
# Import the model's python file as a module, not the class directly so you avoid circular import errors!
# For example: from flask_app.models import table2_model
from flask_app.models.ninja_model import Ninja
'''
! Note: If you are working with tables that are related to each other, 
!       you'll want to import the other table's class here for when you need to create objects with that class. 
from flask_app
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
        self.ninjas = []

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
    
    # @classmethod
    # def get_one_dojo(cls, id):
    #     query = """
    #         SELECT *
    #         FROM dojos
    #         WHERE id = %(id)s;
    #     """
    #     data = {'id': id}
    #     results = connectToMySQL(cls.BD).query_db(query, data)
    #     one_dojo = cls(results[0])
    #     print('ONE_DOJO = ', one_dojo)
    #     return one_dojo

    @classmethod
    def get_one_dojo(cls, id):
        query = """
            SELECT * 
            FROM dojos
            LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = (%(id)s);
        """
        data = {'id':id}
        results = connectToMySQL(cls.BD).query_db(query, data)

        dojo = cls( results[0])
        for row_from_db in results:
            ninja_data = {
                'id':row_from_db['ninjas.id'],
                'first_name':row_from_db['first_name'],
                'last_name':row_from_db['last_name'],
                'age':row_from_db['age'],
                'created_at':row_from_db['ninjas.created_at'],
                'updated_at':row_from_db['ninjas.updated_at'],
                'dojo_id':row_from_db['dojo_id']
            }
            dojo.ninjas.append( Ninja( ninja_data))

        return dojo

#create
    
    @classmethod
    def create_new_dojo(cls, name):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s);
        """
        results = connectToMySQL(cls.BD).query_db(query, name)
        print("RESULTS = ", results)
        return results

