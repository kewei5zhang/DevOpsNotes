import requests


def get_cities(key):
    response = requests.get(f'https://api.teleport.org/api/cities/?search={key}')

    # If the response was successful, no Exception will be raised
    response.raise_for_status()

    cities = [city['matching_full_name'] for city in response.json()["_embedded"]["city:search-results"]]

    return str(cities)
