import click
from workout import *
from api_integration import search_by_name, search_by_muscle
from database import *

bold_start = "\033[1m"
bold_end = "\033[0m"

def print_log(list_of_workouts):
    count = 1
    click.echo("\n\n")
    for workout in list_of_workouts:
        click.echo(f"{count}){bold_start}{workout.name}{bold_end}")
        click.echo(f"  Muscle Group Trained: {workout.muscle}")
        click.echo(f"  You did {workout.sets} sets of {workout.weight} lbs per rep.\n\n")
        count += 1
def validate_1_or_2(input):
    if input != "1" and input != "2":
        raise click.BadParameter("Value not valid. Please enter 1 or 2.")
    return int(input)

def validate_y_or_n(input):
    if input != "y" and input != "n":
        raise click.BadParameter("Value not valid. Please enter y or n.")
    return (input)
def validate_digit(input):
    if input.isdigit():
        return int(input)
    raise click.BadParameter("Value not valid. Please enter a digit.")
def print_instructions(workouts, index_str):
    try:
        index = int(index_str) - 1
        click.echo("\n----------INSTRUCTIONS----------")
        click.echo(workouts[index].instructions)
        click.echo("------END OF INSTRUCTIONS-------\n")
    except ValueError:
        click.echo("ERROR...Please only type an Integer")
def list_workouts(list_of_workouts):
    count = 1
    for workout in list_of_workouts:
        click.echo(f"Workout #{count}:")
        click.echo(f"Name: {workout.name}\nDifficulty: {workout.difficulty}")
        click.echo(f"Muscle Group Trained: {workout.muscle}\n\n")
        count += 1


@click.group()
def cli():
    click.echo("\nYou are using vIN_DEVELOPMENT\n")


@cli.command()
@click.option("--name", '--n', prompt="Enter your name", help="Please enter your name into the test command")
def test_command(name):
    click.echo(f"Welcome {name}")

