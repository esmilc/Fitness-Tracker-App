import sqlite3
from workout import Workout

db_file = 'fitness_tracker.db'
def init_db():
    conn = sqlite3.connect(db_file)    #Makes the connection, first step for a database
    c = conn.cursor()   #Cursor is always Next
    c.execute(""" CREATE TABLE IF NOT EXISTS workouts( 
              name TEXT NOT NULL, 
              main_muscle TEXT NOT NULL,
              sets INTEGER NOT NULL,
              weight INTEGER NOT NULL
              )
            """)
    # Must have IF NOT EXISTS because if not it will try to make a table that alr exists and throw an error
    conn.commit()
    conn.close()
def add_db(workout):
    #Possibly add a check to make sure that all of the data is filled out
   conn = sqlite3.connect(db_file)
   c = conn.cursor()
   c.execute('''INSERT INTO workouts (name, main_muscle, sets, weight) VALUES (?,?,?,?)''', (workout.name, workout.muscle, workout.sets, workout.weight))
   conn.commit()
   conn.close()

def clear_workouts():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''DELETE FROM workouts''')
    conn.commit()
    conn.close()



conn = sqlite3.connect(db_file)
c = conn.cursor()
c.execute("SELECT * FROM workouts")
rows = c.fetchall()
for row in rows:
    print(row)
