# vibe/cli.py

import click
from .build import build

@click.command()
@click.argument('filepath')
def build_command(filepath):
    build(filepath)

if __name__ == '__main__':
    build_command()
