from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "keep it secret, keep it safe"

@app.route('/', methods=['GET', 'POST'])         
def index():

    if 'count' in session:
        count = session.get('count', 0)
        count += 1
        session['count'] = count



    return render_template("index.html", count_on_template=count)

@app.route('/increment')
def increment():
    count = session.get('count', 0)
    count += 2
    session['count'] = count
    return render_template('index.html', count_on_template=count)

@app.route('/reset')
def reset():
    session.clear()
    session['count'] = 0
    return redirect('/') 
    # return render_template('index.html')


if __name__=="__main__":   
    app.run(debug=True)    



# @app.route('/checkout', methods=['POST'])         
# def checkout():
#     print("got post inf0o")
#     print(request.form)
#     arr = (request.form)

#     apple = int(request.form['apple'])
#     straw = int(request.form['strawberry'])
#     rasp = int(request.form['raspberry'])
#     count = apple + straw + rasp
#     print(count)

#     print(arr)
#     print("type", type(arr))
#     print(request.form['apple'])
#     print("//-------------------------------------//")
#     print("Chargin ", request.form['first_name'],
#     request.form['last_name'], " for ", count)
#     print("//-------------------------------------//")

#     return render_template("checkout.html", arr=arr)

# @app.route('/fruits')         
# def fruits():
#     return render_template("fruits.html")