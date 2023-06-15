import os
import json
import random
import secrets
import hashlib
import aiohttp
import asyncio

from aiohttp import web

async def transaction_new(request):
    try:
        txn = await request.json()
        if await is_valid_hash(txn) and await is_valid_txn(txn):
            filename = await assign_filename()
            file_path = f"{os.environ['MEMPOOL']}/{filename}.json"
            with open(file_path, 'w') as file:
                json.dump(txn, file)
        return web.Response(status = 200)
    except:
        return web.Response(status = 500)
    # If we reach this point, the request is
    # at fault.
    return web.Response(status = 418)

async def is_valid_txn(txn: dict = {}) -> bool:
    keys = ["data", "to_addr", "from_addr",
            "hash", "timestamp", "signature"]
    for key in keys:
        if key not in txn:
            return False
        if not keys[key]:
            return False
    return True

async def is_valid_hash(txn: dict = {}) -> bool:
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

<<<<<<< HEAD

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
    # Set the range of random numbers
    max_value = 10000
    min_value = 1000
    
    # Get the list of files in the MEMPOOL directory
    files = os.listdir(os.environ['MEMPOOL'])
    
    # Generate a random number within the specified range
    random_number = random.randint(min_value, max_value)
    
    # Check if the generated filename already exists in the list of files
    while f"{random_number}.json" in files:
        # If the filename exists, generate a new random number
        random_number = random.randint(min_value, max_value)
    
    # Return the unique random number as the assigned filename
    return random_number
=======
async def assign_filename():
    files = os.listdir(os.environ['MEMPOOL'])
    filename = secrets.token_hex(3)
>>>>>>> b14fac74f62bf34c5be54987bd0f14eae5a3f001

    while f"{filename}.json" in files:
        filename = secrets.token_hex(3)

    return filename

# aiohttp application setup
app = web.Application()

# Routes are endpoints (i.e. URIs in this case)
app.add_routes(
    [web.post("/transactions/new", transaction_new)]
)
web.run_app(app, port = 7500)
