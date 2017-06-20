from flask import render_template

from bucketlist import app, models

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/sign-up")
def signup():
    return render_template("sign_up.html")


@app.errorhandler(404)
def nage_not_found(error):
    return render_template('404.html'), 404

