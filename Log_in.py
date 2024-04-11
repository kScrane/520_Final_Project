import sqlite3
import hashlib
from create_database import *
"""User authentication and authorization.
There are two types of users: 
- one uses the system   
- one manages the system (referred to as administrators). 
Both need to log in to use the system. Users need to register before using the system or be added to
the system by administrators. The default administrator has the username is as and password as
admin. After the first login, the system should prompt admin to change the password. The
default administrator has the privilege to add new administrators and users. Administrators can
retrieve all users’ evaluations and compute the average score for each perspective across the
entire user base or selected users"""

def login_user(username, password):
    con = sqlite3.connect("user_databse.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    if cur.fetchall():
        con.close()
        return 1
    else:
        con.close()
        return 0

def handle_login(c):
    c.send("Input Username".encode())
    username = c.recv(1024).decode()
    c.send("Input Password".encode())
    #TODO: Hash password on site
    #password = c.recv(1024).decode()
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()
    r = login_user(username, password)
    if r == 1:
        c.send("Successful".encode())
    else:
        c.send("Unsuccessful".encode())

def print_values():
    con = sqlite3.connect("user_databse.db")
    # display row by row 
    cursor = con.execute("SELECT * from users") 
    for row in cursor: 
        print(row)
    # close the connection 
    con.close() 

def handle_create_user(c):
    """Add user, password to user database
    TODO: Only accessible to admins
    """
    c.send("Input Username".encode())
    username = c.recv(1024).decode()
    c.send("Input Password".encode())
        #password = c.recv(1024).decode()
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()
    r = create_user(username, password)
    
    if r == 0:
        c.send("Unsuccessful - User already exists".encode())
    else:
        c.send("Successful".encode())
    return

def create_user(username, password, admin):
    con = sqlite3.connect("user_databse.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cur.fetchall(): #Successful
        con.close()
        return 0
    else: 
        con.execute("INSERT INTO users VALUES(?, ?, ?)", (username, password, admin))
        con.commit()
        con.close()
        return 1

def delete_user(username):
    con = sqlite3.connect("user_databse.db")
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE username = ?", (username,))
    con.commit()
    con.close()
    return 1

def get_user(username):
    con = sqlite3.connect("user_databse.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchall()
    con.close()
    if user != None: #Successful
        return user
    else: 
        user = None
    return user
def is_admin(username):
    con = sqlite3.connect("user_databse.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchall()
    con.close()
    if user != None: #Successful
        isAdmin = user[0][2]
    else: 
        isAdmin = 0
    return isAdmin
