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
     'index-afa': {
         entry: 'src/main.js',
         template: 'public/index-afa.html',
         filename: 'index-afa.html',
     },
     'index-afa-2021': {
        entry: 'src/main.js',
        template: 'public/index-afa-2021.html',
        filename: 'index-afa-2021.html',
     },
     'index-ca-afa-2021': {
      entry: 'src/main.js',
      template: 'public/index-ca-afa-2021.html',
      filename: 'index-ca-afa-2021.html',
     },
     'index-impact': {
         entry: 'src/main.js',
         template: 'public/index-impact.html',
         filename: 'index-impact.html',
     },
 },
  filenameHashing: false,
  productionSourceMap: false,
  chainWebpack:
    config => {
      config.optimization.delete('splitChunks')
    }
}
