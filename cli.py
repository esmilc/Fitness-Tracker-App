import click



@click.group()
def cli():
    click.echo("\nYou are using vIN_DEVELOPMENT\n")


@click.command()
@click.option("--name", '--n', prompt="Enter your name", help="Please enter your name into the test command")
def test_command(name):
    click.echo(f"Welcome  {name}")



cli.add_command(test_command)