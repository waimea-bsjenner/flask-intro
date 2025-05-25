from flask import Flask
from random import randint
from flask import render_template
from flask import redirect
from flask import request

# create the app
app = Flask(__name__)

# Home page - loading a static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# another static page
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

# passing a random number into a template
@app.get("/random/")
def random():
    num = str(randint(1,100000))
    return render_template('pages/random.jinja', num=num)

# retrieving a value from the url/route and displaying it
@app.get("/number/<int:int>")
def analyseNumber(int):
    return render_template("pages/number.jinja", int=int)

# handle any missing/non-existent pages
@app.errorhandler(404)
def notFound(e):
    return render_template("pages/404.jinja")

# static page with a form
@app.get("/form/")
def form():
    return render_template("pages/form.jinja")

# handle data posted from the form
@app.post("/processForm/")
def processForm():
    print(f"Form data: ${request.form}")
    return render_template(
        "pages/formdata.jinja",
        name=request.form["name"],
        age=request.form["age"],
        creditCard=request.form["creditCard"]
    )