import json
import hashlib
import aiohttp
import asyncio
from aiohttp import web
import os 
import random

async def transaction_new(request):
    try:
        txn = await request.json()
        if await is_valid(txn):
            pass
        return web.Response(status = 200)
    except:
        return web.Response(status = 500)


async def is_valid(txn: dict = {}) -> bool:
    hash = txn['hash']
    # Create a new dictionary without 'hash' and 'signature' keys
    hashables = {}
    for key, val in txn.items():
        if not key in ["hash", "timestamp", "signature"]:
            hashables[key] = val
    # Dump string minified (i.e. no spaces around separators)
    hashable_str = json.dumps(
        hashables,
        separators = (",",":")
    )
    # Encode string as bytestring
    hashable_bytes = hashable_str.encode('utf-8')
    # Calculate the SHA256 hash of the bytes
    sha256_hash = hashlib.sha256()
    sha256_hash.update(hashable_bytes)
    checksum = sha256_hash.hexdigest()
    # Return result of hex string comparison
    return checksum == hash


async def transact_handler(request):
    try:
        data = await request.json()
        key = data.get('key')
        txn = data.get('txn')
        sig = data.get('txn', {}).get('signature')

        filename = await assign()

        if await is_valid(txn) and await signed(sig, key):
            file_path = f"{os.environ['MEMPOOL']}/{filename}.json"
            with open(file_path, 'w') as file:
                json.dump(txn, file)
            return web.Response(status=200)
        
        return web.Response(status=418)  # I'M A TEAPOT
    except:
        return web.Response(status=500)

async def assign():
    max_value = 10000
    min_value = 1000
    files = os.listdir(os.environ['MEMPOOL'])
    random_number = random.randint(min_value, max_value)
    
    while f"{random_number}.json" in files:
        random_number = random.randint(min_value, max_value)
    
    return random_number

async def signed(sig, key):
    # Implementation for signature verification goes here
    pass


# aiohttp application setup
app = web.Application()

# Routes are endpoints (i.e. URIs in this case)
app.add_routes(
    [web.post("/transactions/new", transaction_new)]
)
web.run_app(app, port = 7500)
