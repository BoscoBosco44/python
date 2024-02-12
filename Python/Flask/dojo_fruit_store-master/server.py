from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print("got post inf0o")
    print(request.form)
    arr = (request.form)

    apple = int(request.form['apple'])
    straw = int(request.form['strawberry'])
    rasp = int(request.form['raspberry'])
    count = apple + straw + rasp
    print(count)

    print(arr)
    print("type", type(arr))
    print(request.form['apple'])
    print("//-------------------------------------//")
    print("Chargin ", request.form['first_name'], request.form['last_name'], " for ", count)
    print("//-------------------------------------//")

    return render_template("checkout.html", arr=arr)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    