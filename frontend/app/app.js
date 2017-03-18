(function () {

      'use strict';

      angular.module('sentimentAnalysis',  [
            'ngRoute',
            'sentimentAnalysis.page',
            'sentimentAnalysis.feature',
            'sentimentAnalysis.constant',
            'd3Module',
            'leaflet-directive'
      ])
      .config([
            '$locationProvider',
            '$routeProvider',
            '$logProvider',

            function($locationProvider, $routeProvider, $logProvider) {
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
                  $logProvider.debugEnabled(false);
            }
      ]);

})();
