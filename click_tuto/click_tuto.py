import click

@click.command()
@click.option('--username')
def greet(username):
    click.echo('Hello %s!' % username)

if __name__ == '__main__':
    greet(auto_envvar_prefix='GREETER')