@cli.command()
@click.option("--muscle_group", "--mg", help="The muscle group to search for, please include intensity too.")
@click.option("--name", "--n", help="The name of workout to search for.")
@click.option("--difficulty", "--d", help="The difficulty of workout, please include muscle group too.")
def search_workout(name, muscle_group, difficulty):
    instructions = True
    if name:
        name = name.lower()
        workoutsJSON = search_by_name(name)
        #print(workoutsJSON)
        if workoutsJSON == -1:
            click.echo("No workouts found, please try another name.")
            return

        workouts = json_to_list(workoutsJSON) #Workouts is a list of workout instances
        click.echo()
        list_workouts(workouts)
        while instructions:
            instructions = click.prompt("Would you like to see instructions to a specific workout? (y/n)")
            if instructions != 'y' and instructions != "n":
                click.echo("Response not valid...Try Again")
                continue
            else:
                instructions = instructions == "y"
            if instructions:
                index_str = click.prompt("Enter the # of the workout ")
                print_instructions(workouts,index_str)



        #Search for the workouts by name and return

    elif muscle_group and difficulty:
        muscle_group = muscle_group.lower()
        difficulty = difficulty.lower()
        if muscle_group not in accepted_muscle_groups:
            click.echo("Muscle group not valid...Please see following list of muscle groups and try again.\n")
            for i in accepted_muscle_groups:
                click.echo(i)
            click.echo()
            instructions = False
            return

        if difficulty not in accepted_difficulty:
            click.echo("Difficulty not valid...Please see following list of difficulties and try again.\n")
            for i in accepted_difficulty:
                click.echo(i)
            click.echo()
            instructions = False
            return

        workoutJSON = search_by_muscle(muscle_group)
        allWorkouts = json_to_list(workoutJSON)
        filteredWorkouts = []
        for i in allWorkouts:
            if i.difficulty == difficulty:
                filteredWorkouts.append(i)
        if len(filteredWorkouts) == 0:
            click.echo("ERROR: No workouts that match that criteria found. Please modify search parameters.")
            return
        click.echo()
        list_workouts(filteredWorkouts)
        while instructions:
            instructions = click.prompt("Would you like to see instructions to a specific workout? (y/n)")
            if instructions != 'y' and instructions != "n":
                click.echo("Response not valid...Try Again")
                continue
            else:
                instructions = instructions == "y"
            if instructions:
                index_str = click.prompt("Enter the # of the workout ")
                print_instructions(filteredWorkouts, index_str)
        #Both were given, go and query

    elif muscle_group:
        muscle_group = muscle_group.lower()
        if muscle_group not in accepted_muscle_groups:
            click.echo("Muscle group not valid...Please see following list of muscle groups and try again.\n")
            for i in accepted_muscle_groups:
                click.echo(i)
            click.echo()
            instructions = False
            return

        difficulty =click.prompt("Enter difficulty of workout wanted ").lower()
        if difficulty not in accepted_difficulty:
            click.echo("Difficulty not valid...Please see following list of difficulties and try again.\n")
            for i in accepted_difficulty:
                click.echo(i)
            click.echo()
            instructions = False
            return

        workoutJSON = search_by_muscle(muscle_group)
        allWorkouts = json_to_list(workoutJSON)
        filteredWorkouts = []
        for i in allWorkouts:
            if i.difficulty == difficulty:
                filteredWorkouts.append(i)
        if len(filteredWorkouts) == 0:
            click.echo("ERROR: No workouts that match that criteria found. Please modify search parameters.")
            return
        click.echo()
        list_workouts(filteredWorkouts)
        while instructions:
            instructions = click.prompt("Would you like to see instructions to a specific workout? (y/n)")
            if instructions != 'y' and instructions != "n":
                click.echo("Response not valid...Try Again")
                continue
            else:
                instructions = instructions == "y"
            if instructions:
                index_str = click.prompt("Enter the # of the workout ")
                print_instructions(filteredWorkouts, index_str)



        #Ask for intensity and query

    elif difficulty:
        difficulty = difficulty.lower()
        if difficulty not in accepted_difficulty:
            click.echo("Difficulty not valid...Please see following list of difficulties and try again.\n")
            for i in accepted_difficulty:
                click.echo(i)
            click.echo()
            instructions = False
            return

        muscle_group = click.prompt("Enter muscle group of workout wanted ").lower()
        if muscle_group not in accepted_muscle_groups:
            click.echo("Muscle group not valid...Please see following list of muscle groups and try again.\n")
            for i in accepted_muscle_groups:
                click.echo(i)
            click.echo()
            instructions = False
            return

        workoutJSON = search_by_muscle(muscle_group)
        allWorkouts = json_to_list(workoutJSON)
        filteredWorkouts = []
        for i in allWorkouts:
            if i.difficulty == difficulty:
                filteredWorkouts.append(i)
        if len(filteredWorkouts) == 0:
            click.echo("ERROR: No workouts that match that criteria found. Please modify search parameters.")
            return
        click.echo()
        list_workouts(filteredWorkouts)
        while instructions:
            instructions = click.prompt("Would you like to see instructions to a specific workout? (y/n)")
            if instructions != 'y' and instructions != "n":
                click.echo("Response not valid...Try Again")
                continue
            else:
                instructions = instructions == "y"
            if instructions:
                index_str = click.prompt("Enter the # of the workout ")
                print_instructions(filteredWorkouts, index_str)
        #Ask for muscle group and query
    else:
        selection = click.prompt("Would you like to search by (1) name or by (2) muscle group and intensity?", value_proc=validate_1_or_2)

        if selection == 1: #Search by name algorithm
            name = click.prompt("Enter the name of the workout you'd like to search for")
            name = name.lower()
            workoutsJSON = search_by_name(name)
            # print(workoutsJSON)
            if workoutsJSON == -1:
                click.echo("No workouts found, please try another name.")
                return

            workouts = json_to_list(workoutsJSON)  # Workouts is a list of workout instances
            click.echo()
            list_workouts(workouts)
            while instructions:
                instructions = click.prompt("Would you like to see instructions to a specific workout? (y/n)")
                if instructions != 'y' and instructions != "n":
                    click.echo("Response not valid...Try Again")
                    continue
                else:
                    instructions = instructions == "y"
                if instructions:
                    index_str = click.prompt("Enter the # of the workout ")
                    print_instructions(workouts, index_str)

        else:

            muscle_group = click.prompt("Enter muscle group of workout wanted ").lower()
            if muscle_group not in accepted_muscle_groups:
                click.echo("Muscle group not valid...Please see following list of muscle groups and try again.\n")
                for i in accepted_muscle_groups:
                    click.echo(i)
                click.echo()
                instructions = False
                return

            difficulty = click.prompt("Enter difficulty of workout wanted ").lower()
            if difficulty not in accepted_difficulty:
                click.echo("Difficulty not valid...Please see following list of difficulties and try again.\n")
                for i in accepted_difficulty:
                    click.echo(i)
                click.echo()
                instructions = False
                return

            workoutJSON = search_by_muscle(muscle_group)
            allWorkouts = json_to_list(workoutJSON)
            filteredWorkouts = []
            for i in allWorkouts:
                if i.difficulty == difficulty:
                    filteredWorkouts.append(i)
            if len(filteredWorkouts) == 0:
                click.echo("ERROR: No workouts that match that criteria found. Please modify search parameters.")
                return
            click.echo()
            list_workouts(filteredWorkouts)
            while instructions:
                instructions = click.prompt("Would you like to see instructions to a specific workout? (y/n)")
                if instructions != 'y' and instructions != "n":
                    click.echo("Response not valid...Try Again")
                    continue
                else:
                    instructions = (instructions == "y")
                if instructions:
                    index_str = click.prompt("Enter the # of the workout ")
                    print_instructions(filteredWorkouts, index_str)
        #Nothing was given, ask what type of search and do search
