from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo_model import Dojo

# Import Your Models as Classes into the Controller to use their Classmethods

# from flask_app.models.table_model import classname


# ====================================
#    Create Routes
#    Show Form Route, Submit Form Route
# ====================================

@app.route('/', methods=['GET', 'POST'])         
def index():

    return render_template('survey.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    Dojo.store_results(request.form)
    # if not Dojo.validate_survey(request.form):
    #     return redirect('/')

    return redirect('/result')

@app.route('/result')
def result():
    latest_survey = Dojo.get_last_survey()
    return render_template('results.html', latest_survey=latest_survey)

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