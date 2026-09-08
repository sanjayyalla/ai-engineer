import requests
import json


res = requests.get("https://jsonplaceholder.typicode.com/todos/1")


print(res.text)
print(type(res.text))
print(res.json())
print(type(res.json()))

print("---------------------------------------------")
# Post request

post_dict = {"title": "foo","body": "bar","userId": 1}

res = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_dict)

print(res.status_code)
print(res.json())