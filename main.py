from database import init_db
from cli import cli

unsaved_workouts = []

def welcome():
    print('-----------------------------------')
    print('Welcome to my Fitness Tracker App!')
    print('-----------------------------------\n')


def main():
    init_db() #Initializing the database, where everything will be stored in
    cli() #This is what runs the command line tool
def goodbye():
    print("Thank you for using Fitness Tracker App!")

if __name__ == "__main__":
    welcome()
    main()