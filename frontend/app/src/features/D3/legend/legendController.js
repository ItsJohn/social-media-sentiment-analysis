(function () {
      'use strict';

      angular.module('sentimentAnalysis.feature')
            .controller('legendController', legendController);

      legendController.$inject = ['$scope', 'd3'];
      function legendController($scope, d3) {
            var vm = $scope;

            function drawItems() {
                  vm.element.selectAll('text')
                        .data(vm.data, function(d) { return d.name; })
                        .call(function(d) { d.enter().append('text'); })
                        .call(function(d) { d.exit().remove(); })
                        .attr('y', function(d,i) { return i + 1.1 + 'em'; })
                        .attr('x','1.1em')
                        .text(function(d) { return _.upperFirst(d.name); });

                  vm.element.selectAll('circle')
                        .data(vm.data, function(d) { return d.color; })
                        .call(function(d) { d.enter().append('circle'); })
                        .call(function(d) { d.exit().remove(); })
                        .attr('cy', function(d,i) { return i + 0.75 + 'em'; })
                        .attr('cx', 0.5 + 'em')
                        .attr('r', '0.4em')
                        .style('fill', function(d) { return d.color; });
            }

            function drawBox() {
                  vm.container.append('rect')
                        .classed('legend-box', true);

                  vm.element = vm.container.append('g')
                        .classed('legend-items', true);
                  drawItems();
            }

            vm.controller = function() {
                  vm.container = d3.select('legend')
                        .append('svg');
                  drawBox();
                  vm.container.attr('width', $('.legend-items').width() + 10)
                        .attr('height', $('.legend-items').height() + 10);
            };
      }
})();
