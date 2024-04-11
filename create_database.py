import argparse
import sqlite3
from handle_users import *


def createDatabase():
    con = sqlite3.connect("user_databse.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, admin INT NOT NULL)")
    con.close()

