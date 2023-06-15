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
        else:
            return web.Response(status = 500)
    # If we reach this point, the request is
    # at fault.
    except:    
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

async def assign_filename():
    files = os.listdir(os.environ['MEMPOOL'])
    filename = secrets.token_hex(3)
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
