const http = require('http');
const fs = require('fs-extra');
const express = require('express');
// TODO: Replace references to dotenv; we can't
// distribute .env files
const env = require('dotenv').config({
    path: '../.env'
});

let server = express();
server.use(express.json());

const app = http.createServer(server);
app.listen(5001);

const nodes = [];

server.post("/register", async (req, res) => {
    console.log(req);
    let identity = {
        host: req.headers["x-real-ip"] || req.headers["x-forwarded-for"],
        port: req.body.port
    }
    nodes.push(identity);
    res.sendStatus(200);
    return;
});

server.post("/propagate", async (req, res) => {
    
});

server.get("/directory", (req, res) => {
    res.status(200).send(JSON.stringify(nodes));
});
