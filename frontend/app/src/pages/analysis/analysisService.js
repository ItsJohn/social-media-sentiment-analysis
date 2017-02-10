(function () {
      'use strict';

      angular.module('sentimentAnalysis.page')
            .service('analysisService', analysisService);

      analysisService.$inject = [];
      function analysisService() {
            var data, term;
            this.setData = function(returnedData, searchTerm) {
                  data = returnedData;
                  term = searchTerm;
            };
            this.getData = function() {
                  return {
                        'term': term,
                        'data': data
                  };
            };
      };
})();
