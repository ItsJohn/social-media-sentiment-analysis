(function () {
      'use strict';

      angular.module('sentimentAnalysis.page')
            .controller('analysisController', analysisController);

      analysisController.$inject = ['$scope', '$location', 'analysisService'];
      function analysisController($scope, $location, analysisService) {
            var vm = $scope,
                  positive,
                  negative,
                  data = analysisService.getData();

            vm.showLoading = true;
            
            if(_.isUndefined(data['term'])) {
                  $location.path('home');
            } else {
                  vm.tweets = data['data']['tweets'];
                  vm.term = _.startCase(data['term']);
                  positive = data['data']['sentiment']['positive'];
                  negative = data['data']['sentiment']['negative'];
            }

            vm.data = [
            {x: 0, y: 5},
            {x: 1, y: 8},
            {x: 2, y: 13},
            {x: 3, y: 12},
            {x: 4, y: 16},
            {x: 5, y: 21},
            {x: 6, y: 18},
            {x: 7, y: 23},
            {x: 8, y: 24},
            {x: 9, y: 28},
            {x: 10, y: 35},
            {x: 11, y: 30},
            {x: 12, y: 32},
            {x: 13, y: 36},
            {x: 14, y: 40},
            {x: 15, y: 38},
            {x: 16, y: 24},
            {x: 17, y: 28},
            {x: 18, y: 35},
            {x: 19, y: 30},
            {x: 20, y: 32}
            ];

            vm.pie = [{
                        'name': 'positive',
                        'value': positive | 0,
                        'color': '#0f0f86'
                  }, {
                        'name': 'negative',
                        'value': negative | 0,
                        'color': '#860f26'
                  }
            ];

            vm.showLoading = false;
      }
})();
