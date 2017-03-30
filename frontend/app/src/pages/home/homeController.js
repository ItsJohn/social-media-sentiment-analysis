(function () {
      'use strict';

      angular.module('sentimentAnalysis.page')
            .controller('homeController', homeController);

      homeController.$inject = ['$scope', 'homeService', 'analysisService', '$location'];
      function homeController($scope, homeService, analysisService, $location) {
            var vm = $scope,
                  colorPalette = ['#D0CABF', '#DDA185', '#1dc786', '#b470ad', '#42d2ed'];

            vm.term = {};
            vm.lock = false;

            function setPlatforms(platforms) {
                  if(platforms.length > 2) {
                        vm.platforms = platforms;
                  }
            }

            function getColourNumber() {
                  return Math.floor(Math.random() * colorPalette.length);
            }

            homeService.getKeywords().then(function(trend) {
                  vm.trends = [];
                  setPlatforms(trend['data']['platforms']);
                  _.forEach(trend['data']['keyword'], function(term) {
                        var trends = {};
                        trends['term'] = term;
                        trends['color'] = colorPalette[getColourNumber()];
                        vm.trends.push(trends);
                  });
            });

            vm.showMeThisSentiment = function(term) {
                  vm.term.word = 'This might take a few seconds... Currently looking for opinions regarding ' + term['word'];
                  $('.form-control').css({'width': 90 + '%', 'text-align': 'center'});
                  homeService.getSentiment(term).then(function(data) {
                        analysisService.setData(data['data'], term['word']);
                        $location.path('analysis');
                  });
            };

            vm.keywordSentiment = function(term) {
                  vm.lock = true;
                  vm.showMeThisSentiment({
                        'word': term,
                        'platform': 'All'
                  });
            };

            vm.searchTerm = function() {
                  if(!_.isUndefined(vm.term.word)) {
                        if(_.isUndefined(vm.term.platform)) {
                              vm.term.platform = 'All';
                        }
                        vm.lock = true;
                        vm.showMeThisSentiment(vm.term);
                  }
            };
      }
})();
