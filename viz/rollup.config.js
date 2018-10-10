import npm from 'rollup-plugin-node-resolve';
import commonjs from 'rollup-plugin-commonjs';

export default {
  input: 'index.js',
  plugins: [npm({jsnext: true}), commonjs({})],
  output: {
    name: 'd3',
    file: 'build/d3-ranking.js',
    format: 'umd',
  }
};