from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from sqlalchemy import create_engine
import pandas as pd

DB_VAR=os.environ.get('DATABASE_URL_POSTGRESQL', None)
##DB_VAR="sqlite:///site.db" ###Local DB for testing

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_VAR

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

class test_db:
    def __init__(self,table_name,DB_URI):
        engine_local=create_engine(DB_URI)
        df_t=pd.read_sql("SELECT * FROM {}".format(table_name),engine_local)
        test=df_t.shape[0]
        
        if test==0:
            self.test_bin=False
        else:
            self.test_bin=True
            
        engine_local.dispose()
        

test_post=test_db("post",DB_VAR).test_bin
test_moduls=test_db("moduls",DB_VAR).test_bin
test_announcement=test_db("announcement",DB_VAR).test_bin

from webse import routes
