import click



@click.group()
def cli():
    click.echo("\nYou are currently using Fitness Tracker App vIN_DEVELOPMENT\n")


@click.command()
@click.option("--name", prompt="Enter your name", help="Please enter your name into the test command")
def test_command(name):
    click.echo(f"Welcome my dear {name}")



cli.add_command(test_command)