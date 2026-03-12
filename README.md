# Multiple API Integration — DevPulse CLI

A Python CLI dashboard that fetches live data from multiple APIs concurrently
using asyncio and displays a clean, color-coded summary in the terminal.

## Features
- Live crypto prices and 24h change (BTC, ETH, SOL) via CoinGecko
- NASA Astronomy Picture of the Day space fact
- Daily inspirational quote via ZenQuotes
- Concurrent API calls with asyncio and aiohttp
- Simple file-based caching (5 minute TTL)
- CLI flags for custom coins and cache control
- Unit tested with pytest

## Project Structure
```
multiple-api-integration/
├── config.py
├── fetcher.py
├── parser.py
├── combiner.py
├── cache.py
├── display.py
├── main.py
├── conftest.py
├── requirements.txt
└── tests/
    └── test_parser.py
```

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/Bartier5/multiple-api-integration.git
cd multiple-api-integration
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file
```
NASA_API_KEY=your_key_here
```
Get your free NASA key at: https://api.nasa.gov

## Usage
```bash
# Run with default coins (BTC, ETH, SOL)
python main.py

# Run with custom coins
python main.py --coins bitcoin solana

# Skip cache and force fresh fetch
python main.py --no-cache
```

## Running Tests
```bash
pytest tests/
```

## Technologies
- Python 3.12
- aiohttp — async HTTP requests
- asyncio — concurrent execution
- colorama — terminal colors
- tabulate — table formatting
- python-dotenv — environment variables