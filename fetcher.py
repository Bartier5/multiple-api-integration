import asyncio
import aiohttp
from config import URLS, NASA_API_KEY, COINS

async def fetch_crypto(session, coins):
    params = {
        "ids": ",".join(coins),       # e.g. "bitcoin,ethereum,solana"
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    async with session.get(URLS["crypto"], params=params) as response:
        return await response.json()
    
async def fetch_space(session):
    params = {"api_key": NASA_API_KEY}
    async with session.get(URLS["space"], params=params) as response:
        return await response.json()


async def fetch_quote(session):
    headers = {"User-Agent": "Mozilla/5.0"}
    async with session.get(URLS["quote"], headers=headers) as response:
        return await response.json(content_type=None)


async def fetch_all(coins=COINS):
    # aiohttp.ClientSession is the async version of a requests session
    async with aiohttp.ClientSession() as session:
        # asyncio.gather fires all 3 coroutines at the same time
        results = await asyncio.gather(
            fetch_crypto(session, coins),
            fetch_space(session),
            fetch_quote(session),
            return_exceptions=True  # if one fails, others still return
        )
    return {
        "crypto": results[0],
        "space":  results[1],
        "quote":  results[2],
    }