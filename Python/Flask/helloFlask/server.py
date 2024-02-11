from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response



# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"
    
    # app.run(debug=True) should be the very last statement! 

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<int:num>')
def showUserProfile(username, num):
    print(username)
    print(id)
    return f"Hello, {username * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

# @app.route('/success')
# def success():
#     return "Success"