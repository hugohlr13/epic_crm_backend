import click
from controllers.authenticate_user import authenticate_user

@click.group()
def cli():
    pass

@click.command()
@click.option('--email', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def login(email, password):
    """
    Command to authenticate a user.
    """
    token = authenticate_user(email, password)
    if token:
        click.echo("Authentification réussie. Token : " + token)
    else:
        click.echo("Échec de l'authentification.")

cli.add_command(login)

if __name__ == '__main__':
    cli()
