import click
import os


@click.command()
def cli():
    print(os.system('time'))

if __name__ == '__main__':
    cli()
