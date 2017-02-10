module.exports = function(config) {
      config.set({
            basePath: '',
            frameworks: ['jasmine'],
            files: [
                  '../vendor/angular/angular.min.js',
                  '../vendor/jquery/dist/jquery.min.js',
                  '../vendor/angular-route/angular-route.min.js',
                  '../../node_modules/angular-mocks/angular-mocks.js',
                  '../vendor/bootstrap/dist/js/bootstrap.min.js',
                  '../vendor/lodash/dist/lodash.min.js',
                  '../vendor/d3/d3.min.js',
                  '../vendor/spin.js/spin.js',
                  '../vendor/angular-loading-spinner/angular-loading-spinner.js',
                  '../vendor/angular-spinner/angular-spinner.min.js',
                  '../app.js',
                  '../src/constants.js',
                  '../src/pages/pagesModule.js',
                  '../src/features/featureModule.js',
                  '../src/pages/**/*.js',
                  '../src/features/**/*.js',
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
