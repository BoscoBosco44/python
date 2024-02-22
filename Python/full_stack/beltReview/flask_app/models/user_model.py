from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

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