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

class Ninja:
    DB = 'dojos_and_ninjas'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']


    @classmethod
    def get_all_ninjas(cls):
        query = """
            SELECT * FROM ninjas
        """
        results = connectToMySQL(cls.DB).query_db(query)
        all_ninjas = []

        for row in results:
            all_ninjas.append(cls(row))

        return all_ninjas
    

    @classmethod
    def get_just_these_ninjas(cls, dojo_id):
        query = """
            SELECT * FROM ninjas
            WHERE dojo_id = (%(dojo_id)s);
        """
        data = {'dojo_id': dojo_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        all_these_ninjas = []

        for row in results:
            all_these_ninjas.append(cls(row))

        return all_these_ninjas


    @classmethod
    def create_new_ninja(cls, data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("create new ninja results = ", results)
        return results