
import requests

def get_country(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url, timeout=10)

    print(f'Status code: {response.status_code}')

    data = response.json()
    country = data[0]
    return country

result = get_country("Japan")
print(result["name"]["common"])
print(result["capital"][0])

