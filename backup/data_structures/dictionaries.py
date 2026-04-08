
raw_api_data = {
    "name":       {"common": "Japan", "official": "Japan"},
    "capital":    ["Tokyo"],
    "population": 125700000,
    "languages":  {"jpn": "Japanese"},
    "currencies": {"JPY": {"name": "Japanese yen", "symbol": "¥"}},
    "borders":    [],
    "flag":       "🇯🇵"
}

name = raw_api_data["name"]["common"]
capital = raw_api_data["capital"][0]
language = list(raw_api_data["languages"].values())[0]
currency = raw_api_data["currencies"]["JPY"]["name"]

region = raw_api_data.get("region", "Unknown")
