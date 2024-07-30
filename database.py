import sqlite3
import os
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
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            UNIQUE(first_name, last_name)
            )
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


def add_user(frst_name, lst_name):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO users(first_name, last_name) VALUES(?,?)''', (frst_name, lst_name))
    except sqlite3.IntegrityError as e:
        conn.commit()
        conn.close()
        return -1
    conn.commit()
    conn.close()

def user_exist(frst_name, last_name):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''SELECT COUNT(*) FROM users
                WHERE first_name = ? AND last_name = ?
                ''', (frst_name,last_name))
    count = c.fetchone()[0]
    conn.commit()
    conn.close()
    return count == 1

def get_key(frst_name, lst_name): #This is going to be the mother function...look for user, if not exists prompt user then add the user
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    if user_exist(frst_name,lst_name):
        c.execute('''SELECT * FROM users
        WHERE first_name = ? AND last_name = ?
        ''', (frst_name,lst_name))
        return c.fetchone()[0]
    else:
        return -1

def query_user(frstname, lstname):
    id = get_key(frstname,lstname)
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
# c.execute("SELECT * FROM workouts")
# rows = c.fetchall()
# for row in rows:
#     print(row)
query_user('Esmicl', 'Canet')
