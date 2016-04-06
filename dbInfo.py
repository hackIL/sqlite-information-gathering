#!/usr/bin/env python
#get information about sqlite DB
import sqlite3

__author__ = "Matan"
__version__ = "1.0.0"
__maintainer__ = "Matan"

con = sqlite3.connect('C:\Users\matan\AppData\Local\Google\Chrome\User Data\Default\Login Data')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
cursor.execute("SELECT * FROM logins;")
list(map(lambda x: x[0], cursor.description))
cursor.execute("PRAGMA table_info(logins);")
print(cursor.fetchall())
