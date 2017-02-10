module.exports = function(config) {
      config.set({
            basePath: '',
            frameworks: ['jasmine'],
            files: [
                  '../../frontend/app/vendor/angular/angular.min.js',
                  '../../frontend/app/vendor/jquery/dist/jquery.min.js',
                  '../../frontend/app/vendor/angular-route/angular-route.min.js',
                  '../../frontend/node_modules/angular-mocks/angular-mocks.js',
                  '../../frontend/app/vendor/bootstrap/dist/js/bootstrap.min.js',
                  '../../frontend/app/vendor/lodash/dist/lodash.min.js',
                  '../../frontend/app/vendor/d3/d3.min.js',
                  '../../frontend/app/vendor/spin.js/spin.js',
                  '../../frontend/app/vendor/angular-loading-spinner/angular-loading-spinner.js',
                  '../../frontend/app/vendor/angular-spinner/angular-spinner.min.js',
                  '../../frontend/app/app.js',
                  '../../frontend/app/src/constants.js',
                  '../../frontend/app/src/pages/pagesModule.js',
                  '../../frontend/app/src/features/featureModule.js',
                  '../../frontend/app/src/pages/**/*.js',
                  '../../frontend/app/src/features/**/*.js',
                  './unit/pages/home/homeController-test.js'
            ],
            exclude: [
            ],
            preprocessors: {
            },
            reporters: ['progress'],
            port: 9876,
            colors: true,
            logLevel: config.LOG_INFO,
            autoWatch: true,
            browsers: ['PhantomJS'],
            singleRun: true,
            concurrency: Infinity
      })
}
