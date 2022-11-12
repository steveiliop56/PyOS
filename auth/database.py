import sqlite3
from accountmgmt import *

db = sqlite3.connect("credentials.db")
cursor = db.cursor()

what(db, cursor)