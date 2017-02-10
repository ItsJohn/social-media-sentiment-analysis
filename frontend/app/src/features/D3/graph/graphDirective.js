(function () {
      'use strict';

      angular.module('sentimentAnalysis.feature')
            .directive('graph', graph);

      function graph() {
            function link(scope) {
                  scope.controller();
            };
            return {
                  restrict: 'E',
                  scope: {
                        width: '@width',
                        height: '@height',
                        data: '=data'
                  },
                  link:link,
                  templateUrl: 'src/features/D3/graph/graph.html',
                  controller: 'graphController'
            };
      }
})();
