from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User


# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================

@app.route('/addUser', methods=['POST'])
def add_user():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    print("DATA FROM ADD_USER: ", data)

    User.add_user(data)
    return redirect('/')


# ====================================
# Log In Validations Route
# ====================================


# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================

@app.route('/')
def show_users():

    all_users = User.get_all()

    return render_template('index.html', all_users=all_users)

@app.route('/createNewUser', methods=['GET','POST'])
def createNewUser_page():

    return render_template('create.html')


@app.route('/show_one_user/<int:user_id>')
def show_one_user(user_id):
    one_user = User.show_one_user(user_id)
    return render_template('show_one.html', one_user=one_user)

@app.route('/edit/<int:user_id>')
def show_edit_page(user_id):
    one_user = User.show_one_user(user_id)
    return render_template('edit.html', one_user=one_user)


# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================

@app.route('/editUser/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    User.edit_user(user_id)
    return redirect('/')

# ====================================
#    Delete Routes
# ====================================