import json
import hashlib
import aiohttp
import asyncio
from aiohttp import web

async def register_node():
    url = "https://dir.chain.chompe.rs/register"
    data = {"port": 5000}

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.post(url, json=data) as response:
                    if response.status == 200:
                        print("Registered...")
                        break
            except aiohttp.ClientError:
                print("Unable to register node...")
                return

            await asyncio.sleep(5)


# async def transaction_new(request):
#     try:
#         request_body = await request.json()
#         print(request_body)
#         if not "name" in request_body:
#             return web.Response(status = 418)
#         return web.Response(status = 200)
#     except:
#         return web.Response(status = 500)
    
# async def mempool(request):
#     mempool_dir = os.environ.get('MEMPOOL')
#     files = await asyncio.get_event_loop().run_in_executor(None, os.listdir, mempool_dir)
#     return web.json_response(files)    
    

# async def assign():
#     files = await asyncio.to_thread(fs.readdir, process.env.MEMPOOL)
#     min_value = 1000
#     max_value = 10000
#     random_number = random.randint(min_value, max_value)

#     while f"{random_number}.json" in files:
#         random_number = random.randint(min_value, max_value)

#     return str(random_number)
    



# async def verify(txn):
#     tx_hash = txn['hash']
#     # Create a new dictionary without 'hash' and 'signature' keys
#     hashables = {}
#     for k, v in txn.items():
#         if k != 'hash' and k != 'signature':
#             hashables[k] = v
#     # Sort the keys in alphabetical order
#     sorted_keys = sorted(hashables.keys())
#     # Convert the sorted keys and corresponding values to a string
#     hashable_str = "{"
#     for key in sorted_keys:
#         value = hashables[key]
#         hashable_str += f"'{key}': {json.dumps(value)}, "
#     hashable_str = hashable_str.rstrip(', ') + "}"
#     # Convert the string to bytes using UTF-8 encoding
#     hashable_bytes = hashable_str.encode('utf-8')
#     # Calculate the SHA256 hash of the bytes
#     sha256_hash = hashlib.sha256()
#     sha256_hash.update(hashable_bytes)
#     checksum = sha256_hash.hexdigest()
#     # Check if the calculated checksum matches the original tx_hash
#     return checksum == tx_hash


# aiohttp application setup
app = web.Application()

# Routes are endpoints (i.e. URIs in this case)
app.add_routes(
    [web.post("/transactions/new", transaction_new)]
)
app.add_routes(web.get('/', handle)),
web.run_app(app)

