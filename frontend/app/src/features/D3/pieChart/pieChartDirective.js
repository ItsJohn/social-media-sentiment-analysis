(function () {
      'use strict';

      angular.module('sentimentAnalysis.feature')
            .directive('piechart', pieChart);

      function pieChart() {
            function link(scope) {
                  scope.startPie();
            }
            return {
                  restrict: 'E',
                  scope: {
                        width: '@',
                        height: '@',
                        data: '=',
                        radius: '@'
                  },
                  link:link,
                  // templateUrl: 'src/features/D3/graph/graph.html',
                  controller: 'pieChartController'
            };
      }
})();
