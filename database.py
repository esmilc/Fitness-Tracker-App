import sqlite3

def init_db():
    conn = sqlite3.connect('fitness_tracker.db')
    c = conn.curor()
    c.execute(""" CREATE TABLE IF NOT EXISTS workouts
              (
              name TEXT NOT NULL, 
              main_muscle TEXT NOT NULL,
              duration INTEGER NOT NULL,
              )
            """)
    