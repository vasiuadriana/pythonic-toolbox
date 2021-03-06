import click
from datetime import datetime
import time


@click.command()
@click.option('--timestamp', '-t', type=click.FLOAT, help='Provide a timestamp to be converted')
def cdate(timestamp):
    try:
        click.echo(datetime.fromtimestamp(float(timestamp)))
    except TypeError:
        raise(click.BadParameter('Please provide a timestamp to be converted'))
    except ValueError:
        raise(click.BadParameter('Please provide a valid timestamp'))


@click.command()
@click.option('--date', '-d', type=click.STRING,
              help='Provide a date in format "Y-m-d H:m:s" to be converted',
              default=time.strftime('%Y-%m-%d %H:%M:%S'))
def timestamp(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        click.echo(date_obj.strftime("%s"))
    except ValueError:
        raise (click.BadParameter('Please provide a valid date in the format "Y-m-d H:M:S"'))