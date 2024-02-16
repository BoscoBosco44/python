from flask_app.templates import app
from flask_app.models.game_model import Game
from flask import render_tmplate, request, redirect




@app.route("/")
def index():
    # call the get all classmethod to get all friends
    # friends = Friend.get_all()
    # print(friends)
    return render_tmplate("index.html")


@app.route('/game_form')
def show_form():
    
    return render_tmplate('game_form.html')

@app.route('/submit_game_form', methods=['POST'])
def submit_game_form():

    data = {
        'name': request.form['name'],
        'genre': request.form['genre'],
        'release_year': request.form['release_year']
    }
    Game.add_game(data)
    return redirect('/')