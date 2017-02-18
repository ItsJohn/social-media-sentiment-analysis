(function () {
      'use strict';

      angular.module('sentimentAnalysis.page')
            .service('homeService', homeService);

      homeService.$inject = ['$http', 'constants'];
      function homeService($http, constants) {
            this.getKeywords = function() {
                  var url = constants.local_url + 'keywords';
                  return $http({
                        method: 'GET',
                        url: url,
                        dataType: 'json'
                  }).then(function (response) {
                        return response;
                  });
            };
            this.getSentiment = function(term) {
                  var url = constants.local_url + 'getTotalSentiment/' + window.encodeURIComponent(term);
                  return $http({
                        method: 'GET',
                        url: url,
                        dataType: 'json'
                  }).then(function (response) {
                        return response;
                  });
            };
      }
})();
