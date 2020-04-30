import os
from wwapi.data import __file__ as DATAROOT
from importlib import import_module
from wwapi.log import logger

DATA_DIR = os.path.dirname(DATAROOT)
WWLANG = os.environ['WWLANG']

if os.path.exists(os.path.join(DATA_DIR, os.environ['WWLANG'])):
    module = import_module(f'wwapi.data.{WWLANG}.models')
    Option = module.Option
    Pronoun = module.Pronoun
    Verb = module.Verb
    Response = module.Response
    ResponseObject = module.ResponseObject
else:
    logger.error(f"Can't find '{WWLANG}', are you sure you 'WWLANG' is defined in your environment?")
