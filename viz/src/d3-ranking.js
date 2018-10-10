import * as d3_array from 'd3-array';
import * as d3_selection from 'd3-selection';
import * as d3_scale from 'd3-scale';

/**
 *
 * @param {string}    element
 *
 * @param {Object}    options
 * @param {number}    options.width
 * @param {number}    options.height
 * @param {number[]}  options.data
 * 
 * @param {Object}    options.pagination
 * @param {number}    options.pagination.size
 * @param {number}    options.pagination.limit
 */
export function ranking(element, options) {

  if (!options.pagination) options.pagination = {};
  if (!options.pagination.size) options.pagination.size = 20;
  if (!options.pagination.limit) options.pagination.limit = 10;

  /************************\
    Data -> Visualization  |
  \************************/
  
  const marks = options.data.map((datum, index) => ({
    datum: datum,
    index: index,
  }));
  const rails = options.data.map((datum, index) => ({
    datum: datum,
    index: index,
  }));
  const pages = marks.reduce((pages, mark) => (
    pages[pages.length - 1].length < options.pagination.size
      ? (pages[pages.length - 1].push(mark), pages)
      : (pages.push([mark]), pages)
  ), [[]]);

  console.log(marks);
  console.log(rails);
  console.log(pages);

  const visualization = {
    marks,
    rails,
    pages,
  };

  /*****************************\
  |  Visualization -> Graphics  |
  \*****************************/

  const svg = d3_selection
    .select(element)
    .append('svg')
    .attr('width', options.width)
    .attr('height', options.height)
    ;

    draw(svg, visualization);
}

/**
 *
 * @typedef visualization
 * @property {Object[]} marks
 * @property {Object[]} rails
 * @property {Object[]} pages
 * 
 *
 * @param {d3_selection.Selection} svg
 */
function draw(svg, /** @type {visualization} */ {
  marks,
  pages,
}) {
  const width = svg.attr('width');
  const height = svg.attr('height');

  const FIGURE_TOP_MARGIN = 30;
  const FIGURE_BOT_MARGIN = 30;
  const FIGURE_LEFT_MARGIN = 30;
  const FIGURE_RIGHT_MARGIN = 30;

  const MARKER_MIN_RADIUS = 10;
  const MARKER_MAX_RADIUS = 15;


  // row to vertical axis conversion scale
  const row2vax = d3_scale
    .scaleLinear()
    .domain([0, pages[0].length - 1])
    .range([0 + FIGURE_TOP_MARGIN, height - FIGURE_BOT_MARGIN])
    ;
  // column to horizontal axis conversion scale
  const col2hax = d3_scale
    .scaleLinear()
    .domain([0, pages.length - 1])
    .range([0 + FIGURE_LEFT_MARGIN, width - FIGURE_RIGHT_MARGIN])
    ;
  // radius based on data values
  const r = d3_scale
    .scaleLinear()
    .domain(d3_array.extent(marks.map(mark => mark.datum)))
    .range([MARKER_MIN_RADIUS, MARKER_MAX_RADIUS])
    ;
  // color based on data values
  const c = d3_scale
    .scaleSequential()
    .domain(d3_array.extent(marks.map(mark => mark.datum)))
    .interpolator(d3_scale.interpolateViridis)
    ;


  const page = svg
    .selectAll('g')
      .data(pages)
      .enter().append('g')
        .attr('transform', (page, index) => `translate(${col2hax(index)}, 0)`)
    ;

  const mark = page
    .selectAll('circle')
      .data(d => d)
      .enter().append('circle')
        .attr('id', mark => mark.index)
        .attr('cx', 0)
        .attr('cy', (mark, pindex) => row2vax(pindex))
        .attr('r', mark => r(mark.datum))
        .attr('fill', mark => c(mark.datum))
    ;

}
