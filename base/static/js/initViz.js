 var circleRadii = [40, 20, 10]






 var barContainer = d3.select("#content").append("svg")
                                     .attr("width", 600)
                                    .attr("height", 600)
                                    .style("border", "1px solid black");

 
 var svgContainer = d3.select("#mainviz").append("svg")
                                     .attr("width", 600)
                                    .attr("height", 600)
				    .style("border", "1px solid black");

var circles = svgContainer.selectAll("circle")
                          .data(jsonCircles)
                          .enter()
                          .append("circle")

var circleAttributes = circles
                       .attr("cx", function (d) { return d.x_axis; })
                       .attr("cy", function (d) { return d.y_axis; })
                       .attr("r", function (d) { return d.radius; })
                       .style("fill", function(d) {
                         var returnColor;
                         if (d === 40) { returnColor = "green";
                         } else if (d === 20) { returnColor = "purple";
                         } else if (d === 10) { returnColor = "red"; }
                         return d.color;
                       });


var dataArray = [40]
var bars = barContainer.selectAll("div")
			.data(dataArray)
			.enter()
			.append("div")
			.attr("class", "bar")
			.style("background-color", "red")
			.style("width", "50px")
