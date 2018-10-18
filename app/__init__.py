from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


# NOTE: the routes module is imported at the bottom 
# and not at the top of the script as it is always done. 
# The bottom import is a workaround to circular imports, 
# a common problem with Flask applications. 
# You are going to see that the routes module needs to 
# import the app variable defined in this script, so 
# putting one of the reciprocal imports at the bottom avoids 
# the error that results from the mutual references between 
# these two files.

