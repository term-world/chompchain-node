const fs = require('fs-extra');
const http = require('http');
const express = require('express');
const env = require('dotenv').config(); // ({ path: '/opt/server/.env' });
const { createHash } = require('crypto');

let server = express();
server.use(express.json());

const app = http.createServer(server);
app.listen(5000);

const generateNumber = (min, max) => {
    return Math.floor(
        Math.random() * (max - min + 1) + min
    );
}

const assign = async () => {
    const max = 1000;
    const min = 10000;
    const files = await fs.readdir(
        process.env.MEMPOOL
    );
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
    delete txn.hash;
    delete txn.timestamp;
    // Make the hash from remainder
    let hashable = JSON.stringify(txn);
    let checksum = createHash('sha256').update(hashable).digest('hex');
    return checksum == txHash;
}

server.post("/transact", async (req, res) => {
    let record = req.body.txn;
    let filename = `${await assign()}.json`;
    if(await verified(req.body.txn)){
        fs.writeFile(`${process.env.MEMPOOL}/{filename}`, JSON.stringify(req.body.txn), (err) => {
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
});
