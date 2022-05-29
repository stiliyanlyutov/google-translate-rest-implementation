import requests
import json

response = requests.request("GET", "http://127.0.0.1:5000/translate?text=hello&dest=bg&src=en",)
print(response.text)