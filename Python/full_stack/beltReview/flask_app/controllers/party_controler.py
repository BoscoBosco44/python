from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.party_model import Party


#Show Route for Form
@app.route('/parties/new')
def Show_Form():
    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')

    return render_template('create_party.html')


#Submit Form route
@app.route('/parties/create', methods=['POST'])
def Submit_Party_Form():

    if not Party.validate_party(request.form):
        return redirect('/parties/new')

    # party_data = {
    #     'name': request.form['name'],
    #     'location': request.form['location'],
    #     'party_date': request.form['party_date'],
    #     'all_ages': request.form['all_ages'],
    #     'description': request.form['description'],
    #     'user_id': session['user_id'],
    # }  THIS CODE IS EQUAL TO THE CODE BELLOW

    party_data = {
        **request.form,
        'user_id': session['user_id']
    }

    party_id = Party.create_party(party_data)

    return redirect('/dashboard')


@app.route('/parties/<int:party_id>/edit')
def show_edit_party(party_id):
    if 'user_id' not in session:
        flash('Please sign in!')
        return redirect('/')

    one_party = Party.get_one_party({'party_id': party_id})

    return render_template('edit_party.html', one_party=one_party)