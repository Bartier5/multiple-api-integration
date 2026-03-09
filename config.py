import argparse
from dotenv import load_dotenv
import os

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY","DEMO_KEY")

COINS = ["bitcoin","ethereum,","solana"]
URLS = {
    "crypto":"https://api.coingecko.com/api/v3/simple/price",
    "space":"https://api.nasa.gov/planetary/apod",
    "qoute":"https://api.quotable.io/random?tags=technology,success",
    
}
CACHE_TTL = 300 #5 minutes

def get_args():
    parser = argparse.ArgumentParser(description="DevPulse — Your daily dev dashboard")
    parser.add_argument("--coins", nargs="+", default=COINS, help="Coins to fetch e.g. --coins bitcoin solana")
    parser.add_argument("--no-cache", action="store_true", help="Skip cache and force fresh API calls")
    return parser.parse_args()
