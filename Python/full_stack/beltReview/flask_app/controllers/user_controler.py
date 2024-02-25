from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.party_model import Party

from flask_bcrypt import Bcrypt  # Only needed on routes related to login/reg
bcrypt = Bcrypt(app)

# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname
@app.route('/')
def home():
    
    return render_template('register_login.html')

# ==================================== 
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================


@app.route('/register_user', methods=['post'])
def register_user():

    if not User.validate_registration(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['new_password'])

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['new_email'],
        'password': pw_hash
    }

    newuser_id = User.Save_user(data)
    session['user_id'] = newuser_id
    return redirect('/dashboard')



@app.route('/logout')
def Logout_User():
    session.clear()
    return redirect('/')

# ====================================
# Log In Validations Route
# ====================================


@app.route('/Login_user', methods=['POST'])
def Login_user():

    email_data = {
        'email': request.form['email']
    }

    user_in_db = User.GetUserByEmail(email_data)

    if not user_in_db:
        flash('Invalid Email/Password')
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Password')
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')
# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================


@app.route('/dashboard')
def Dashboard():
    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')
    
    one_user = User.GetUserById({'id': session['user_id']})

    all_parties = Party.get_all_parties()
    
    return render_template('dashboard.html', one_user=one_user, all_parties=all_parties)



@app.route('/parties/<int:party_id>')
def show_party(party_id):
    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')
    
    one_party = Party.get_one_party({'party_id': party_id})

    return render_template('one_party.html', one_party=one_party)



@app.route('/my_parties')
def show_myParties():
    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')
    
    user_with_parties = User.GetMyParties({'user_id': session['user_id']})

    return render_template('user_parties.html', user_with_parties=user_with_parties)


# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================



# ====================================
#    Delete Routes
# ====================================