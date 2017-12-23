import pandas as pd

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

def csvtojson(file_name):
    df = pd.read_csv(file_name)
    print df
    nodelist = []
    jsondata = {}
    jsondata["nodes"] = []
    jsondata["links"] = []
    for i in range(0,2):
        print df["destination"][i]
        if df["source"][i] not in nodelist:
            nodelist.append(df["source"][i])
        if df["destination"][i] not in nodelist:
            nodelist.append(df["destination"][i])
    for i in range(len(nodelist)):
        jsondata["nodes"].append({"name":nodelist[i]})

    for i in range(len(df["destination"])):
        jsondata["links"].append({
        "source": df["source"][i],
        "destination": df["destination"][i],
        "colour": df["colour"][i],
        "size": 5,
        "value": 5
        })
    return jsondata

def genforced_layout(width, height, file_name, stroke_width):
    temp = ""
    temp += '<script src="d3.v4.min.js"></script>\n'
    temp += '<style>\n'
    temp += '\n'
    temp += '.link {\n'
    temp += ' stroke: #777;\n'
    temp += ' stroke-opacity: 0.3;\n'
    temp += ' stroke-width: '+str(stroke_width)+'px;\n'
    temp += '}\n'

    temp += '.node circle {\n'
    temp += ' fill: #ccc;\n'
    temp += ' stroke: #000;\n'
    temp += ' stroke-width: 1.5px;\n'
    temp += '}\n'

    temp += '.node text {\n'
    temp += ' display: none;\n'
    temp += ' font: 10px sans-serif;\n'
    temp += '}\n'

    temp += '.node:hover circle {\n'
    temp += ' fill: #000;\n'
    temp += '}\n'

    temp += '.node:hover text {\n'
    temp += ' display: inline;\n'
    temp += '}\n'

    temp += '.cell {\n'
    temp += ' fill: none;\n'
    temp += ' pointer-events: all;\n'
    temp += '}\n'

    temp += ' </style>\n'
    temp += ' <body>\n'

    temp += ' <script>\n'
    temp += ' var width = '+str(width)+',\n'
    temp += '       height = '+str(height)+',\n'
    temp += '       color = d3.scale.category20c();\n'

    temp += 'var svg = d3.select("body").append("svg")\n'
    temp += '   .attr("width", width)\n'
    temp += '   .attr("height", height);\n'

    temp += 'var force = d3.layout.force()\n'
    temp += '   .gravity(0.1)\n'
    temp += '   .charge(-120)\n'
    temp += '   .linkDistance(30)\n'
    temp += '   .size([width, height]);\n'

    temp += 'var voronoi = d3.geom.voronoi()\n'
    temp += '   .x(function(d) { return d.x; })\n'
    temp += '   .y(function(d) { return d.y; })\n'
    temp += '   .clipExtent([[0, 0], [width, height]]);\n'

    temp += 'd3.json("graph.json", function(error, json) {\n'
    temp += ' if (error) throw error;\n'
    temp += ' console.log(json.nodes);\n'
    temp += ' console.log(json.links);\n'
    temp += ' force\n'
    temp += '     .nodes(json.nodes)\n'
    temp += '     .links(json.links)\n'
    temp += '     .start();\n'

    temp += ' var link = svg.selectAll(".link")\n'
    temp += '     .data(json.links)\n'
    temp += '     .enter().append("line")\n'
    temp += '     .attr("class", "link")\n'
    temp += '     .style("stroke", function(d) { return d.color; });//new\n'

    temp += ' var node = svg.selectAll(".node")\n'
    temp += '     .data(json.nodes)\n'
    temp += '     .enter().append("g")\n'
    temp += '     .attr("class", "node")\n'
    temp += '     .call(force.drag);\n'

    temp += ' var circle = node.append("circle")\n'
    temp += '     .attr("r", function(d) { return d.size; })\n'
    temp += '     .style("fill", function(d) { return d.color; }); //new\n'

    temp += ' var label = node.append("text")\n'
    temp += '     .attr("dy", ".35em")\n'
    temp += '     .text(function(d) { return d.name; });\n'

    temp += ' var cell = node.append("path")\n'
    temp += '     .attr("class", "cell");\n'
    temp += ' force.on("tick", function() {\n'
    temp += '   cell\n'
    temp += '       .data(voronoi(json.nodes))\n'
    temp += '       .attr("d", function(d) { return d.length ? "M" + d.join("L") : null; });\n'

    temp += '   link\n'
    temp += '       .attr("x1", function(d) { return d.source.x; })\n'
    temp += '       .attr("y1", function(d) { return d.source.y; })\n'
    temp += '       .attr("x2", function(d) { return d.target.x; })\n'
    temp += '       .attr("y2", function(d) { return d.target.y; });\n'

    temp += '   circle\n'
    temp += '       .attr("cx", function(d) { return d.x; })\n'
    temp += '       .attr("cy", function(d) { return d.y; });\n'

    temp += '   label\n'
    temp += '       .attr("x", function(d) { return d.x + 8; })\n'
    temp += '       .attr("y", function(d) { return d.y; });\n'
    temp += ' });\n'
    temp += ' }\n'
    return temp
