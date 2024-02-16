from flask_app import app
from flask_app.models.game_model import Game
from flask import render_template, request, redirect




@app.route("/")
def index():
    # call the get all classmethod to get all friends
    # friends = Friend.get_all()
    # print(friends)
    all_games = Game.get_all()

    return render_template("index.html", all_games=all_games)


@app.route('/game_form')
def show_form():
    
    return render_template('game_form.html')

@app.route('/submit_game_form', methods=['POST'])
def submit_game_form():

    data = {
        'name': request.form['name'],
        'genre': request.form['genre'],
        'release_year': request.form['release_year']
    }
    Game.add_game(data)
    return redirect('/')


#Show one game route

@app.route('/game/<int:game_id>')
def show_one_game(game_id):
    one_game = Game.get_one({ 'game_id' : game_id})

    return render_template('one_game.html', one_game=one_game)