from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user_model


class Pie:
    DB = 'eye_on_the_pie_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.votes = 0
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.pie_creator = None


    @staticmethod
    def validate_pie(new_pie):
        is_valid = True
        if len(new_pie['name']) < 1:
            flash('Please include a name')
            is_valid = False
        if len(new_pie['filling']) < 1:
            flash('Please include a filling')
            is_valid = False
        if len(new_pie['crust']) < 1:
            flash('Please include a crust')
            is_valid = False
        return is_valid
    

    #CREATE PIE
    @classmethod
    def create_pie(cls, data):
        query = """
            INSERT INTO pies (name, filling, crust, user_id)
            VALUES ( %(name)s, %(filling)s, %(crust)s, %(user_id)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print('RESULTS FROM CREATE PIE : ')
        return results


    #GET USER'S PIES
    @classmethod
    def get_users_pies(cls, data):
        query = """
            SELECT * FROM pies
            JOIN users ON users.id = pies.user_id
            WHERE user_id = %(user_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("GET USERS PIES RESULTS : ", results)

        user_pie_list = []

        for row in results:
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'], 
                'updated_at': row['users.updated_at']
            }
            one_pie = cls(row)
            one_pie.pie_creator = user_model.User(user_data)
            user_pie_list.append(one_pie)

        return user_pie_list
    

    #GET ALL PIES
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM pies
            JOIN users ON users.id = pies.user_id;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        print("GET ALL PIES RESULTS : ", results)
        all_pies = []

        for row in results:
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'], #users.blank because users is the table we want the id from
                'updated_at': row['users.updated_at']
            }

            one_pie = cls(row)
            one_pie.pie_creator = user_model.User(user_data)

            all_pies.append(one_pie)
        return all_pies
    
    @classmethod
    def get_one_pie(cls, data):
        query = """
            SELECT * FROM pies
            JOIN users ON users.id = pies.user_id
            WHERE pies.id = %(pie_id)s; 
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("GET ONE PIE RESULTS : ", results)

        one_pie = cls(results[0])
        user_data = {
                'id': results[0]['users.id'],
                'first_name': results[0]['first_name'],
                'last_name': results[0]['last_name'],
                'email': results[0]['email'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'], 
                'updated_at': results[0]['users.updated_at']
            }
        one_pie.pie_creator = user_model.User(user_data)
        return one_pie


    @classmethod
    def update_pie(cls, data):
        query = """
            UPDATE pies
            SET name = %(name)s,
            filling = %(filling)s,
            crust = %(crust)s
            WHERE id = %(id)s
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        print("UPDATE RESULTS : ", result)
        return result
    

    @classmethod
    def delete_pie(cls, data):
        query = """
            DELETE FROM pies
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)