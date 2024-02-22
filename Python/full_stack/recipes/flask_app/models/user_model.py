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

class User:
    DB = 'recipes'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_registration(user):
        is_valid = True
        if len(user['first_name']) < 3:
            is_valid = False
            flash('First name must be longer than 3 char')
        if len(user['last_name']) < 3:
            is_valid = False
            flash('Last name must be longer than 3 char')
        if not EMAIL_REGEX.match(user['new_email']):
            is_valid = False
            flash("Email is invalid")
        if not User.check_if_email_exits(user['new_email']):
            is_valid = False
            flash('Email already exits')
        if len(user['new_password']) < 3:
            is_valid = False
            flash('Password must be longer than 3 char')
        if user['new_password'] != user['new_password_confirm']:
            is_valid = False
            flash("Passwords must match")
        return is_valid
    
    @classmethod
    def add_user(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        id_num = connectToMySQL(cls.DB).query_db(query, data)
        return id_num
    
    @classmethod
    def check_if_email_exits(cls, email):
        email_allowed = True
        query = """
            SELECT email
            FROM users
        """
        email_list = connectToMySQL(cls.DB).query_db(query)
        print(email_list)
        for email_addy in email_list:
            if email == email_addy['email']:
                email_allowed = False

        return email_allowed
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
