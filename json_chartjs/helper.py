import sqlite3

def get_db_connection():
   db = sqlite3.connect("workout.db", check_same_thread=False)
   db.row_factory = sqlite3.Row
   return db

def default(obj):
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')