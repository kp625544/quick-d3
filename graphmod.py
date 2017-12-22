

def genhead(title):
    return '<!DOCTYPE html>\n<meta charset="utf-8">\n<head>\n<title>'+title+'</title></head>\n'

def genbar(width, height, file_name):
    temp = ""
    temp += '<style> /* set the CSS */\n'

    temp +='.bar { fill: steelblue; }\n'
    temp +='</style>\n'
    temp +='<body>'
    temp +='<script src="d3.v4.min.js"></script>\n'
    temp +='<script>'
    temp += '// set the dimensions and margins of the graph\n'
    temp += 'var margin = {top: 20, right: 20, bottom: 30, left: 40},\n'
    temp += 'width = '+str(width)+' - margin.left - margin.right,\n'
    temp += 'height = '+str(height)+' - margin.top - margin.bottom;\n'
    temp += '    // set the ranges\n'
    temp += 'var x = d3.scaleBand()\n'
    temp += '          .range([0, width])\n'
    temp += '          .padding(0.1);\n'
    temp += 'var y = d3.scaleLinear()\n'
    temp += '          .range([height, 0]);\n'
    temp += ''
    temp += '// append the svg object to the body of the page\n'
    temp += '// append a group element to svg\n'
    temp += '// moves the group element to the top left margin\n'
    temp += 'var svg = d3.select("body").append("svg")\n'
    temp += '    .attr("width", width + margin.left + margin.right)\n'
    temp += '    .attr("height", height + margin.top + margin.bottom)\n'
    temp += '  .append("g")\n'
    temp += '    .attr("transform", \n'
    temp += '          "translate(" + margin.left + "," + margin.top + ")");\n'

    temp += '// get the data\n'
    temp += 'd3.csv("'+file_name+'", function(error, data) {\n'
    temp += '  if (error) throw error;\n'

    temp += '  // format the data\n'
    temp += '  data.forEach(function(d) {\n'
    temp += '    d.sales = +d.sales;\n'
    temp += '  });\n'

    temp += '  // Scale the range of the data in the domains\n'
    temp += '  x.domain(data.map(function(d) { return d.salesperson; }));\n'
    temp += '  y.domain([0, d3.max(data, function(d) { return d.sales; })]);\n'

    temp += '  // append the rectangles for the bar chart\n'
    temp += '  svg.selectAll(".bar")\n'
    temp += '      .data(data)\n'
    temp += '    .enter().append("rect")\n'
    temp += '      .attr("class", "bar")\n'
    temp += '      .attr("x", function(d) { return x(d.salesperson); })\n'
    temp += '      .attr("width", x.bandwidth())\n'
    temp += '      .attr("y", function(d) { return y(d.sales); })\n'
    temp += '      .attr("height", function(d) { return height - y(d.sales); });\n'

    temp += '  // add the x Axis\n'
    temp += '  svg.append("g")\n'
    temp += '      .attr("transform", "translate(0," + height + ")")\n'
    temp += '      .call(d3.axisBottom(x));\n'

    temp += '  // add the y Axis\n'
    temp += '  svg.append("g")\n'
    temp += '      .call(d3.axisLeft(y));\n'

    temp += '});\n'

    temp += '</script>\n'
    temp += '</body>\n'
    return temp
