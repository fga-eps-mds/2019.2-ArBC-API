from .settings import *
from .env import credentials
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)

#test enviroments variables
enviroments = 'prod'

""" if credentials.get('enviroment') == 'prod':
   from .prod import *
if credentials.get('enviroment') == 'dev':
   from .dev import * """