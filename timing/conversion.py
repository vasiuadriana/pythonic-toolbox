import click
from datetime import datetime


@click.command()
@click.option('--timestamp', default=1.0, help='Provide a timestamp to be converted')
def cdate(timestamp):
    click.echo(datetime.fromtimestamp(float(timestamp)))

if __name__ == '__main__':
    cdate()
