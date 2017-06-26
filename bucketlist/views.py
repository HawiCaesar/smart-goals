from flask import render_template, request, redirect, url_for, session, flash, Markup

from bucketlist import app, models
from .forms import SignUpForm, LoginForm, BucketlistForm, ActivityForm, BucketlistFormUpdate
import hashlib
from .models import all_users, all_bucketlists, all_bucketlists_activities

global current_user
current_user = []


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
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route('/auth/', methods=['GET', 'POST'])
def new_user_login():

    form = LoginForm(request.form)

    if form.validate_on_submit():

        hash_object = hashlib.sha1(request.form.get('password').encode())
        entered_password = hash_object.hexdigest()

        #User exists
        if request.form.get('email') in all_users:

            if all_users[request.form.get('email')][2] == entered_password:

                set_current_user(all_users[request.form.get('email')])

                return redirect(url_for('user_bucket_lists'))
            else:
                error = Markup("<div class='alert alert-danger' role='alert'>\
                        <strong>Invalid Credentials! </strong>Either your email or password is wrong!\
                        Please enter correct credentials!\
                        </div>")

                flash(error)
                return render_template("login.html", form=LoginForm())

        else:
            error = Markup("<div class='alert alert-danger' role='alert'>\
                        <strong>Invalid Credentials</strong> Either your email or password is wrong!\
                        Please enter correct credentials!\
                        </div>")
            flash(error)
            return render_template("login", form=LoginForm())


    else:
        return render_template("login", form=LoginForm())

## Set user details on login
def set_current_user(user_details):

    global current_user
    current_user = user_details

## Get user details
def check_current_user():
    logged_in = False

    global current_user

    details_count = len(current_user)

    if details_count == 0:
        logged_in = False
    else:
        logged_in = True

    return logged_in


@app.route("/sign-up")
def signup():
    form = SignUpForm()
    return render_template("sign_up.html", form=form)


@app.route("/sign-up/new-user", methods=['GET', 'POST'])
def create_user():

    form = SignUpForm(request.form)

    if form.validate_on_submit():

        if request.form.get('email') in all_users:

            error = Markup("<div class='alert alert-danger' role='alert'>\
                            <strong>User Exisits!</strong> The Email entered already exists!\
                            </div>")
            flash(error)
            return redirect(url_for("signup"))

        else:
            user = models.User()
            user.create_user(request.form.get('fullname'),
                             request.form.get('email'), request.form.get('password'))

            success = Markup("<div class='alert alert-success' role='alert'>\
                            <strong>Done! </strong>You have successfully registered! Kindly Login\
                            </div>")

            flash(success)

            form_login = LoginForm()
            return render_template("login.html", form=form_login)

    return render_template("sign_up.html", form=form)


# Log out and set the current user to empty list
@app.route("/logout")
def logout():
    global current_user
    current_user = []

    return redirect(url_for('index'))


############################# Bucketlist functions

@app.route("/my-bucketlists/")
def user_bucket_lists():

    if check_current_user() is True:

        #Check if user has bucketlist already
        if current_user[1] in all_bucketlists:
            return render_template('view_bucket_lists.html', user=current_user,
                                   bucketlists=all_bucketlists[current_user[1]])

        else:
            return render_template('view_bucket_lists.html', user=current_user)

    else:
        error = Markup("<div class='alert alert-danger' role='alert'>\
                        <strong>Login Required! </strong>You must be logged in to\
                        to access that page\
                        </div>")

        flash(error)
        return redirect(url_for("login"))


@app.route("/add-bucketlist")
def add_bucketlist():
    if check_current_user() is True:
        form = BucketlistForm()
        return render_template("add_bucket_list.html", form=form)

    else:
        error = Markup("<div class='alert alert-danger' role='alert'>\
                        <strong>Login Required! </strong>You must be logged in to\
                        to access that page\
                        </div>")

        flash(error)
        return redirect(url_for("login"))



