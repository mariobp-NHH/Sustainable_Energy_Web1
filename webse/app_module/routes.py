import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import app, db, bcrypt
from webse.app_module.forms import ChatFormUpdate
from webse.app_module.forms import ModulsForm_m1_ch1_q1, ModulsForm_m1_ch1_q2, ModulsForm_m1_ch1_q3
from webse.app_module.forms import ModulsForm_m1_ch2_q1, ModulsForm_m1_ch2_q2, ModulsForm_m1_ch2_q3, ModulsForm_m1_ch2_q4, ModulsForm_m1_ch2_q5
from webse.models import Userpage, Moduls, Announcement, Chat, Emissions
from flask_login import login_user, current_user, logout_user, login_required

app_module = Blueprint('app_module', __name__)

#################################
####   Block 9. App Module   ####
#################################
# App web
@app_module.route('/app_web')
@login_required
def app_web():
	return render_template('app web/app_web.html', title='App Web')

# App Module, Chapter 1.
@app_module.route('/app_web/ch1', methods=['GET', 'POST'])
@login_required
def app_web_ch1():
    return render_template('app web/ch1/app_web_ch1.html', title='App Web - Ch1')

# App Module, Chapter 2.
@app_module.route('/app_web/ch2', methods=['GET', 'POST'])
@login_required
def app_web_ch2():
    return render_template('app web/ch2/app_web_ch2.html', title='App Web - Ch2')

