from flask import render_template, redirect, Blueprint, request, url_for, flash
from flask_login import login_user, logout_user
from todoproject import db
from todoproject.models import User, Todos
from todoproject.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)


# register
@users.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
        username=form.username.data,
        password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('You are now registered')
        return redirect(url_for('users.login'))
    
    return render_template('register.html', form=form)


#login
@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Login Success!')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('core.index')
            
            return redirect(next)

    return render_template('login.html', form=form)


#logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
