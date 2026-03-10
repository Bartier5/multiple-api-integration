import json
import time
import os

CACHE_FILE = "cache.json"

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE,'r') as f:
        return json.load(f)
def save_cache(data):
    payload = {
        "timestamp": time.time(),
        "data": data
    }
    with open(CACHE_FILE, 'w') as f:
        json.dump(payload, f)
def get_cache(ttl):
    cache = load_cache()
    if not cache:
        return None
    age = time.time() - cache["timestamp"]
    if age > ttl:
        return None
def clear_cache():
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
    
        