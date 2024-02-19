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
    one_game = Game.get_one(game_id)

    return render_template('one_game.html', one_game=one_game)



@app.route('/game/edit/<int:game_id>')
def show_eddit_form(game_id):
    one_game = Game.get_one(game_id)
    
    return render_template('edit_form.html', one_game=one_game)


@app.route('/submit_edit_form/<int:game_id>', methods=['POST'])
def submit_edit_form(game_id):

    data = {
        'name': request.form['name'],
        'genre': request.form['genre'],
        'release_year': request.form['release_year'],
        'game_id' : game_id
    }
    Game.update_game_game(data)
    return redirect('/')


#Delete
@app.route('/delete_game_from_DB/<int:game_id>')
def delete_this_game_from_DB(game_id):

    Game.delete_game(game_id)
    return redirect('/')