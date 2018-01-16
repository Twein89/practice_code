import click
import os

@click.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
def digest(hash_type):
    print(hash_type)
    click.echo(hash_type)

if __name__ == '__main__':
    digest()
