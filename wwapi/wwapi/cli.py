import click

from loguru import logger
from wwapi.data.utils import initialize_db, validate

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
    ''' Initialize Database
    '''
    initialize_db()
