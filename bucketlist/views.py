from flask import render_template, request, redirect, url_for, session

from bucketlist import app, models
from .forms import SignUpForm


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
    form = SignUpForm(request.form)
    return render_template("sign_up.html", form=form)

@app.route("/sign-up/new-user", methods=['GET', 'POST'])
def create_user():
    user = models.User(request.form.get('fullname'),
                       request.form.get('email'), request.form.get('password'))
    user_full_name = user.getUser()

    session['name'] = user_full_name['name']

    return redirect(url_for('user_bucket_lists'))


@app.route("/logout")
def logout():
    session['name'] = ""
    return redirect(url_for('index'))


@app.route("/my-bucketlists/")
def user_bucket_lists():
    return render_template('view_bucket_lists.html')


@app.errorhandler(404)
def nage_not_found(error):
    return render_template('404.html'), 404



