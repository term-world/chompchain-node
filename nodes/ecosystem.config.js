module.exports = {
  apps : [
    {
        name   : "validator",
        script : "/opt/server/chompchain-node/nodes/validator/main.py",
        exec_mode: "fork",
        interpreter: "python"
    },
    {
        name   : "registry",
        script : "/opt/server/chompchain-node/nodes/registry/index.js",
        exec_mode: "fork",
    }
  ]
}
