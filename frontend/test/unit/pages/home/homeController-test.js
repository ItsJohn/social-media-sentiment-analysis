describe('sentimentAnalysisController', function() {
      var $controller,
            $scope,
            $timeout,
            $location,
            $q,
            ctrl,
            constants,
            homeService,
            mock_trends;

      beforeEach(function() {
            module('sentimentAnalysis.page');
            module('sentimentAnalysis.feature');
            module('sentimentAnalysis.constant');
      });

      beforeEach(inject(function ($injector) {
            $scope = $injector.get('$rootScope').$new();
            $controller = $injector.get('$controller');
            $location = $injector.get('$location');
            $q = $injector.get('$q');
            $timeout = $injector.get('$timeout');
            homeService = $injector.get('homeService');
            mock_trends = {
                  'data': ['trend1', 'trend2']
            };

            spyOn(homeService, 'getKeywords').and.callFake(function () {
                  var deferred = $q.defer();
                  deferred.resolve(mock_trends)
                  return deferred.promise;
            });

            ctrl = $controller('homeController', {
                  $scope: $scope
            });

      }));

      describe('showMeThisSentiment', function() {
            it('should have 2 genders', function() {
                  // expect(homeService.getKeywords()).toEqual(4);
            });
      });
});
