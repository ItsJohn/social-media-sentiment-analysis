(function () {

      'use strict';

      angular.module('sentimentAnalysis',  [
            'ngRoute',
            'sentimentAnalysis.page',
            'sentimentAnalysis.feature',
            'sentimentAnalysis.constant',
            'd3Module',
            'ngLoadingSpinner',
            'leaflet-directive'
      ])
      .config([
            '$locationProvider',
            '$routeProvider',

            function($locationProvider, $routeProvider) {
                  $locationProvider.hashPrefix('!');
                  $routeProvider
                  .when('/', {
                        controller: 'homeController',
                        templateUrl: 'src/pages/home/home.html'
                  })
                  .when('/analysis', {
                        controller: 'analysisController',
                        templateUrl: 'src/pages/analysis/analysis.html'
                  })
                  .otherwise({
                        redirectTo: '/'
                  });
            }
      ]);

})();
