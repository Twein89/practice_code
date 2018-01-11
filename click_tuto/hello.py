import click
import os

class Repo(object):
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = debug

@click.group()
@click.option('--repo-home', envvar='REPO_HOME', default='.repo')
@click.option('--debug/--no-debug', default=False,
              envvar='REPO_DEBUG')
@click.pass_context
def cli(ctx, repo_home, debug):
    ctx.obj = Repo(repo_home, debug)


@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
@click.pass_obj
def clone(repo, src, dest):
    print(repo.home)
    print(repo.debug)

if __name__ == '__main__':
    cli()
