import requests
from .exceptions import APIConnectionError, PaysafeException

def make_request(method, url, headers=None, json=None):
    try:
        response = requests.request(method, url, headers=headers, json=json)
        if not response.ok:
            raise PaysafeException(f"Error: {response.status_code} - {response.text}")
        return response.json()
    except requests.exceptions.RequestException as e:
        raise APIConnectionError(f"Connection failed: {str(e)}")
