import requests
import json

with open("data.json", "r") as fh:
    data = json.load(fh)

response = requests.post(
    # URL -> "endpoint"
    "http://localhost:7500/transactions/new",
    data = json.dumps(data)
)

print(response.status_code)
