import asyncio
from config import get_args, CACHE_TTL
from fetcher import fetch_all
from parser import parse_all
from combiner import combine
from display import display_all
from cache import get_cache, save_cache, clear_cache

async def main():
    args = get_args()
    if args.no_cache:
        clear_cache()
    cached = get_cache(CACHE_TTL)
    if cached:
        print("\n loaded from cache")
        display_all(cached)
        return
    print("\n  Fetching data...\n")
    raw_data    = await fetch_all(args.coins)
    parsed_data = parse_all(raw_data)
    combined    = combine(parsed_data)
    save_cache(combined)

    display_all(combined)


if __name__ == "__main__":
    asyncio.run(main())