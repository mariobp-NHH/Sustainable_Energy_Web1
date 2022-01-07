from flask import render_template, url_for, flash, redirect, request, abort
from webse import app


@app.route('/home')
@app.route('/')
# Declare the main function
def home():
	return render_template('home.html', title='Home')





# App Calculator form
@app.route('/app_calculator')
def app_calculator():
	return render_template('app_calculator.html', title='App Calculator')

# App Calculator routine
@app.route('/send1', methods=['POST'])
def send(sum=sum):
	num1 = request.form.get("num1")
	num2 = request.form.get("num2")
	oper_name = request.form.get("operation")

	num1 = float(num1)
	num2 = float(num2)
	if oper_name == "add":
		oper_result = num1 + num2
	elif oper_name == "subtract":
		oper_result = num1 - num2
	elif oper_name == "multiply":
		oper_result = num1 * num2
	elif oper_name == "divide":
		oper_result = num1 / num2

	return render_template ('app_calculator.html', sum=oper_result)


@app.route('/teachers')
def teachers():
	return render_template('teachers.html', title='Teachers')


# App web
@app.route('/app_web')
def app_web():
	return render_template('app_web.html', title='App Web')

# App web. Module 1.
@app.route('/app_web/module1')
def app_web_module1():
	return render_template('app_web_module1.html', check="20", title='App Web Module1')

# App web. Module 1. Exercise 1.
@app.route('/app_web/module1/ex1', methods=['POST'])
def app_web_module1_ex1():
	if request.method == "POST":
		num1 = request.form.get("num1")

		num1 = float(num1)
		if num1 == 2:
			answ = "right"
		else:
			answ = "wrong"
		return render_template('app_web_module1.html', check=answ)
	else:
		return render_template('app_web_module1.html', check="20")

# Sustainable Energy Web
@app.route('/sustainable_energy_web')
def sustainable_energy_web():
	return render_template('sustainable_energy_web.html', title='SE Web')