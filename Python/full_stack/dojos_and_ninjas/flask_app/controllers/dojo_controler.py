from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo_model import Dojo



# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================


# ====================================
# Log In Validations Route
# ====================================


# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================
@app.route('/')
def home():
    all_dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', all_dojos=all_dojos)

@app.route('/show_dojo/<int:id>')
def get_one_dojo(id):

    one_dojo = Dojo.get_one_dojo(id)
    print('name = ', one_dojo.name)
    return render_template('show_dojo.html', one_dojo=one_dojo)

# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================