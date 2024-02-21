from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.email_model import Email_Address


# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname

@app.route('/')
def home():

    return render_template('email_validation.html')

# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================
@app.route('/add_email', methods=['POST'])
def add_email_to_db():

    if Email_Address.validator(request.form) == True:
        data = {'email':request.form['email']}
        Email_Address.add_email_to_DB(data)
        return redirect('/email_valid')
    else:
        return redirect('/')

# ====================================
# Log In Validations Route
# ====================================


# ====================================
#    Read Routes
#    Show Routes (Get All and Get One)
# ====================================
@app.route('/email_valid')
def get_all_and_display():
    emails = Email_Address.get_all_emails()
    return render_template('success.html', emails=emails)

# ====================================
#    Update Routes
#    Update Form Route, Submit Update Form Route
# ====================================


# ====================================
#    Delete Routes
# ====================================