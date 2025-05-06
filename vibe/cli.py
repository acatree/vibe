# vibe/cli.py..X
import click
from .build import build

@click.group()
def cli():
    pass

@cli.command(name='build')
@click.argument('filepath')
def build_cmd(filepath):
    """Build a Vibe file into HTML."""
    build(filepath)

if __name__ == '__main__':
    cli()
