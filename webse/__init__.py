from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# DB_VAR=os.environ.get('DATABASE_URL_POSTGRESQL', None)

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nwnuqchwcpcjss:7176f206a90a4161a0b7a4d1d74eb6c5f1c4382be315c7cc816cd9e034511f8c@ec2-52-31-217-108.eu-west-1.compute.amazonaws.com:5432/de5cnke41h2r55'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from webse import routes