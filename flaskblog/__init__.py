from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# app initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = '8841cdfb73befb12ef339724378e22e1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # creates database instance

from flaskblog import routes