from flask_app.config.mysqlconnection import connectToMySQL

class Game:

    DB = 'gamedb'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.release_year = data['release_year']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def get_all(cls):
        query = """ 
            SELECT *
            FROM games;
        """


        results = connectToMySQL(cls.DB).query_db(query)
        print(f"Results : {results}")

        games = []

        for row in results:
            games.append(cls(row))

        return games
    

    @classmethod
    def get_one(cls, game_id):
        query = """
        SELECT *
        FROM games
        WHERE id = %(game_id)s;
        """

        data = {'game_id' : game_id }
        results = connectToMySQL(cls.DB).query_db(query, data)
        print("Right here")
        print("These results: ", results)

        one_game = cls(results[0])

        return one_game


    @classmethod
    def add_game(cls, data):
        #data represents our request.form dictionary!
        query = """
        INSERT INTO games (name, genre, release_year)
        VALUES ( %(name)s, %(genre)s, %(release_year)s )
        """
        return connectToMySQL(cls.DB).query_db(query, data)
    


    @classmethod
    def update_game(cls, data):
        query = """
            UPDATE games
            SET name=%(name)s, genre=%(genre)s, release_year=%(release_year)s
            WHERE id = %(game_id)s
            """

        return connectToMySQL(cls.DB).query_db(query, data)
    

    @classmethod
    def delete_game(cls, game_id):
        print("Game id from delte_game CLASSMETHOD: ", game_id)
        query = """DELETE FROM games WHERE id = %(game_id)s"""
        data = {"game_id": game_id}

        print('DELETE QUERY: ', query)

        return connectToMySQL(cls.DB).query_db(query, data)