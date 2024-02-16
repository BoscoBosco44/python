from flask_app.templates import app
from flask_app.models.game_model import Game

from flask import render_tmplate, request




@app.route("/")
def index():
    # call the get all classmethod to get all friends
    # friends = Friend.get_all()
    # print(friends)
    return render_template("index.html")


@app.route('/game_form')
def show_form():
    
    return render_tmplateJ('game_form.html')