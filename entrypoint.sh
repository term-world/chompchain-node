#!/bin/sh

# CouchDB setup

COUCHDB_PASSWORD=$(echo -n $RANDOM | sha256sum)

# pm2 task
pm2-runtime /opt/server/ecosystem.config.js