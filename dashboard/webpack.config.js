var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

var appStyles = new ExtractTextPlugin('styles.css');
var vendorStyles = new ExtractTextPlugin('vendor.css');

module.exports = {
  devtool: 'cheap-module-eval-source-map',
  context: path.join(__dirname, './src'),
  entry: {
    jsx: './index.js',
    vendor: [
      'react',
      'react-dom',
      'alt',
      'classnames',
      'react-router',
      'redbox-react'
    ]
  },
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'bundle.js',
    publicPath: '/dist/'
  },
  plugins: [
    vendorStyles,
    appStyles,
    new webpack.NoErrorsPlugin(),
    new webpack.optimize.CommonsChunkPlugin('vendor', 'vendor.bundle.js'),
    new webpack.DefinePlugin({
      'process.env': { NODE_ENV: JSON.stringify(process.env.NODE_ENV || 'development') }
    })
  ],
  module: {
    loaders: [
      {
        test: /\.js$/,
        loaders: ['babel'],
        include: [path.join(__dirname, 'src'), path.join(__dirname, 'node_modules', 'jsonpicklejs')]
      },
      {
        test: /\.(less|css)$/,
        loader: appStyles.extract('style', 'css?sourceMap!autoprefixer?browsers=last 2 version!less?&sourceMap'),
        exclude: [/font_awesome/, /theme/, /vendor/]
      },
      {
        test: /\.(less|css)$/,
        loader: vendorStyles.extract('style', 'css?sourceMap!autoprefixer?browsers=last 2 version!less?&sourceMap'),
        include: [/font_awesome/, /theme/, /vendor/]
      },
      {
        test: /\.(jpe?g|png|gif|svg|woff2?|eot|ttf)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'file?name=[sha512:hash:base64:7].[ext]'
      },
      {
        test: /\.json$/,
        loader: 'json'
      }
    ]
  },
  devServer: {
    contentBase: './src',
    hot: true
  }
};