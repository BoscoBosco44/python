from flask import Flask, render_template, request, session
import random
app = Flask(__name__)  
app.secret_key = "keep it secret, keep it safe"


@app.route('/', methods=['GET', 'POST'])         
def index():
    session.clear()
    theNum = random.randint(1, 100)
    session['theNum'] = theNum

    numGuess = 0
    session['numGuess'] = numGuess
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    theNum = session['theNum']
    guess = int(request.form['theGuess'])
    session['theGuess'] = guess
    guessWas = False
    bgColor = 'bg-danger'

    session['numGuess'] = session['numGuess'] + 1
    numGuess = session['numGuess'] 


    if guess > theNum:
        hint = "Too high!"
    if guess < theNum:
        hint = "Too low!"
    if guess == theNum:
        hint = "Nice Job!!!"
        bgColor = 'bg-warning'

    if numGuess > 5:
        hint = "You have FAILED, Try again"
        

    if guess == theNum:
        guessWas = True
    print(theNum)
    print(guess)

    return render_template('guess.html', guessWas_on_template = guessWas, 
                    hint_on_template = hint, returnBgColor = bgColor, numGuess_on_tempalte = numGuess)



if __name__=="__main__":   
    app.run(debug=True)    