import pytz
from decouple import config

PYTHONPRO_DATABASE_URL = config("PYTHONPRO_DATABASE_URL")

ANALYTICS_DATABASE_URL = config("ANALYTICS_DATABASE_URL")

GOOGLE_ADS_SPREADSHEET_KEY = config("GOOGLE_ADS_SPREADSHEET_KEY")

PAGARME_API_KEY = config("PAGARME_API_KEY")

TIME_ZONE = pytz.timezone("America/Sao_Paulo")

TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")

