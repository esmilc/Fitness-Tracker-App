from database import init_db
from cli import cli

unsaved_workouts = []

# def welcome():
#     print('Welcome to my Fitness Tracker App!\n\n')
#     user_input = input("Would you like to start up the app? (y/n)  ")
#     if user_input == 'y':
#         return True
#     else:
#         return False

def main():
    init_db() #Initializing the database, where everything will be stored in
    cli() #This is what runs the command line tool

if __name__ == "__main__":
    main()