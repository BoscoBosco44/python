from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homePg():
    return render_template("checkerboard.html")

@app.route('/<int:x>/<int:y>')
def createBoard(x, y):
    return render_template("checkerboard.html", x=x, y=y)



if __name__ == "__main__":
    app.run(debug=True)