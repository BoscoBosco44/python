from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash




class Party:
    DB = 'belt_review'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.party_date = data['party_date']
        self.all_ages = data['all_ages']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']