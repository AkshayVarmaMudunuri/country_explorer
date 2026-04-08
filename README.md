# Country Explorer

A Python command-line app that fetches real data about any country in the world using the REST Countries API.

## What it does
- Look up any of 250+ countries by name
- Compare two countries side by side
- Browse all countries in a region
- Generate population charts with matplotlib
- Saves results to a local cache (no repeated API calls)

## How to run
pip install -r requirements.txt
python main.py


## API used
REST Countries API — restcountries.com
Free, no key needed, no signup required.

## What I built this with
- Python 3.11
- requests (API calls)
- pandas (data analysis)
- matplotlib (charts)
- pytest (testing)