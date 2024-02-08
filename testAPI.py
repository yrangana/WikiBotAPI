#test hosted API in amazon app runner
import requests
import json

url = "http://0.0.0.0:8081/wikipedia_summary"

data = {
    "title": "Microsoft",
    "sentences": 2
}

response = requests.post(url, json=data,timeout=20)

print(json.dumps(response.json(), indent=2))