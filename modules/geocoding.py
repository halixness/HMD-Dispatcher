from typing import List, Any, Tuple
import urllib.parse
import requests

class Geocoding:

    @staticmethod
    def is_address_valid(query:str) -> bool:
        try:
            params = urllib.parse.urlencode({
                "q": query,
                "api_key": "659c357267680338147852zure325fe"
            }, doseq=True)
            resp = requests.get(url="https://geocode.maps.co/search", params=params)
            data = resp.json()
            print(data)
            return type(data) is list and len(data) > 0
        except:
            return True