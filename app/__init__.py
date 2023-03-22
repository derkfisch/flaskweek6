from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

#create an instance of sql alchemy to connect our app to the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# import all of the routes from the routes file into the current package
from app import route, models
