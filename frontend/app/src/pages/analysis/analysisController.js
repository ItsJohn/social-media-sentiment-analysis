(function () {
      'use strict';

      angular.module('sentimentAnalysis.page')
            .controller('analysisController', analysisController);

      analysisController.$inject = ['$scope', '$location', 'analysisService'];
      function analysisController($scope, $location, analysisService) {
            var vm = $scope,
                  positive,
                  negative,
                  info = analysisService.getData(),
                  data = info['data'];

            vm.showLoading = true;

            if(_.isUndefined(info['term'])) {
                  $location.path('home');
            } else {
                  vm.tweets = data['tweets'];
                  vm.term = _.startCase(info['term']);
                  positive = data['sentiment']['positive'];
                  negative = data['sentiment']['negative'];
            }

            if(data['coordinates']['length'] > 0) {
                  vm.center = {
                        'lng': 0,
                        'lat': 20,
                        'zoom': 2
                  };
                  vm.paths = {};
                  _.forEach(data['coordinates'], function(coord, i) {
                        vm.paths['c' + i] = {
                              weight: 2,
                              color: '#ff612f',
                              latlngs: coord,
                              radius: 10,
                              type: 'circleMarker'
                        };
                  });
                  vm.showMap = true;
            } else {
                  vm.showMap = false;
            }

            vm.data = [];
            _.forEach(data['tweets'], function(tweet) {
                  vm.data.push({
                        'x': new Date(tweet['timestamp']),
                        'y': tweet['retweet']
                  });
            });

            vm.pie = [{
                  'name': 'positive',
                  'value': positive | 0,
                  'color': '#2F47FF'
            }, {
                  'name': 'negative',
                  'value': negative | 0,
                  'color': '#FF4D3C'
            }];

            vm.showLoading = false;
      }
})();
