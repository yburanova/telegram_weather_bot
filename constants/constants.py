import os

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_TOKEN')
WEATHER_OPENAPI_TOKEN = os.environ.get('WEATHER_OPENAPI_TOKEN')


def is_token_set():
    return TELEGRAM_BOT_TOKEN is not None and WEATHER_OPENAPI_TOKEN is not None


