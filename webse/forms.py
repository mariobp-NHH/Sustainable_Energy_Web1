from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from webse.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    group = SelectField('Group', validators=[DataRequired()],
                       choices=[('0', '0'),
                                ('1', '1'),
                                ('2', '2')])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat-Post')

class AnnouncementForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Annoucement')

#App Statistics
class AppStatisticsForm(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                        choices=[('Ch1. Introduction', 'Ch1. Introduction'),
                                 ('Ch2. Installation', 'Ch2. Installation')])
    submit = SubmitField('App Module Statistics')

#Sustainable Energy Statistics
class SEStatisticsForm(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                        choices=[('Ch1. Overview', 'Ch1. Overview'),
                                 ('Ch2. Wind', 'Ch2. Wind')])
    submit = SubmitField('Sustainable Energy Module Statistics')

#M1_Ch1
class ModulsForm_M1_Ch1_Q1(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Python', 'Python'),
                                ('HTML', 'HTML')])
    submit = SubmitField('Programming Language')

class ModulsForm_M1_Ch1_Q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('GitHub', 'GitHub'),
                                ('Heroku', 'Heroku')])
    submit = SubmitField('Server')

class ModulsForm_M1_Ch1_Q3(FlaskForm):
    type = RadioField(choices=['Easy', 'Medium', 'Difficult'],
                       validators=[InputRequired()])
    submit = SubmitField('Implementation')

#M1_Ch2
class ModulsForm_M1_Ch2_Q1(FlaskForm):
    identifier = StringField()
    question_str = StringField('App Module, Chapter 2, Question 1', validators=[DataRequired()])
    submit1 = SubmitField('Check')

class ModulsForm_M1_Ch2_Q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('wind', 'wind'),
                                ('solar', 'solar')])
    submit = SubmitField('Type Energy')

class ModulsForm_M1_Ch2_Q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                                choices=[('income', 'income'),
                                        ('expense', 'expense')])
    submit = SubmitField('Type Income')

class ModulsForm_M1_Ch2_Q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                                choices=[('university', 'university'),
                                        ('school', 'school')])
    submit = SubmitField('Type Work')

class ModulsForm_M1_Ch2_Q5(FlaskForm):
    type = RadioField('Level',
                       choices=['Petrol', 'Electric', 'Hydrogen'],
                       validators=[InputRequired()])
    submit = SubmitField('Type type')

#M2_Ch1
class ModulsForm_M2_Ch1_Q1(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Europe', 'Europe'),
                                ('Africa', 'Africa')])
    submit = SubmitField('Continent')

class ModulsForm_M2_Ch1_Q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Local', 'Local'),
                                ('National', 'National')])
    submit = SubmitField('Geographical Level')

class ModulsForm_M2_Ch1_Q3(FlaskForm):
    type = RadioField(choices=['Easy', 'Medium', 'Difficult'],
                       validators=[InputRequired()])
    submit = SubmitField('Implementation')

#M2_Ch2
class ModulsForm_M2_Ch2_Q1(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Europe', 'Europe'),
                                ('Africa', 'Africa')])
    submit = SubmitField('Continent')

class ModulsForm_M2_Ch2_Q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Local', 'Local'),
                                ('National', 'National')])
    submit = SubmitField('Geographical Level')

class ModulsForm_M2_Ch2_Q3(FlaskForm):
    type = RadioField(choices=['Easy', 'Medium', 'Difficult'],
                       validators=[InputRequired()])
    submit = SubmitField('Implementation')