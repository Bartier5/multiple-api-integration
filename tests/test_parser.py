import pytest
from parser import parse_crypto, parse_space, parse_quote


def test_parse_crypto_success():
    raw = {
        "bitcoin":  {"usd": 65000.12, "usd_24h_change": 2.34},
        "ethereum": {"usd": 3200.45,  "usd_24h_change": -1.12},
    }
    result = parse_crypto(raw)
    assert result["bitcoin"]["price"]  == 65000.12
    assert result["ethereum"]["change"] == -1.12


def test_parse_crypto_failure():
    result = parse_crypto(Exception("API down"))
    assert "error" in result


def test_parse_space_success():
    raw = {"title": "Black Hole", "date": "2024-01-01", "explanation": "A" * 400}
    result = parse_space(raw)
    assert result["title"] == "Black Hole"
    assert len(result["explanation"]) == 303  # 300 chars + "..."


def test_parse_space_failure():
    result = parse_space(Exception("API down"))
    assert "error" in result


def test_parse_quote_success():
    raw = {"content": "Code is art.", "author": "Someone"}
    result = parse_quote(raw)
    assert result["text"]   == "Code is art."
    assert result["author"] == "Someone"


def test_parse_quote_failure():
    result = parse_quote(Exception("API down"))
    assert "error" in result