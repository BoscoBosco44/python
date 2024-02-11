from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homePg():
    return render_template("home.html")

@app.route('/play/<int:x>/<boxColor>')
def playX(x, boxColor):
    return render_template("playground.html", x=x, boxColor=boxColor)

if __name__ == "__main__":
    app.run(debug=True)