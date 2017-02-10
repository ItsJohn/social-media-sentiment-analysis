module.exports = function(config) {
      config.set({
            basePath: '',
            frameworks: ['jasmine'],
            files: [
                  '../app/vendor/angular/angular.min.js',
                  '../app/vendor/jquery/dist/jquery.min.js',
                  '../app/vendor/angular-route/angular-route.min.js',
                  '../node_modules/angular-mocks/angular-mocks.js',
                  '../app/vendor/bootstrap/dist/js/bootstrap.min.js',
                  '../app/vendor/lodash/dist/lodash.min.js',
                  '../app/vendor/d3/d3.min.js',
                  '../app/vendor/spin.js/spin.js',
                  '../app/vendor/angular-loading-spinner/angular-loading-spinner.js',
                  '../app/vendor/angular-spinner/angular-spinner.min.js',
                  '../app/app.js',
                  '../app/src/constants.js',
                  '../app/src/pages/pagesModule.js',
                  '../app/src/features/featureModule.js',
                  '../app/src/pages/**/*.js',
                  '../app/src/features/**/*.js',
                  'unit/pages/home/homeController-test.js'
            ],
            exclude: [
            ],
            preprocessors: {
            },
            reporters: ['progress', 'coverage'],
            port: 9876,
            colors: true,
            logLevel: config.LOG_INFO,
            autoWatch: true,
            browsers: ['PhantomJS'],
            singleRun: true,
            concurrency: Infinity
      })
}
