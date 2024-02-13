from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "keep it secret, keep it safe"

@app.route('/', methods=['GET', 'POST'])         
def index():
    if request.method == 'POST':
        session['usrName'] = request.form.get('usrName')
        session['location'] = request.form.get('location')
        session['favLang'] = request.form.get('favLang')
        session['usrComments'] = request.form.get('usrComments')
        return redirect('/result')
    return render_template('survey.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
#why is this needed?
    return redirect('/result')

@app.route('/result')
def result():
    name = session.get('usrName')
    loca = session.get('location')
    favlang = session.get('favLang')
    comment = session.get('usrComments')
    return render_template('results.html',  name_on_template=name, location_on_template=loca, favLang_on_template=favlang, comment_on_template=comment)

if __name__=="__main__":   
    app.run(debug=True)    