from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# Have import from mysqlconnection on every model for DB interactions
# Import the model's python file as a module, not the class directly so you avoid circular import errors!
# For example: from flask_app.models import table2_model

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


'''
! Note: If you are working with tables that are related to each other, 
!       you'll want to import the other table's class here for when you need to create objects with that class. 

! Example: importing pets so we can make pet objects for our users that own them.

Class should match the data table exactly that's in your DB.

REMEMBER TO PARSE DATA INTO OBJECTS BEFORE SENDING TO PAGES!

'''

class Email_Address:
    DB = 'email_db'

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validator(email):
        is_valid = True
        if len(email['email']) < 3:
            is_valid = False
            flash("Email must be longer than 3 char")
        if not EMAIL_REGEX.match(email['email']):
            is_valid = False
            flash("Email is invalid")
        return is_valid


    @classmethod
    def add_email_to_DB(cls, data):
        query = """
            INSERT INTO emails (email)
            VALUES (%(email)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result


    @classmethod
    def get_all_emails(cls):
        query = """
            SELECT *
            FROM emails
            ORDER BY id DESC;
        """
        results = connectToMySQL(cls.DB).query_db(query)

        print('get all results = ', results)
        return results


    # @classmethod
    # def 