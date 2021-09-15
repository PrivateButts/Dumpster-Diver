const path = require('path');

module.exports = {
    entry: {
        index: './frontend/index.js',
        snippet: './frontend/snippet-viewer.js',
    },
    output: {
        filename: '[name]-bundle.js', // output bundle file name
        path: path.resolve(__dirname, './static/webpack/'), // path to our Django static directory
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: { presets: ["@babel/preset-env"] }
            },
            {
                test: /.css$/,
                use: [
                    'style-loader',
                    'css-loader',
                ]
            }
        ]
    }
};