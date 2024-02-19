from flask import render_template, redirect, request
from flask_app import app



# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================

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


# ====================================
# Log In Validations Route
# ====================================


# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================

@app.route('/')
def home():

    return render_template('index.html')


# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================