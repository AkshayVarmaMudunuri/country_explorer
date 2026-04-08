import json
import os

CACHE_FILE = "data/cache.json"

def load_cache():
    os.makedirs("data", exist_ok= True)
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

cache = load_cache()

if "japan" in cache:
    country = cache["japan"]
else:
    country = get_country("japan")
    cache["japan"] = country
    save_cache(cache)

