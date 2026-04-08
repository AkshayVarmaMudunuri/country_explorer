
import requests

def get_country(name):
    url = f"https://restcountries.com/v3.1/name/{name}"
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            print(f"'{name}' not found. Check the Spelling.")
            return None

        response.raise_for_status()
        data = response.json()
        return data[0]

    except requests.exception.ConnectionError:
        print("No internet connection. Check your WiFi.")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out. Try again.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")
        return None

