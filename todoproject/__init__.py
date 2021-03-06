from distutils.log import Log
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# DATABASE CONNECTION
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# LOGIN CONFIG
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'


from todoproject.core.views import core
from todoproject.users.views import users
from todoproject.todos.views import todos
from todoproject.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(todos)
app.register_blueprint(error_pages)