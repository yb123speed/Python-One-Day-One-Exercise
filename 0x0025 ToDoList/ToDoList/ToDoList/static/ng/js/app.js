'use strict';

angular.module('myApp', ['ui.router'])
    .controller("HomeCtrl", function ($scope, $http) {
        $scope.list = $http.get("/api/ToDoList")
    })
    .config(function ($stateProvider, $urlRouterProvider) {
        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/static/ng/ng-templates/ng-ToDoList.html',
                controller: 'HomeCtrl'
            });
        $urlRouterProvider.otherwise('/');
    });