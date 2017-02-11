(function () {
      'use strict';

      angular.module('sentimentAnalysis.page')
            .controller('homeController', homeController);

      homeController.$inject = ['$scope', 'homeService', 'analysisService', '$location'];
      function homeController($scope, homeService, analysisService, $location) {
            var vm = $scope;

            homeService.getKeywords().then(function(trend) {
                  vm.trends = trend['data'];
            });

            vm.showMeThisSentiment = function(term) {
                  homeService.getSentiment(term).then(function(data) {
                        analysisService.setData(data['data'], term);
                        $location.path('analysis')
                  });
            };

            vm.searchTerm = function() {
                  vm.showMeThisSentiment(vm.term);
            };
      }
})();
