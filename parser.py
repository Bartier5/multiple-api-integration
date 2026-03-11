from config import COINS
def parse_crypto(raw):
    if isinstance(raw, Exception):
        return{"error":"Crypto fetch failed"}
    result = {}
    for coin in raw:
        price =raw[coin].get("usd") or 0
        change = raw[coin].get("usd_24h_change") or 0
        result[coin] = {
            "price": round(price, 2),
            "change": round(change, 2),
        }
    return result
def parse_space(raw):
    if isinstance(raw,Exception):
        return{"error": "Space fetch failed"}
    return {
        "title": raw.get("title", "N/A"),
        "date":  raw.get("date", "N/A"),
        "explanation": raw.get("explanation", "N/A")[:300] + "...",  # trim long text
    }
def parse_quote(raw):
    if isinstance(raw, Exception):
        return {"error": "Quote fetch failed"}
    quote = raw[0]
    return {
        "text":   quote.get("q", "N/A"),
        "author": quote.get("a", "N/A"),
    }
def parse_all(raw_data):
    return {
        "crypto": parse_crypto(raw_data["crypto"]),
        "space":  parse_space(raw_data["space"]),
        "quote":  parse_quote(raw_data["quote"]),
    }