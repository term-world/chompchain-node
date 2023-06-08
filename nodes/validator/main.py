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

async def transaction_new(request):
    try:
        request_body = await request.json()
        if not "name" in request_body:
            return web.Response(status = 418)
        return web.Response(status = 200)
    except:
        return web.Response(status = 500)

# async def assign():
#     files = await asyncio.to_thread(fs.readdir, process.env.MEMPOOL)
#     min_value = 1000
#     max_value = 10000
#     random_number = random.randint(min_value, max_value)

#     while f"{random_number}.json" in files:
#         random_number = random.randint(min_value, max_value)

#     return str(random_number)
    



# async def verified(txn):
#     tx_hash = txn['hash']
#     hashables = {k: v for k, v in txn.items() if k not in ['hash', 'signature']}
#     hashable = json.dumps(hashables, sort_keys=True).encode('utf-8')
#     checksum = hashlib.sha256(hashable).hexdigest()
#     return checksum == tx_hash

# aiohttp application setup
app = web.Application()

# Routes are endpoints (i.e. URIs in this case)
app.add_routes(
    [web.post("/transactions/new", transaction_new)]
)
web.run_app(app)

