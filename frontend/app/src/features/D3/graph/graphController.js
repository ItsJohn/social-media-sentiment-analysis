(function () {
      'use strict';

      angular.module('sentimentAnalysis.feature')
            .controller('graphController', graphController);

      graphController.$inject = ['$scope', 'd3'];
      function graphController($scope, d3) {
            var vm = $scope,
                  height = vm.height | 250,
                  width = vm.width | 500,
                  date,
                  padding = {
                        left: 5
                  },
                  margin = {
                        top: 20,
                        right: 100,
                        bottom: 40,
                        left: 30
                  };

            function calculateRange() {
                  return d3.max(vm.data, function(d){ return d.y; });
            }

            function configureAxisScale(range) {
                  return d3.scale.linear()
                        .domain([0, calculateRange()])
                        .range(range);
            }

            function configureDateRange() {
                  var date = [];
                  _.forEach(vm.data, function(data) {
                        date.push(data['x']);
                  });
                  return [_.min(date), _.max(date)];
            }

            function configureDateAxisScale(range) {

                  return d3.time.scale()
                        .domain(configureDateRange())
                        .range(range);
            }

            function drawAxis() {
                  vm.element.selectAll('g').remove();
                  var xAxis = d3.svg.axis()
                        .scale(configureDateAxisScale([0, width]))
                        .orient('bottom')
                        .innerTickSize(-height)
                        .outerTickSize(0)
                        .tickPadding(10);

                  var yAxis = d3.svg.axis()
                        .scale(configureAxisScale([height, 0]))
                        .orient('left')
                        .innerTickSize(-width)
                        .outerTickSize(0)
                        .tickPadding(10);

                  vm.element.append('g')
                        .attr('class', 'xaxis')
                        .attr('transform', 'translate(0,' + height + ')')
                        .call(xAxis);

                  vm.element.append('g')
                        .attr('class', 'y axis')
                        .attr('transform', 'translate(' + padding.left + ',0)')
                        .call(yAxis);
            }

            vm.drawGraph = function() {
                  vm.element = vm.container.append('svg')
                        .attr('width', width)
                        .attr('height', calculateHeight())
                        .style('padding-left', margin.left)
                        .style('padding-top', margin.top);
                  drawAxis();
            };

            vm.controller = function() {
                  vm.container = d3.select('graph');
                  vm.drawGraph();
                  draw();
            };

            function calculateHeight() {
                  return height + (margin.bottom * 2);
            }

            function rotateText() {
                  vm.element.selectAll('.xaxis text')
                        .attr('transform', function() {
                              return 'translate(' + this.getBBox().height*-2 + ',' + this.getBBox().height + ')rotate(-45)';
                        });
            }

            function draw(){

                  var line = d3.svg.line()
                        .x(function(d) { return configureDateAxisScale([padding.left, width - margin.left], 'x')(d.x); })
                        .y(function(d) { return configureAxisScale([height, 0], 'y')(d.y); });

                  vm.element.append('path')
                        .data([vm.data])
                        .attr('class', 'line')
                        .attr('d', line);

                  vm.element.append('path')
                        .data([vm.data])
                        .attr('class', 'line')
                        .attr('d', line);

                  drawAxis();
                  rotateText();
                  date = configureDateRange();
                  vm.startDate = _.head(date);
                  vm.endDate = _.last(date);
            }
      }
})();
