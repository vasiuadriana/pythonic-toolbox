import click
import os


@click.command()
@click.argument('directory', required=False)
def cleanup_pyc(directory):
    if directory:
        current_directory = os.getcwd()
        os.chdir(os.path.realpath(directory))
        os.system('find . -name \*.pyc -delete')
        os.chdir(current_directory)
    else:
        os.system('find . -name \*.pyc -delete')


if __name__ == "__main__":
    cleanup_pyc()