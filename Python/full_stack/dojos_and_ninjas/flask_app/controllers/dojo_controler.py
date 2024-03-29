from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja



# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================
@app.route('/create_new_dojo', methods=['GET', 'POST'])
def create_new_dojo():
    name = {'name' : request.form['name']}
    print('name = ', name)
    Dojo.create_new_dojo(name)
    return redirect('/')




# @app.route('/new_ninja_page')
# def new_ninja():
#     all_dojos = Dojo.get_all_dojos()
#     return render_template('new_ninja.html', dojos = all_dojos)

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
    return render_template('show_dojo.html', one_dojo=one_dojo)

# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================