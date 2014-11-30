/* configuration file for my angular.js */

//load modules
//second var: what internal modules do I need for my app
var app = angular.module("djangoAppAngular", ["ngResource"]);

//configure my app (configure the module I've created)
app.config(function ($interpolateProvider) {
    //here I set how I call angular variables from html
    //because default angular setting ( {{}} )
    //overrides with django setting ( {{}} )
    $interpolateProvider.startSymbol("{$");
    $interpolateProvider.endSymbol("$}");
});

//global vars 
//app.value('$app', {"title": "my first machete"});

//define controllers 
app.controller('mainController', function ($scope, $http, dataResource) {
    /*$scope.data = [
     /*{id: 101, name: "computador", valor: 30000},
     {id: 102, name: "celular", valor: 24500},
     {id: 103, name: "memoria usb", valor: 78000},
     {id: 104, name: "cuaderno", valor: 125000}*/
    /*
     {contenidoPubli: "fffff", numeroLikesPubli: '0',
     fechaPubli: new Date().toLocaleString()},
     ];*/
    //$scope.data = [$app.get('/aaa')]
    //getdata_view
    $http.get('/json/').success(function (data) {
        //formattedData = JSON.stringify(data);
        //formattedData = JSON.parse(formattedData);
        console.log(data);
        $scope.datos = data;
    });
    $scope.dataResource = dataResource.get();
})

app.factory("dataResource", function ($resource) {
    return $resource('/json/',
        {},
        {get: {method: "GET", isArray: true}
    })
})



//add "save" button
/*$scope.save = function (publicacion) {
    var p = {
        contenidoPubli: publicacion.publi,
        numeroLikesPubli: '0',
        fechaPubli: new Date().toLocaleString(),
    };
    $scope.data.push(p);
    publicacion.publi = "";
    $scope.status = "Elemento guardado!";
};*/


/*app.controller('productsController', function ($scope, $app) {
    //
});*/