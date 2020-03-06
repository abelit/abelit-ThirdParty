process.env.VUE_APP_VERSION = require("./package.json").version;

module.exports = {
  // config
  assetsDir: "static", // For simple configuration of static files in Flask (the "static_folder='client/dist/static'" part in app.py)
  devServer: {
    proxy: 'http://10.46.100.220:5000/',// So that the client dev server can access your Flask routes

    // host: 'localhost',
    // port: 8080,

    // auto open browser
    open: true
  }
};
