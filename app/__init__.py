from flask import Flask
from random import randint
from flask import render_template
from flask import redirect

# create the app
app = Flask(__name__)

@app.get("/")
def home():
    return render_template('pages/home.jinja')

@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

@app.get("/random/")
def random():
    num = str(randint(1,100000))
    return render_template('pages/random.jinja', num=num)

@app.get("/number/<int:int>")
def analyseNumber(int):
    return render_template("pages/number.jinja", int=int)


@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")

@app.get("/form/")
def form():
    return render_template("pages/form.jinja")