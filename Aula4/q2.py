import requests
import json

url = "https://api.github.com/"

request = requests.get(url)



print(json.dumps(request.json(), indent=4))