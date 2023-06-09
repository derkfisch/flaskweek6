from app import app
from flask import render_template, redirect, url_for, flash
from fake_data import posts
from app.forms import SignUpForm, LoginForm

@app.route('/')
def index():
    return render_template('index.html', posts=posts, logged_in=False)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Create an instance of the form (in the context of the current request)
    form = SignUpForm()
    # Check if the form was submitted and that all of the fields are valid
    if form.validate_on_submit():
        # If so, get the data from the form fields
        print('Hooray our form was validated!!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(first_name, last_name, email, username, password)
        flash(f"Thank you {first_name} for signing up!", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Form Validated :)')
        username = form.username.data
        password = form.password.data
        print(username, password)
        # TODO: Check if there is a user with username and that password
        # Fake an invalid log in
        if password == 'abc':
            flash('Invalid username and/or password. Please try again', 'danger')
            return redirect(url_for('login'))

        flash(f'You have successfully logged in as {username}', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)