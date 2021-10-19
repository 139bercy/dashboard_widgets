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
  pages: {
     index: {
         entry: 'src/main.js',
         template: 'public/index.html',
         filename: 'index.html',
     },
 },
  filenameHashing: false,
  productionSourceMap: false,
  chainWebpack:
    config => {
      config.optimization.delete('splitChunks')
    }
}