@cli.command()
@click.option("--name", "--n", help="Enter the  name of the workout, if looking for workouts, use 'search-workout' function.")
def log_workout(name):
    if not name:
        name = click.prompt("Enter name of workout to log")
    workouts = search_by_name(name)
    try:
        workouts = json_to_list(workouts)
    except:
        print("Hey")
    if workouts == -1:
        click.echo("ERROR: No Workout was found, please check name inputted")
    else:
        list_workouts(workouts)
        index = click.prompt("Enter the # of the workout you'd like to log",value_proc=validate_digit)
        if not 0 < index <= len(workouts):
            click.echo("Number invalid...Try again")
            return
        toAdd = workouts[index-1]
        sets = click.prompt("Enter amount of sets", value_proc=validate_digit)
        weight = click.prompt("Enter amount of weight", value_proc=validate_digit)
        toAdd.sets = sets
        toAdd.weight = weight
        fname = click.prompt("Enter your first name")
        lname = click.prompt("Enter your last name")
        user_id = get_key(fname,lname)
        if user_id == -1:
            cont = click.prompt(f"No user was found with those parameters. Would you like to create a user acount as {fname} {lname}? (y/n)", value_proc=validate_y_or_n)
            if cont == 'y':
                add_user(fname,lname)
                user_id = get_key(fname,lname)
            else:
                click.echo("Goodbye!")
                return
        #ADD TO DATABASE
        add_db(toAdd, user_id)
        click.echo(f"\nSuccessfully added {toAdd.name} to the database. See you soon {fname}!\n\n")

@cli.command() #This is a temporary command, meant to make development easier
def search_log():
    fname = click.prompt("Enter the first name")
    lname = click.prompt("Enter the last name")
    query = query_user(fname,lname)
    if query == -1:
        click.echo("User not found with those parameters, try again")
        return
    query = query_formatting(query)
    print_log(query)


@cli.command()
def delete_database():
    purge_db()






#Argument is mandatory while option is optional