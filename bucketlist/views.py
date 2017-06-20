from flask import render_template, request, redirect, url_for, session

from bucketlist import app, models
from .forms import SignUpForm, LoginForm
import hashlib


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
    form = LoginForm(request.form)
    return render_template("login.html", form=form)


@app.route('/auth/login', methods=['GET', 'POST'])
def new_user_login():
    if request.method == 'POST':
        if request.form.get('email') == session['email']:

            hash_object = hashlib.sha1(request.form.get('password').encode())
            entered_password = hash_object.hexdigest()

            if session['password'] == entered_password:
                return redirect(url_for('user_bucket_lists'))
            else:
                return redirect(url_for('new_user_login'))

@app.route('/auth/user', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        user = models.User("Return User A",
                           request.form.get('email'), request.form.get('password'))
        user_details = user.getUser()

        session['name'] = user_details['name']
        session['email'] = user_details['email']
        session['password'] = user_details['password']

        return redirect(url_for('user_bucket_lists'))


@app.route("/sign-up")
def signup():
    form = SignUpForm(request.form)
    return render_template("sign_up.html", form=form)

@app.route("/sign-up/new-user", methods=['GET', 'POST'])
def create_user():

    if request.method == 'POST':
        user = models.User(request.form.get('fullname'),
                           request.form.get('email'), request.form.get('password'))
        user_details = user.getUser()

        session['name'] = user_details['name']
        session['email'] = user_details['email']
        session['password'] = user_details['password']
        session['new'] = 1

        return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session['name'] = ""
    session['email'] = ""
    session['password'] = ""
    return redirect(url_for('index'))


@app.route("/my-bucketlists/")
def user_bucket_lists():
    return render_template('view_bucket_lists.html')

@app.route("/bucketlist-activities")
def user_bucket_lists_activities():
    return render_template('view_bucket_list_activities')


@app.errorhandler(404)
def nage_not_found(error):
    return render_template('404.html'), 404



