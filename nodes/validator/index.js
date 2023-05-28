const fs = require('fs-extra');
const http = require('http');
const key = require('node-rsa');
const express = require('express');
const { createHash } = require('crypto');
const env = require('dotenv').config({
    path: '/opt/server/.env'
});

let server = express();
server.use(express.json());

const app = http.createServer(server);
app.listen(5000);

// TODO: Register as a node on the network
let registered = false;

do {
    http.get('http://dir.chain.chompe.rs', (response) => {
        response.on('data', (dir) = > {
            registered = true;
        });
    }
} (while !registered);

const generateNumber = (min, max) => {
    return Math.floor(
        Math.random() * (max - min + 1) + min
    );
}

const assign = async () => {
    const max = 1000;
    const min = 10000;
    // Read current filenames in MEMPOOL
    const files = await fs.readdir(
        process.env.MEMPOOL
    );
    // Assign new filename until unique
    let random = generateNumber(1000, 10000);
    do {
        random = generateNumber(1000, 10000);
    } while (files.includes(random));
    return random;
}

const verified = async (txn) => {
    // Save hash for comparison
    let txHash = txn.hash;
    // Remove extraneous unhashed fields
    let hashables = Object.fromEntries(
        Object.entries(txn).filter(
            ([k,v]) => {
                return !["hash","timestamp","signature"].includes(k)
            }
        )
    );
    // Make the hash from remainder
    let hashable = JSON.stringify(hashables);
    let checksum = createHash('sha256').update(hashable).digest('hex');
    // Compare truthiness
    return checksum == txHash;
}

const signed = async (signature, key) => {
    // TODO: Roll out when wallet signatures are standardized
    // key.importKey(key, 'pkcs8');
    // return key.verify(signature, key);
    return true;
}

server.post("/transact", async (req, res) => {
    let key = req.body.key;
    let sig = req.body.txn.signature;
    let txn = req.body.txn;
    let filename = `${await assign()}.json`;
    if(await verified(txn) && await signed(sig, key)){
        fs.writeFile(`${process.env.MEMPOOL}/${filename}`, JSON.stringify(txn), (err) => {
            if(err) {
                console.log(`500: ${err}`);
                res.sendStatus(500);
                return;
            }
        });
        res.sendStatus(200);
        return;
    }
    // I'M A TEAPOT
    res.sendStatus(418);
    return;
});

server.post("/validate", async (req, res) => {
    let block = req.body.block;
    let pubKey = req.body.key;
});
