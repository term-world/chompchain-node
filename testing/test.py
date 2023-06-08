import requests
import json

data = {"msg": "hi", "name": "Professor"}

response = requests.post(
    # URL -> "endpoint"
    "http://localhost:8080/transactions/new",
    data = json.dumps(data)
)

print(response.status_code)