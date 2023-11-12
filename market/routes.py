from market import app
from flask import (
    render_template, 
    redirect, 
    url_for, 
    get_flashed_messages, 
    flash, 
    request, 
    session
)
from market.models import Item, User, Review
from market.forms import RegistrationForm, SearchForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required

# Route for the base URL ("/")
@app.route("/")
def base():
    return render_template("home.html")

# Route for the "/home" URL
@app.route("/home")
def home_page():
    return render_template('home.html')

# Route for the "/market" URL
@app.route("/market")
@login_required
def market():
    item_name = Item.query.all()
    
    return render_template('market.html', item_name = item_name)

# Route for the "/login" URL
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(form.password.data):
            login_user(attempted_user)
            flash(f'Welcome {attempted_user.username}, You have successfully logged in...', category='admit')
            return redirect(url_for("market"))
        else:
            flash('Invalid user credentials', category='danger')
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", 'POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_create = User(username=form.username.data, 
                           email_address=form.email.data, 
                           mobile=form.mobile.data, 
                           password=form.password1.data)
        db.session.add(user_create)
        db.session.commit()
        flash('You have successfully registered...', category='admit')
        return redirect(url_for("login"))
    if form.errors:
        for err_msg in form.errors.values():
            flash(f'There is an error while creating user, {err_msg[0]}', category='danger')
    return render_template('register.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out successfully", category='info')
    return redirect(url_for('base'))

@app.context_processor
def inject_search_form():
    form = SearchForm()
    return dict(form=form)

@app.route('/search', methods=["POST", "GET"])
@login_required
def search():
    form = SearchForm()
    posts = Item.query
    if form.validate_on_submit():
        searched = form.searched.data
        posts = posts.filter(Item.name.like('%' + searched + '%'))
        posts = posts.order_by(Item.price).all()
        searched_list = []
        if posts:
            for post in posts:
                if post.name not in searched_list:
                    searched_list.append([post.name, post.price])
            return render_template('search.html', form=form, searched=searched, posts=searched_list)
        else:
            return render_template('search.html', form=form, searched=f'{searched}, no match found')


@app.route('/market/<int:id>', methods=["GET", "POST"])
@login_required
def product(id):
    post = Item.query.get(id)
    return render_template('product.html', item = post)

   