from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user_model




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
        self.party_poster = None


    @staticmethod
    def validate_party(new_party):
        is_valid = True
        if len(new_party['name']) < 1:
            is_valid = False
            flash('Name must be longer than 3 char')
        if len(new_party['location']) < 1:
            is_valid = False
            flash('Location must be longer than 3 char')
        if len(new_party['party_date']) < 1:
            is_valid = False
            flash('Date must be longer than 3 char')
        #logic for radio buttons
        if 'all_ages' not in new_party:
            flash('All ages is requiored')
            is_valid = False
        
        if len(new_party['description']) < 1:
            is_valid = False
            flash('muuust describe')

        return is_valid


    @classmethod
    def create_party(cls, data):
        query = """
            INSERT INTO parties (name, location, party_date, all_ages, description, user_id)
            VALUES ( %(name)s, %(location)s, %(party_date)s, %(all_ages)s, %(description)s, %(user_id)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    

    @classmethod
    def get_all_parties(cls):
        query = """
            SELECT * FROM parties
            JOIN users ON users.id = parties.user_id;
        """
        results = connectToMySQL(cls.DB).query_db(query)

        all_parties = []

        for row in results:
        #create name baised on what object you want to build
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'], #users.blank because users is the table we want the id from
                'updated_at': row['users.updated_at']
            }

            one_party = cls(row) #creates one party object from each row returned from the join query
            one_party.party_poster = user_model.User(user_data)
            # Construction a single party object
            #Inside of that party Object is a User object in the feild "party_poster"
            all_parties.append(one_party)
        
        return all_parties
    

    @classmethod
    def get_one_party(cls, data):
        query = """
        SELECT * FROM parties
        JOIN users ON users.id = parties.user_id
        WHERE parties.user_id = %(party_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print('get one party results = ', results)

        one_party = cls(results[0])  
        user_data = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'], #users.blank because users is the table we want the id from
                'updated_at': results[0]['users.updated_at']
            }

        one_party.party_poster = user_model.User(user_data)
        return one_party
