from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_bcrypt import Bcrypt  # Only needed on routes related to login/reg
bcrypt = Bcrypt(app)

# Import Your Models as Classes into the Controller to use their Classmethods
from flask_app.models.pie_model import Pie
from flask_app.models.user_model import User
# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================

#CREATE PIE ROUTE
@app.route('/pie/create', methods=['POST'])
def create_pie():

    if not Pie.validate_pie(request.form):
        return redirect('/dashboard')
    
    pie_data = {
        **request.form,
        'user_id': session['user_id']
    }
    party_id = Pie.create_pie(pie_data)
    return redirect('/dashboard')

# ====================================
# Log In Validations Route
# ====================================


# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================

#SHOW ALL PIES
@app.route('/pies')
def show_all_pies():

    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')

    all_pies = Pie.get_all()

    return render_template('all_pies.html', pies=all_pies)

#SHOW EDIT PIE PAGE
@app.route('/pies/edit/<int:pie_id>')
def show_edit_pie(pie_id):

    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')
    
    data = {'pie_id': pie_id}
    thePie = Pie.get_one_pie(data)


    return render_template('edit.html', pie=thePie)


#SHOW ONE PIE (AND VOTES)
@app.route('/pies/<int:pie_id>')
def show_one_pie(pie_id):

    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')

    data = {'pie_id': pie_id}
    thePie = Pie.get_one_pie(data)

    return render_template('view_one_pie.html', pie=thePie)

# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================

@app.route('/pies/delete/<int:pie_id>')
def delete_pie(pie_id):

    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')

    pie_data = {'id': pie_id}
    Pie.delete_pie(pie_data)
    return redirect('/dashboard')


# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================

@app.route('/pies/submit_edit/<int:pie_id>', methods=['POST'])
def edit_pie(pie_id):

    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')
    if not Pie.validate_pie(request.form):
        return redirect(f'/pies/edit/{pie_id}')
    
    pie_data = {
        **request.form,
        'id': pie_id
    }
    pie_id = Pie.update_pie(pie_data)

    return redirect('/dashboard')