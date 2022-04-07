import sqlite3

def get_db_connection():
   db = sqlite3.connect("workout.db", check_same_thread=False)
   db.row_factory = sqlite3.Row
   return db