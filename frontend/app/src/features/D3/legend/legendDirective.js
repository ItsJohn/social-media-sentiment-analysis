(function () {
      'use strict';

      angular.module('sentimentAnalysis.feature')
            .directive('legend', legend);

      function legend() {
            function link(scope) {
                  scope.controller();
            }
            return {
                  restrict: 'E',
                  scope: {
                        data: '=data'
                  },
                  link:link,
                  controller: 'legendController'
            };
      }
})();
