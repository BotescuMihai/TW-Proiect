from flask import Flask, render_template, request, redirect, url_for, session
import os
import random
from flask import url_for
from data_manager import *

app = Flask(  # Create a flask app
	__name__,
	template_folder='',  # Name of html file folder
	static_folder=''  # Name of directory for static files
)

@app.route('/contact')
def contact_page():
  return render_template('contact_us.html')

@app.route('/about')
def about_page():
  return render_template('about.html')

"""
@app.route('/login',methods=['GET','POST'])
def login_page():
  username = request.form.get("email","")
  password = request.form.get("password","")
  valid, function =  check_account_credentials(username,password,'data_files/accounts.json')[0], check_account_credentials(username,password,'data_files/accounts.json')[1]

  if valid == True:
    if function == "doctor": #return redirect(url_for('/doctor'))
      return redirect(render_template('doctor.html'), title='Doctor')
    elif function == "nurse":
      return redirect(render_template('asistent.html',title='Asistent'))
    elif function == "receptionist":
      return redirect(receptionist_page())
  ### passing the data to the log file
  with open('login_datas.log','a+') as f:
    f.write(username + "\n" + password)
  return render_template('login.html')
"""

@app.route('/admin')
def admin_page():
  return render_template('index.html')


@app.route('/login', methods=['POST','GET'])
def login():
  if request.method == 'GET':
    print('intram pe GET')
    return render_template('login.html')
  if request.method == 'POST':
    print('intram pe post')
    username = request.form['email']
    password = request.form['password']
    datas = check_account_credentials(username,password,'data_files/accounts.json')
    if datas[0] == True:
      return redirect(url_for(datas[1]))


@app.route('/')
def home_page():
  return render_template('index.html')

@app.route('/doctor')
def doctor():
  return render_template('doctor.html')

@app.route('/pacient_appointment')
def pacient_appointment_page():
  return render_template('pacient_appointment.html')


@app.route('/receptioner')
def receptionist():
  return render_template('receptioner.html')

@app.route('/nurse')
def nurse():
  return render_template('asistent.html')
 
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=8080  # Randomly select the port the machine hosts on.
	)