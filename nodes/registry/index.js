const fs = require('fs-extra');
const http = require('http');
const express = require('express');
const env = require('dotenv').config({ path: '/opt/server/.env' });

let server = express();
server.use(express.json());

const app = http.createServer(server);
app.listen(5001);

const nodes = [];

server.post("/register", async (req, res) => {
    // How do we know that this is a genuine request?
    // TODO: Implment some test; in future, spend some
    // amount of coin (stake) to guarantee?

    // But, if we're thinking about 100% consensus, and
    // we have one node that we run in good faith, do we
    // care about bad actors?

    let identity = {
        host: req.headers["x-real-ip"],
        port: req.body.port
    }

    nodes.push(identity);
    // Write to file?
    res.status(200);
    return;
});

server.get("/directory", (req, res) => {
    res.status(200).send(JSON.stringify(nodes));
});
