const { src, dest, watch, series } = require('gulp')
const sass = require('gulp-sass')(require('sass'));

function buildStyles() {
    return src('static/scss/**/*.scss')
        .pipe(sass())
        .pipe(dest('static/css'))
}

function watchTask() {
    watch(['static/scss/**/*.scss'], buildStyles)
}

exports.default = series(buildStyles, watchTask)