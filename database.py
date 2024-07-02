import sqlite3
from workout import Workout

db_file = 'fitness_tracker.db'
def init_db():
    conn = sqlite3.connect(db_file)    #Makes the connection, first step for a database
    c = conn.cursor()   #Cursor is always Next
    c.execute(""" CREATE TABLE IF NOT EXISTS workouts( 
              name TEXT NOT NULL, 
              main_muscle TEXT NOT NULL,
              duration INTEGER NOT NULL
              )
            """)
    # Must have IF NOT EXISTS because if not it will try to make a table that alr exists and throw an error
    conn.commit()
    conn.close()
def add_db(workout):
   conn = sqlite3.connect(db_file)
   c = conn.cursor("INSERT INTO workouts VALUES (workout.name, workout.muslce, muscle.duration)")

