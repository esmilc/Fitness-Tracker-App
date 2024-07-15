import click
from workout import *
from api_integration import search_by_name, search_by_muscle


def validate_muscleGroup(muscle):
    if muscle not in accepted_muscle_groups:
        raise click.BadParameter("Invalid muscle group. Use show_muscles to see a list of all muscle groups.")
    return muscle
@click.group()
def cli():
    click.echo("\nYou are using vIN_DEVELOPMENT\n")


@cli.command()
@click.option("--name", '--n', prompt="Enter your name", help="Please enter your name into the test command")
def test_command(name):
    click.echo(f"Welcome! {name}")

@cli.command()
@click.option("--muscle_group", "--mg", help="The muscle group to search for, please include intensity too.")
@click.option("--name", "--n", help="The name of workout to search for.")
@click.option("--difficulty", "--d", help="The difficulty of workout, please include muscle group too.")
def search_workout(name, muscle_group, difficulty):
    instructions = True
    if name:
        workoutsJSON = search_by_name(name)
        print(workoutsJSON)
        if workoutsJSON == -1:
            click.echo("No workouts found, please try another name.")
            return

        workouts = json_to_list(workoutsJSON) #Workouts is a list of workout instances
        count = 1
        for workout in workouts :
            click.echo(f"Workout #{count}:")
            click.echo(f"Name: {workout.name}\nDifficulty: {workout.difficulty}")
            click.echo(f"Muscle Group Trained: {workout.muscle}\n\n")
            count +=1
        while instructions:
            instructions = click.prompt("Would you like to see instructions to a specific workout? (y/n)")
            if instructions != 'y' and instructions != "n":
                click.echo("Response not valid...Try Again")
                continue
            else:
                instructions = instructions == "y"
            if instructions:
                index_str = click.prompt("Enter the # of the workout: ")
                try:
                    index = int(index_str) - 1
                    click.echo("\n----------INSTRUCTIONS----------")
                    click.echo(workouts[index].instructions)
                    click.echo("------END OF INSTRUCTIONS-------\n")
                except ValueError:
                    click.echo("ERROR...Please only type an Integer")




        #Search for the workouts by name and return

    elif muscle_group and difficulty:
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
        count = 1
        for workout in filteredWorkouts:
            click.echo(f"Workout #{count}:")
            click.echo(f"Name: {workout.name}\nDifficulty: {workout.difficulty}")
            click.echo(f"Muscle Group Trained: {workout.muscle}\n\n")
            count += 1
        while instructions:
            instructions = click.prompt("Would you like to see instructions to a specific workout? (y/n)")
            if instructions != 'y' and instructions != "n":
                click.echo("Response not valid...Try Again")
                continue
            else:
                instructions = instructions == "y"
            if instructions:
                index_str = click.prompt("Enter the # of the workout: ")
                try:
                    index = int(index_str) - 1
                    click.echo("\n----------INSTRUCTIONS----------")
                    click.echo(filteredWorkouts[index].instructions)
                    click.echo("------END OF INSTRUCTIONS-------\n")
                except ValueError:
                    click.echo("ERROR...Please only type an Integer")
        #Both were given, go and query

    elif muscle_group:
        if muscle_group not in accepted_muscle_groups:
            click.echo("Muscle group not valid...Please see following list of muscle groups and try again.\n")
            for i in accepted_muscle_groups:
                click.echo(i)
            click.echo()
            instructions = False
            return
        difficulty = click.prompt("Enter difficulty of workout wanted: ", value_proc=validate_muscleGroup) #FIXME

        #Ask for intensity and query

    elif difficulty:
        pass
        #Ask for muscle group and query
    else:
        pass
        #Nothing was given, ask what type of search and do search



cli.add_command(test_command)

#Argument is mandatory while option is optional