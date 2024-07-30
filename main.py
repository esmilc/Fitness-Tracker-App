from database import init_workouts_db, init_users_db
from cli import cli

unsaved_workouts = []

def welcome():
    print('\n-----------------------------------')
    print('Welcome to my Fitness Tracker App!')
    print('-----------------------------------\n')


def main():
    init_users_db()
    init_workouts_db() #Initializing the workout database, where everything will be stored in
    cli() #This is what runs the command line tool


if __name__ == "__main__":
    welcome()
    main()
