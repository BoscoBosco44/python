from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User

from flask_bcrypt import Bcrypt  # Only needed on routes related to login/reg
bcrypt = Bcrypt(app)

# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname

@app.route('/')
def home():

    return render_template('home.html')

# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================
@app.route('/create_user', methods=['post'])
def create_user():

    if not User.validate_registration(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['new_password'])

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['new_email'],
        'password': pw_hash
    }

    new_user_id = User.add_user(data)
    session['user_id'] = new_user_id
    return redirect(f'/success/{new_user_id}')

    # return redirect('/success/{{ new_user_id }}')

@app.route('/success/<int:user_id>')
def show_success(user_id):
    if 'user_id' not in session:
        flash("You need to log in")
        return redirect('/')
    
    return render_template('success.html')
    

# ====================================
# Log In Validations Route
# ====================================
@app.route('/login_user', methods=['POST'])
def login_user():

    data = {'email': request.form['login_email']}
    user_in_db = User.get_by_email(data)
    print('user in db = ', user_in_db)

    if not user_in_db:
        flash('Invalid Email')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['login_password']):
        flash('Invalid Password')
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    return redirect(f'/success/{session['user_id']}')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

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