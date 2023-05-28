module.exports = {
  apps : [
    {
        name   : "validator",
        script : "/opt/server/chompchain-node/nodes/validator/index.js",
        exec_mode: "fork",
    },
    {
        name   : "registry",
        script : "/opt/server/chompchain-node/nodes/registry/index.js",
        exec_mode: "fork",
    }
  ]
}
