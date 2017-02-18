
var gulp = require('gulp'),
    connect = require('gulp-connect'),
      sass = require('gulp-sass'),
      uglify = require('gulp-uglify'),
      cssMin = require('gulp-minify-css'),
      concat = require('gulp-concat'),
      rename = require('gulp-rename'),
      imageMin = require('gulp-imagemin'),
      eslint = require('gulp-eslint'),
      _ = require('lodash'),
      srcFile = {
            js: './app/src/**/*.js',
            sass: 'app/src/sass/**/*.sass',
            mainSass: 'app/src/sass/main.sass',
            img: 'app/src/img/**/*'
      },
      distFile = {
            js: 'app/dist',
            sass: 'app/dist',
            img: 'app/dist/img'
      },
      distRename = {
            sass: 'style.min.css'
      },
      excludeFiles = [
            '!./app/dist/**',
            '!./app/vendor/**'
      ];

      gulp.task('lint', function () {
            return gulp.src(['./app/**/*.js'])
                  .pipe(eslint())
                  .pipe(eslint.format())
                  .pipe(eslint.failAfterError());
      });
      gulp.task('minifyjs', function() {
            return gulp.src(_.concat([srcFile.js, './app/app.js'], excludeFiles))
                  .pipe(concat('scripts.min.js'))
                  .pipe(uglify())
                  .pipe(gulp.dest(distFile.js))
                  .pipe(connect.reload());
      });

      gulp.task('image', function() {
            gulp.src(srcFile.img)
                  .pipe(imageMin())
                  .pipe(gulp.dest(distFile.img));
      });

      gulp.task('sassReload', function() {
            gulp.src(srcFile.mainSass)
                  .pipe(connect.reload());
      });

      gulp.task('sass', function() {
            return gulp.src(srcFile.mainSass)
                  .pipe(sass())
                  .pipe(cssMin())
                  .pipe(rename(distRename.sass))
                  .pipe(gulp.dest(distFile.sass));
      });

      gulp.task('server', function() {
            return connect.server({
                  root: 'app/',
                  port: 8888,
                  livereload: true
            });
      });

      gulp.task('watch', function() {
            gulp.watch(srcFile.js, ['minifyjs']);
            gulp.watch(srcFile.sass, ['sass']);
            gulp.watch(srcFile.sass, ['sassReload']);
      });

      gulp.task('default', ['minifyjs', 'image', 'sass', 'watch', 'server']);
