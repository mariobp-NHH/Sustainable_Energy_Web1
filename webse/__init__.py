import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



#DBVAR=os.environ.get("HEROKU_POSTGRESQL_JADE_URL_POSTGRESQL",None)

DBVAR="postgresql://eluudpjqotymch:2f4e452d80a90c0fa4f71e68840f76f6ad0969584af738e32fd0c3b836d80ea0@ec2-54-247-137-184.eu-west-1.compute.amazonaws.com:5432/dfjc7sqjeq61om"

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = DBVAR


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


from webse.announcements.routes import announcements
from webse.app_calculator.routes import app_calculator
from webse.app_module.routes import app_module
from webse.chats.routes import chats
from webse.dashboards.routes import dashboards
from webse.dashboards.spot_go import create_dash_spot_go
from webse.dashboards.dash_application2 import create_dash_application2
from webse.home.routes import home
from webse.se_module.routes import se_module
from webse.statistics.routes import statistics
from webse.students_apps.routes import students_apps
from webse.users.routes import users

create_dash_spot_go(app)
create_dash_application2(app)

app.register_blueprint(announcements)
app.register_blueprint(app_calculator)
app.register_blueprint(app_module)
app.register_blueprint(chats)
app.register_blueprint(dashboards)
app.register_blueprint(home)
app.register_blueprint(se_module)
app.register_blueprint(statistics)
app.register_blueprint(students_apps)
app.register_blueprint(users)
