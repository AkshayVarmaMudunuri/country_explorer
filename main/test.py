import requests

print("Testing your setup...")

url = "https://restcountries.com/v3.1/name/india"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    country = data[0]
    print("Success! Here is some data:")
    print("Country:", country["name"]["common"])
    print("Capital:", country["capital"][0])
    print("Population:", country["population"])
    print("Setup is working correctly!")
else:
    print("Something went wrong. Check your internet connection.")