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
                  data = info['data'],
                  positiveColor = '#2F47FF',
                  negativeColour = '#FF4D3C';


            if(_.isUndefined(info['term'])) {
                  $location.path('home');
            } else {
                  vm.tweets = data['tweets'];
                  vm.term = _.startCase(info['term']);
                  positive = data['sentiment']['positive'];
                  negative = data['sentiment']['negative'];

                  vm.legend = [{
                        'name': 'positive',
                        'color': positiveColor
                  }, {
                        'name': 'Negative',
                        'color': negativeColour
                  }];

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

                  var max = [];
                  var new_data = {};
                  _.forEach(data['graph'], function(graph, key) {
                        new_data[key] = [];
                        _.forEach(graph, function(value) {
                              max.push(value['y']);
                              new_data[key].push({
                                    'y': value['y'],
                                    'x': new Date(value['x'])
                              });
                        });
                  });

                  vm.data = {
                        'max': new Date(data['newest']),
                        'min': new Date(data['latest']),
                        'maxY': _.max(max),
                        'lines': new_data
                  };

                  vm.pie = [{
                        'name': 'positive',
                        'value': positive | 0,
                        'color': positiveColor
                  }, {
                        'name': 'negative',
                        'value': negative | 0,
                        'color': negativeColour
                  }];
            }
      }
})();
