from dotenv import load_dotenv
import os

load_dotenv('.env', override=True)

COMPLETIONS_MODEL = os.getenv('COMPLETIONS_MODEL')
API_EXCHANGE_VERSION = os.getenv('API_EXCHANGE_VERSION')
API_BASE_URL = os.getenv('API_BASE_URL')

EMBEDDINGS_MODEL = os.getenv('EMBEDDINGS_MODEL')
EMBEDDINGS_BASE_URL = os.getenv('EMBEDDINGS_BASE_URL')

TOKEN_ID = os.getenv('TOKEN_ID')
TOKEN_SECRET = os.getenv('TOKEN_SECRET')
