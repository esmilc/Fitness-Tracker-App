import sqlite3
import os
import bcrypt
from workout import Workout

db_file = 'fitness_tracker.db'
def init_workouts_db():
    conn = sqlite3.connect(db_file)    #Makes the connection, first step for a database
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()   #Cursor is always Next
    c.execute(""" CREATE TABLE IF NOT EXISTS workouts( 
              name TEXT NOT NULL, 
              main_muscle TEXT NOT NULL,
              sets INTEGER NOT NULL,
              weight INTEGER NOT NULL,
              user_id INTEGER NOT NULL,
              FOREIGN KEY (user_id) REFERENCES users(id)
              )
            """)
    # Must have IF NOT EXISTS because if not it will try to make a table that alr exists and throw an error
    conn.commit()
    conn.close()

def init_users_db():
    conn = sqlite3.connect(db_file) #Must always establish connection first, then cursor
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            UNIQUE(username))
            """)
    conn.commit()
    conn.close()
def add_db(workout, userID):
    #Possibly add a check to make sure that all of the data is filled out
   conn = sqlite3.connect(db_file)
   c = conn.cursor()
   c.execute('''INSERT INTO workouts (name, main_muscle, sets, weight, user_id) VALUES (?,?,?,?,?)''', (workout.name, workout.muscle, workout.sets, workout.weight, userID))
   conn.commit()
   conn.close()

def purge_db():
    if os.path.exists(db_file):
        os.remove(db_file)
        print('DATABASE WAS SUCCESSFULLY DELETED')
    #
    # conn = sqlite3.connect(db_file)
    # c = conn.cursor()
    # c.execute('''DELETE FROM workouts''')
    # c.execute('''DELETE FROM users''')
    # conn.commit()
    # conn.close()
    # 





def user_exist(username):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''SELECT COUNT(*) FROM users
                WHERE username = ?
                ''', (username,))
    count = c.fetchone()[0]
    conn.commit()
    conn.close()
    return count == 1

def create_user(username, password):
    if user_exist(username):
        return -1
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    encoded_pass = password.encode('utf-8')
    hashed = bcrypt.hashpw(encoded_pass, bcrypt.gensalt())
    c.execute('''INSERT INTO users(username, password) VALUES (?,?)''', (username, hashed))
    conn.commit()
    conn.close()

def get_key(username, password): #This is going to be the mother function...look for user, if not exists prompt user then add the user
    enc_password = password.encode('utf-8')
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    if user_exist(username):
        c.execute('''SELECT * FROM users
        WHERE username = ?''', (username,))
        row = c.fetchone()
        if bcrypt.checkpw(enc_password, row[2]):
            return row[0]
        conn.close()
        return -2
    else:
        conn.close()
        return -1

def query_user(user, passw):
    id = get_key(user,passw)
    if id == -1:
        return -1

    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''SELECT * FROM workouts
            WHERE user_id = ?''', (id,))
    all = c.fetchall()
    conn.close()
    return all



# conn = sqlite3.connect(db_file)
# c = conn.cursor()
# c.execute("SELECT * FROM users")
# rows = c.fetchall()
# for row in rows:
#     print(row)
# print(get_key('ecanet', "1234"))
