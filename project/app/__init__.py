import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import config

app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')


db = SQLAlchemy(app)
migrate = Migrate(app,  db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


from . import views
