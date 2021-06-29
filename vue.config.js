const webpack = require('webpack')
module.exports = {
  configureWebpack: {
    plugins: [
      new webpack.optimize.LimitChunkCountPlugin({
        maxChunks: 1
      })
    ],
    devServer: {
      headers: { "Access-Control-Allow-Origin": "*" }
    }
  },
  filenameHashing: false,
  productionSourceMap: false,
  chainWebpack:
    config => {
      config.optimization.delete('splitChunks')
    }
}