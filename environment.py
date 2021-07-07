import os
from dotenv import load_dotenv

load_dotenv()
load_dotenv(verbose=True)


class _Environment:
    DISCORD_BOT_TOKEN: str

    def __init__(self):
        self.DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')


__environment = _Environment()


def get_env():
    return __environment
