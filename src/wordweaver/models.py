import os
from importlib import import_module

from wordweaver.data import DEFAULT_LANG
from wordweaver.data import __file__ as DATAROOT
from wordweaver.log import logger

DATA_DIR = os.path.dirname(DATAROOT)
WWLANG = os.environ.get("WWLANG", DEFAULT_LANG)

if os.path.exists(os.path.join(DATA_DIR, WWLANG)):
    module = import_module(f"wordweaver.data.{WWLANG}.models")
    Option = module.Option
    Pronoun = module.Pronoun
    Verb = module.Verb
    Response = module.Response
    ResponseObject = module.ResponseObject
else:
    logger.error(
        f"""Can't find '{WWLANG}', are you sure you 'WWLANG' is
        defined in your environment?"""
    )
