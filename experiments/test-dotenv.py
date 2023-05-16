# Rename `os.environ` to `env` for nicer code
from os import environ as env

from dotenv import load_dotenv

# Default name for the file is ".env"
load_dotenv()

# This is for testing as .gitignore ignores .env:
load_dotenv(".env-TEMPLATE")

print('API_KEY:  {}'.format(env['API_KEY']))
print('HOSTNAME: {}'.format(env['HOSTNAME']))
print('PORT:     {}'.format(env['PORT']))

