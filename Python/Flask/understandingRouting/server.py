from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template("index.html")

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def returnName(name):
    return "Hi " + name

@app.route('/repeat/<int:num>/<string:str>')
def repeat(num, str):
    return f"{str * num}"

if __name__ == "__main__":
    app.run(debug=True)