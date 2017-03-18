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
                        left: 30
                  };

            function configureAxisScale(range) {
                  return d3.scale.linear()
                        .domain([0, vm.data['maxY']])
                        .range(range);
            }

            function configureDateRange() {
                  return [vm.data['min'], vm.data['max']];
            }

            function configureDateAxisScale(range) {
                  return d3.time.scale()
                        .domain(configureDateRange())
                        .nice(d3.time.minute)
                        .range(range);
            }

            function drawAxis() {
                  vm.element.selectAll('g').remove();
                  var xAxis = d3.svg.axis()
                        .scale(configureDateAxisScale([0, width]))
                        .orient('bottom')
                        .outerTickSize(0)
                        .tickPadding(10);

                  var yAxis = d3.svg.axis()
                        .scale(configureAxisScale([height, 0]))
                        .orient('left')
                        .innerTickSize(-width)
                        .outerTickSize(0)
                        .tickPadding(10);

                  vm.element.append('g')
                        .attr('class', 'x axis')
                        .attr('transform', 'translate(0,' + height + ')')
                        .call(xAxis);

                  vm.element.append('g')
                        .attr('class', 'y axis')
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
                  vm.element.selectAll('.x text')
                        .attr('transform', function() {
                              return 'translate(' + this.getBBox().height*-2 + ',' + this.getBBox().height + ')rotate(-45)';
                        });
            }

            function draw(){
                  var date;
                  var line = d3.svg.line()
                        .interpolate('basis')
                        .x(function(d) { return configureDateAxisScale([0, width])(d.x); })
                        .y(function(d) { return configureAxisScale([height, 0])(d.y); });

                  _.forEach(vm.data['lines'], function(value, sentiment) {
                        vm.element.append('path')
                              .data([value])
                              .attr('class', sentiment)
                              .attr('d', line);
                  });

                  drawAxis();
                  rotateText();
                  date = configureDateRange();
                  vm.startDate = _.head(date);
                  vm.endDate = _.last(date);
            }
      }
})();
