from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================
@app.route('/new_ninja_page')
def new_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos = all_dojos)


@app.route('/ninja/create', methods=['POST'])
def create_new_ninja():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    Ninja.create_new_ninja(data)
    return redirect('/')


# ====================================
# Log In Validations Route
# ====================================


# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================


# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================