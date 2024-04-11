import socket
import handle_users
from flask import Flask, render_template, request, redirect, url_for
from functools import wraps
from flask import session
from create_database import *
#from werkzeug import secure_filename
app = Flask(__name__) 

@app.route("/")
def index():
    return render_template('index.html') 

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None or session.get('logged_in') is False:
            return redirect('/login',code=302)
        return f(*args, **kwargs)
    return decorated_function

def basic_user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None or session.get('logged_in') is False:
            return redirect('/login',code=302)
        elif session.get('admin') is True:
            return redirect('/admin_homepage',code=302)
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('admin') is None or session.get('admin') is False:
            return redirect('/login',code=302)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/signup', methods = ['GET', 'POST'])  
def sign_up():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        r = handle_users.create_user(username, password, 0)
        if (r == 1):
            msg = "Account created successfully"
            handle_users.print_values()
        else:
            msg = "Error creating account"
    return render_template('signup.html', msg = msg)

@app.route('/login', methods = ['GET', 'POST']) 
def log_in():  
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        r = handle_users.login_user(username, password)
        if (r == 1):
            session['logged_in'] = True
            session['username'] = username
            session['admin'] = False
            msg = "Log in successful"
            if(handle_users.is_admin(username) == 1):
                session['admin'] = True
                return redirect(url_for("admin_homepage"))
            return redirect(url_for('home_page'))
        else:
            msg = "Error logging in"
    return render_template('login.html', msg = msg)

@app.route('/logout')
@login_required
def log_out():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('admin', None)
    return redirect(url_for('log_in'))

@app.route('/deleteUser', methods = ['GET', 'POST'])
@admin_required
def delete_user():
    msg = ''
    if request.method == 'POST' and 'username' in request.form:
        username = request.form['username']
        r = handle_users.delete_user(username)
        if (r == 1):
            msg = "Delete user successful"
        else:
            msg = "Error deleting user"
    return render_template('delete_user.html', msg = msg)

@app.route('/getUser', methods = ['GET', 'POST'])
@admin_required
def get_user():
    msg = ''
    user = ''
    if request.method == 'POST' and 'username' in request.form:
        username = request.form['username']
        r = handle_users.get_user(username)
        if (r != None):
            r = r[0]
            msg = "Get user successful" 
            user = "user: ", r[0], "is admin: ", r[2]
        else:
            msg = "Error getting user"
    return render_template('get_user.html', msg = msg, user = user)

@app.route("/homepage")
@basic_user_required
def home_page():
    return render_template('homepage.html') 

@app.route("/admin_homepage")
@admin_required
def admin_homepage():
    return render_template('admin_homepage.html')  

#TODO: Allow file uploads, save to folder
@app.route('/fileupload', methods = ['POST'])   
def file_uploaded():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)   
        return render_template("give_macros.html", name = f.filename)   
  
if __name__=='__main__': 
   app.secret_key = 'your secret key'
   app.run(port=8080, debug=True) 