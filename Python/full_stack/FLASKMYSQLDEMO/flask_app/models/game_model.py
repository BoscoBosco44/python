from flask_app.config.mysqlconnection import connectToMySQL

class Game:

    DB = 'gamedb'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.release_year = data['release_year']
        self.created_at = data['createed_at']
        self.updated_at = data['updated_at']
        
    
    @classmethod
    def get_all(cls):
        query = """" 
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
    def add_game(cls, data):
        #data represents our request.form dictionary!
        query = """
        INSERT INTO games (name, genre, release_year)
        VALUES ( %(name)s, %(genre)s, %(release_year)s )
        """
        return connectToMySQL(cls.DB).query_db(query, data)