from flask import render_template, request
from ene425 import app

@app.route('/')
@app.route("/home")
def home():
	return "hello"

