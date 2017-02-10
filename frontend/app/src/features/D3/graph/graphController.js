(function () {
      'use strict';

      angular.module('sentimentAnalysis.feature')
            .controller('graphController', graphController);

      graphController.$inject = ['$scope', 'd3'];
      function graphController($scope, d3) {
            var vm = $scope,
                  height = vm.height | 250,
                  width = vm.width | 500,
                  margin = {
                        top: 20,
                        right: 100,
                        bottom: 40,
                        left: 25
                  };
            function calculateRange(axis) {
                  return d3.max(vm.data, function(d){ return axis == 'x' ? d.x : d.y });
            }
            function configureAxisScale(range, axis) {
                  return d3.scale.linear()
                        .domain([0, calculateRange(axis)])
                        .range(range);
            }
            function drawAxis() {
                  vm.element.selectAll('g').remove()
                  var xAxis = d3.svg.axis()
                        .scale(configureAxisScale([0, width], 'x'))
                        .orient("bottom")
                        .innerTickSize(-height)
                        .outerTickSize(0)
                        .tickPadding(10);

                  var yAxis = d3.svg.axis()
                        .scale(configureAxisScale([height, 0], 'y'))
                        .orient("left")
                        .innerTickSize(-width)
                        .outerTickSize(0)
                        .tickPadding(10);

                  vm.element.append("g")
                        .attr("class", "x axis")
                        .attr("transform", "translate(0," + height + ")")
                        .call(xAxis)

                  vm.element.append("g")
                        .attr("class", "y axis")
                        .call(yAxis)
            };

            vm.drawGraph = function() {
                  vm.element = vm.container.append('svg')
                        .attr('width', width)
                        .attr('height', calculateHeight())
                        .style('padding-left', margin.left)
                        .style('padding-top', margin.top)
                  drawAxis()
            };
            vm.controller = function() {
                  vm.container = d3.select('graph');
                  vm.drawGraph();
                  draw()
            };


            function calculateHeight() {
                  return height + margin.bottom;
            };

            // function calculateNewValue() {
            //       return {
            //             'x': 20,
            //             'y':Math.random() * 100
            //       };
            // }

            function draw(){

                  var line = d3.svg.line()
                        .x(function(d) { return configureAxisScale([0, width], 'x')(d.x); })
                        .y(function(d) { return configureAxisScale([height, 0], 'y')(d.y); });

                  vm.path = vm.element.append("path")
                        .data([vm.data])
                        .attr("class", "line")
                        .attr("d", line);

                  // setInterval(function(){
                  //       _.forEach(vm.data, function(data) {
                  //             if (data != _.head(_.head(vm.data))){
                  //                   data.x -= 1;
                  //             }
                  //       });
                  //       vm.data.push(calculateNewValue());
                  //       vm.data.shift();
                        drawAxis();
                        // vm.path.transition()
                        //       .attr("d", line);
                  // }, 2000);
            }
      }
})();
