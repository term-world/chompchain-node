module.exports = {
  apps : [
    {
        name   : "validator",
        script : "/opt/server/validator/index.js",
        exec_mode: "fork",
    },
    {
        name   : "registry",
        script : "/opt/server/registry/index.js",
        exec_mode: "fork",
    }
  ]
}
