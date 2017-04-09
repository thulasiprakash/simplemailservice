'use strict';
var myApp = angular.module('mailservice', []);

myApp.controller('HomeCtrl', function($scope, $http) {
    $scope.content = {
        from_email: 'no-reply@test.com',
        api_key: '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'
    };

    $scope.sendMessage = function() {
        var res = $http({
            method: 'POST',
            url: '/sendMail',
            data: $scope.content
        });
        res.success(function(data, status, headers, config) {
            if (data.status === 'SUCCESS') {
                alert('Sent successfully');
            } else if (data.status === 'ERROR') {
                alert(data.message)
            }

        });
        res.error(function(data, status, headers, config) {
            alert("failure message: " + JSON.stringify({
                data: data
            }));
        });
    }
});