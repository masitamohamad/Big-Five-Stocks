var margin = {top: 10, right: 10, bottom: 10, left: 100},
    width = 550 - margin.left - margin.right,
    height = 350 - margin.top - margin.bottom;
var format = d3.format("g");
var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);
var y = d3.scale.linear()
    .range([height, 0]);
var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");
var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(format);
var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong>Volume:</strong> <span style='color:white'>" + d.volume + "</span>";
  })
var svg = d3.select("#stockVolume").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
svg.call(tip);
d3.tsv("data.tsv", type, function(error, data) {
  x.domain(data.map(function(d) { return d.date; }));
  y.domain([0, d3.max(data, function(d) { return d.volume; })]);
  svg.append("g")
      .attr("card-body", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);
  svg.append("g")
      .attr("card-body", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Stock Volume");
  svg.selectAll("card-body.bar")
      .data(data)
    .enter().append("rect")
      .attr("card-body", "card-body.bar")
      .attr("x", function(d) { return x(d.date); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.volume); })
      .attr("height", function(d) { return height - y(d.volume); })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide)
});
function type(d) {
  d.volume = +d.volume;
  return d;
}
