from datetime import datetime
from webse import app, db, login_manager
from flask_login import UserMixin

    
@login_manager.user_loader
def load_user(user_id):
    return Userpage.query.get(int(user_id))

 
class Userpage(db.Model, UserMixin):
    __tablename__="userpage
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    course = db.Column(db.String(60), unique=False, nullable=False)
    moduls = db.relationship('Moduls', backref='author', lazy=True)
    announcements = db.relationship('Announcement', backref='author', lazy=True)
    postsm = db.relationship('Chat', backref='author', lazy=True)
    emissions = db.relationship('Emissions', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Chat(db.Model):
    __tablename__= 'chat'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    chat_module = db.Column(db.String(100), nullable=False)
    chat_group = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Chat('{self.title}', '{self.date_posted}')"

class Announcement(db.Model):
    __tablename__= 'announcement'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Announcement('{self.title}', '{self.date_posted}')"

class Moduls(db.Model):
    __tablename__= 'moduls'
    id = db.Column(db.Integer, primary_key=True)
    title_mo = db.Column(db.String(100), nullable=False)
    title_ch = db.Column(db.String(100), nullable=False)
    question_num = db.Column(db.Integer)
    question_str = db.Column(db.String(100))
    question_result = db.Column(db.Integer)
    question_option = db.Column(db.Integer, nullable=True)
    question_section = db.Column(db.String(100), nullable=True)
    date_exercise = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Moduls('{self.question_str}', '{self.question_result}', '{self.date_exercise}')"

class Emissions(db.Model):
    __tablename__= 'emissions'
    id = db.Column(db.Integer, primary_key=True)
    kms = db.Column(db.Float)
    transport = db.Column(db.String)
    fuel = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    co2= db.Column(db.Float)
    ch4= db.Column(db.Float)
    total = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Emissions('{self.kms}', '{self.transport}', '{self.fuel}', '{self.date}', '{self.co2}', '{self.ch4}', '{self.total}', '{self.user_id}')"
    
@app.before_first_request
def before_first_request(): 
    db.create_all()