@app.route("/create-bucketlist", methods=['GET', 'POST'])
def create_bucketlist():
    form = BucketlistForm()

    global current_user

    if request.method == "POST" and form.validate_on_submit():

        bucketlist = models.Bucketlist()
        bucketlist.create_bucketlist(current_user[1], request.form.get("bucketlistname"),
                                     request.form.get("simple_description"))

        success = Markup("<div class='alert alert-success' role='alert'>\
                        <strong>Done! </strong>Your "+request.form.get("bucketlistname")+"\
                         Bucketlist is created.</div>")
        flash(success)

        return render_template('view_bucket_lists.html',
                               bucketlists=all_bucketlists[current_user[1]],
                               user=current_user)

    return render_template('view_bucket_lists.html', form=form)


@app.route("/change-bucketlist/<id>")
def change_bucketlist(id):
    if check_current_user() is True:  

        global current_user
        bucketlist_detail = all_bucketlists[current_user[1]][int(id)]
        bucketlist_id = int(id)

        form = BucketlistFormUpdate()

        for key, value in bucketlist_detail.items():
            form.bucketlistname.data = key
            form.simple_description.data = value

        return render_template("change_bucket_list.html", form=form, bucketlist_id=bucketlist_id)

    else:
        error = Markup("<div class='alert alert-danger' role='alert'>\
                        <strong>Login Required! </strong>You must be logged in to\
                        to access that page\
                        </div>")

        flash(error)
        return redirect(url_for("login"))

@app.route("/update-buckelist/<id>", methods=['GET', 'POST'])
def update_bucketlist(id):
    if check_current_user() is True:

        form = BucketlistFormUpdate(request.form)

        if form.validate_on_submit():
            global current_user

            bucketlist = models.Bucketlist()
            bucketlist.update_bucketlist(current_user[1], int(id),
                                         request.form.get("bucketlistname"),
                                         request.form.get("simple_description"))


            print(all_bucketlists[current_user[1]])

            return redirect(url_for("user_bucket_lists"))

        else:
            return render_template("change_bucket_list.html", form=form)

    else:
        error = Markup("<div class='alert alert-danger' role='alert'>\
                        <strong>Login Required! </strong>You must be logged in to\
                        to access that page\
                        </div>")

        flash(error)
        return redirect(url_for("login"))


@app.route("/delete-bucketlist/<id>", methods=['GET', 'POST'])
def delete_bucketlist(id):
    if check_current_user() is True:
        global current_user

        bucketlist = models.Bucketlist()
        bucketlist.delete_bucketlist(current_user[1], int(id))

        return redirect(url_for("user_bucket_lists"))

    else:
        error = Markup("<div class='alert alert-danger' role='alert'>\
                        <strong>LLogin Required! </strong>You must be logged in to\
                        to access that page\
                        </div>")

        flash(error)
        return redirect(url_for("login"))


################# Bucketlist Activity functions

@app.route("/bucketlist-activities/<id>/<bucketlist>")
def user_bucket_lists_activities(id, bucketlist):

    id = int(id)

    bucketlist_details = []
    bucketlist_details.append(id)
    bucketlist_details.append(bucketlist)

    return render_template('view_bucket_list_activities.html',
                           bucketlist_info=bucketlist_details,
                           activities=all_bucketlists_activities)

@app.route("/add-bucketlist-activity/<id>")
def activity_page(id):
    form = ActivityForm()

    bucketlist_key = int(id)
    bucket = ""

    for key, value in all_bucketlists[bucketlist_key].items():
        bucket = key

    return render_template('add_activity.html', form=form, bucketlist=bucket, key=bucketlist_key)

@app.route("/create-bucketlist-activity/<id>/<bucketlist>",  methods=['GET', 'POST'])
def create_activity(id, bucketlist):

    form = ActivityForm(request.form)

    bucketlist_key = int(id)
    bucket = bucketlist

    if form.validate_on_submit():
        activity = models.Bucketlist_Activities()
        activity.create_bucketlist_activity(bucket,
                                            request.form.get("bucketlist_activity_name"),
                                            request.form.get("date"), False)

        success = Markup("<div class='alert alert-success' role='alert'>\
                        <strong>Done! </strong>"+request.form.get("bucketlist_activity_name")+"\
                        </div>")

        flash(success)

        current_bucket = [id, bucket]

        return render_template('view_bucket_list_activities.html',
                               activities=all_bucketlists_activities,
                               bucketlist_info=current_bucket)

    else:

        return render_template('add_activity.html', form=form)



@app.errorhandler(404)
def nage_not_found(error):
    return render_template('404.html'), 404



