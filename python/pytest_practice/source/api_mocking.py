from http.client import HTTPException

import requests

def get_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200 :
        return response.json()

    raise requests.HTTPError()