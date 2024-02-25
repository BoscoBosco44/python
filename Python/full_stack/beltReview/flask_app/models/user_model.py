from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

from flask_app.models import party_model


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class User:
    DB = 'belt_review'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.my_parties = []


    @staticmethod
    def validate_registration(new_user):
        is_valid = True
        if len(new_user['first_name']) < 3:
            is_valid = False
            flash('First name must be longer than 3 char')
        if len(new_user['last_name']) < 3:
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

        if len(new_user['new_password']) < 3:
            is_valid = False
            flash('Password must be longer than 3 char')
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
    

    @classmethod
    def GetMyParties(cls, data):
        query = """
            SELECT * FROM users
            JOIN parties ON users.id = parties.user_id;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)

        one_user = cls(results[0])

        for row in results:
        #create name baised on what object you want to build
            party_data = {
                'id': row['parties.id'],
                'name': row['name'],
                'location': row['location'],
                'party_date': row['party_date'],
                'all_ages': row['all_ages'],
                'description': row['description'],
                'created_at': row['parties.created_at'], #users.blank because users is the table we want the id from
                'updated_at': row['parties.updated_at'],
                'user_id': row['user_id']
            }

            one_user.my_parties.append(party_model.Party(party_data))
            # Construction a single party object
            #Inside of that party Object is a User object in the feild "party_poster"
        
        return one_user