from flask import render_template, url_for, flash, redirect
from application import app
from application.forms import RegistrationForm, LoginForm
from application.models import User, Post

posts = [
    {
        "author": "Bhargav Das Gupta",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "July 5, 2021"
    },
    {
        "author": "Hill",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "July 1, 2021"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template("about.html", title = "About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}.", 'success')
        return redirect(url_for('home'))

    return render_template("register.html", title = "Register", form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("Login successfull, Welcome", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful, please check credentials", 'danger')

    return render_template("login.html", title = "Login", form = form)
