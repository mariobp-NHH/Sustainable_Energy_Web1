from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from sqlalchemy import create_engine
import pandas as pd

DB_VAR=os.environ.get('DATABASE_URL_POSTGRESQL', None)
#DB_VAR="sqlite:///site.db" ###Local DB for testing

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_VAR

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

engine_local =create_engine(DB_VAR)

df_announcement=pd.read_sql("SELECT * FROM announcement",engine_local)
test_announcement=df_announcement.shape[0]
if test_announcement==0:
    test_announcement=False
else:
    test_announcement=True 

df_post=pd.read_sql("SELECT * FROM post",engine_local)
test_post=df_post.shape[0]
if test_post==0:
    test_post=False
else:
    test_post=True

df_moduls=pd.read_sql("SELECT * FROM moduls",engine_local)
test_moduls=df_moduls.shape[0]
if test_moduls==0:
    test_moduls=False
else:
    test_moduls=True

engine_local.dispose() 

from webse import routes
