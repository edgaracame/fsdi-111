from flask import Flask  # we imported Flask class from flask module

app = Flask(__name__)  # app is an instance


@app.route("/")  # this is a route
def index():  # our view function
    return "<h1>Hello world</h1>"


@app.route("/aboutme")
def aboutme():
    me = {
        "first_name": "Edgar",
        "last_name": "Castillo",
        "hobby": "Videogames"
    }

    return me
