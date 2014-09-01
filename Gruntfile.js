module.exports = function(grunt) {
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');
  
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    less: {
      options: {
        compress: true,
      },
      files: {
//        "fleischer_films/static/fleischer_studios/css/styles.css": "fleischer_films/static/fleischer_studios/less/styles.less"
          'styles.css':'styles.less'
      }
    },
    watch: {
      styles: {
        files: ['fleischer_films/static/fleischer_studios/**/*.less'], // which files to watch
        tasks: ['less'],
        options: {
          nospawn: true
        }
      }
    }
  });

  grunt.registerTask('default', ['watch']);
};