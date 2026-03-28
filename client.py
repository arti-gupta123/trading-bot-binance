from dotenv import load_dotenv
load_dotenv()

from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    return Client(
        api_key,
        api_secret,
        testnet=True
    )
print("API KEY:", os.getenv("API_KEY"))