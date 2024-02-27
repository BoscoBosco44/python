from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class User:
    DB = 'eye_on_the_pie_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_registration(new_user):
        is_valid = True
        if len(new_user['first_name']) < 2:
            is_valid = False
            flash('First name must be longer than 3 char')
        if len(new_user['last_name']) < 2:
            is_valid = False
            flash('Last name must be longer than 3 char')


        if not EMAIL_REGEX.match(new_user['new_email']):
            is_valid = False
            flash("Email is invalid")
        else:
            query = "SELECT * FROM users WHERE email = %(new_email)s;"
            results = connectToMySQL(User.DB).query_db(query, new_user)
            if len(results) >= 1:
                flash("Email taken, try a different Email!")
                is_valid = False

        if len(new_user['new_password']) < 8:
            is_valid = False
            flash('Password must be longer than 8 char')
        if new_user['new_password'] != new_user['new_password_confirm']:
            is_valid = False
            flash("Passwords must match")
        return is_valid
    

    @classmethod
    def Save_user(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email, password)
                VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        result = connectToMySQL(cls.DB).query_db(query, data)

        if result < 1:
            return False
        return result
    
    @classmethod
    def GetUserById(cls, data):
        query = """
            SELECT * FROM users
            WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def GetUserByEmail(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])