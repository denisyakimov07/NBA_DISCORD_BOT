import os
from dotenv import load_dotenv

load_dotenv()
load_dotenv(verbose=True)


class _Environment:

    def __init__(self):
        self.DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

        self.DB_DATABASE_TYPE = os.getenv('DB_DATABASE_TYPE')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_DATABASE = os.getenv('DB_DATABASE')


__environment = _Environment()


def get_env():
    return __environment
