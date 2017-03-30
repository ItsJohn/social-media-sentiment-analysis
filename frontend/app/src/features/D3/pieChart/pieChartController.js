(function () {
      'use strict';

      angular.module('sentimentAnalysis.feature')
            .controller('pieChartController', pieChartController);

      pieChartController.$inject = ['$scope', 'd3'];
      function pieChartController($scope, d3) {
            var vm = $scope,
                  radius = vm.radius | _.min([vm.width, vm.height]) / 2,
                  height = vm.radius * 2,
                  width = vm.radius * 2;

            vm.startPie = function() {
                  vm.container = d3.select('piechart').append('svg')
                        .attr('width', width)
                        .attr('height', height)
                        .append('g')
                        .attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')');
                  drawPie();
            };

            function drawPie() {
                  vm.pie = d3.layout.pie()
                        .sort(null)
                        .value(function(d) {
                              return d.value;
                        });
                  drawArc();
            }

            function drawArc() {
                  vm.arc = d3.svg.arc()
                        .outerRadius(radius - 10)
                        .innerRadius(0);
                  drawSection();
            }

            function drawSection() {
                  vm.section = vm.container.selectAll('.arc')
                        .data(vm.pie(vm.data))
                        .enter()
                        .append('g')
                        .attr('class', 'arc');
                  drawSlice();
            }

            function drawSlice() {
                  vm.section.append('path')
                        .attr('d', vm.arc)
                        .style('fill', function(d) {
                              return d.data.color;
                        });
                  drawText();
            }

            function drawText() {
                  vm.section.append('text')
                        .attr('transform', function(d) {
                              return 'translate(' + vm.arc.centroid(d) + ')';
                        })
                        .attr({
                              'dy': '.35em',
                              'class': 'fa-thumbs-o-up'
                        });
            }
      }
})();
