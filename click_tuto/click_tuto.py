import click

@click.command()
@click.argument('src', nargs=-1)
@click.argument('dst', nargs=1)
def copy(src, dst):
    print(src)
    for fn in src:
        click.echo('move %s to folder %s' % (fn, dst))

copy()