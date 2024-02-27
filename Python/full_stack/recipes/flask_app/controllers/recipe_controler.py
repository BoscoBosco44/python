from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe

from flask_bcrypt import Bcrypt  # Only needed on routes related to login/reg
bcrypt = Bcrypt(app)

# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname

# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================
@app.route('/add_new_recipe', methods=['GET','POST'])
def add_new_recipe():

    if not Recipe.validate_recipe(request.form):
        return redirect('/add_new_recipe_page')

    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'under_30_min': request.form['under_30_min'],
        'user_id': session['user_id'],
    }

    recipe_id = Recipe.add_recipe_to_DB(data)
    return redirect('/users_recipes')

# ====================================
# Log In Validations Route
# ====================================


# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================
@app.route('/get_all_user_recipes')
def get_all_user_recipes():
    id = session['user_id']
    recipe_list = Recipe.get_all_by_id(id)
    return redirect('/user_recipes', recipe_list)

@app.route('/users_recipes')
def show_users_recipes():
    all_recipes = Recipe.get_all_recipies()

    return render_template('view_user_recipes.html', all_recipes=all_recipes)

@app.route('/add_new_recipe_page')
def show_add_recipe_page():
    
    return render_template('add_new_recipe.html')

# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================