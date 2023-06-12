import requests
import json
# from chompchainwallet.interface import Transaction
# transaction = Transaction(
#     wallet=Wallet(),
#     to_addr="...",
#     data={...},
#     from_addr="..."
# )
# transaction_data = {
#     'data': transaction.data,
#     'to_addr': transaction.to_addr,
#     'from_addr': transaction.from_addr,
#     'hash': transaction.hash,
#     'timestamp': transaction.timestamp,
#     'signature': transaction.signature
# }

data = {'msg': 'hi', 'name': 'Professor'}

response = requests.post(
    # URL -> "endpoint"
    "http://localhost:8080/transactions/new",
    data = json.dumps(data)
)

print(response.status_code)