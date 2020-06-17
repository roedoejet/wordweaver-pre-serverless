import click
from wordweaver.data.utils import gzip_assets, validate

@click.group()
def cli():
    '''Management script for WordWeaver'''

@cli.command()
def validate_data():
    ''' See if data is clean
    '''
    validate()

@cli.command()
def init():
    ''' Initialize JSON Assets
    '''
    gzip_assets()
