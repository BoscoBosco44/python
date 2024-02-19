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


class User:
    db = 'users_cr_db'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = """
            SELECT *
            FROM users;
        """

        results = connectToMySQL(cls.db).query_db(query)
        print("Get All results : ", results)
        users = []

        for row in results:
            users.append(cls(row))

        return users
    
    @classmethod
    def add_user(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email)
            VALUES ( %(first_name)s, %(last_name)s, %(email)s)
        """

        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def show_one_user(cls, user_id):
        query = """
            SELECT *
            FROM users
            WHERE id = %(user_id)s
        """
        data = {'user_id': user_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        print("RESULTS FROM 'SHOW_ONE_USER' : ", results)

        one_user = cls(results[0])
        return one_user
    
    @classmethod
    def edit_user(cls, user_id):
        query = """
            UPDATE users
            SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s
            WHERE id = %(user_id)s
        """
        data = {'user_id':user_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        print(data)
        print("RESULTS FROM 'edit_user' : ", results)
        return data
