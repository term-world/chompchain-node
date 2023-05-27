const fs = require('fs-extra');
const http = require('http');
const express = require('express');
const env = require('dotenv').config();

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

const verified = async () => {
    return true;
}

server.post("/transact", async (req, res) => {
    let record = req.body.txn;
    let filename = `${await assign()}.json`;
    if(await verified(req.body.txn)){
        fs.writeFile(`${process.env.MEMPOOL}{filename}`, JSON.stringify(req.body.txn), (err) => {
            console.log(err);
        });
    }
    // TODO: Send a 200 where successful
});

server.post("/validate", async (req, res) => {
});
