import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from werkzeug.serving import make_ssl_devcert

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:kancolledbpw@127.0.0.1:3306/admin'
db = SQLAlchemy(app)

# use this to run the SSL to run locally on 127.0.0.1:8080
make_ssl_devcert('./ssl', host='localhost')

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = "strong"
login_manager.login_message_category = 'info'

from webapp import routes, models
