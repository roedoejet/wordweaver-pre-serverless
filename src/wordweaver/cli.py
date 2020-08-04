import click

from wordweaver.data.utils import gzip_assets, i18n_add, i18n_extract, validate


@click.group()
def cli():
    '''Management script for WordWeaver'''

@click.option('--force/--no-force', default=False)
@click.argument('langs', nargs=-1)
@cli.command()
def extract_translations(langs, **kwargs):
    ''' Extract translations
    '''
    i18n_extract(langs, **kwargs)

@click.option('--force/--no-force', default=False)
@click.option('-i', '--input-asset', 'assets', multiple=True)
@click.argument('langs', nargs=-1)
@cli.command()
def add_translations(langs, **kwargs):
    ''' Add translations to assets
    '''
    i18n_add(langs, **kwargs)

@cli.command()
def validate():
    ''' Validate data against declared types
    '''
    validate()

@cli.command()
def compress():
    ''' Compress JSON Assets
    '''
    gzip_assets()
