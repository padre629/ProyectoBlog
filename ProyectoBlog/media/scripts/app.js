/* configuration file for my angular.js */

//load modules
//second var: what internal modules do I need for my app
var app = angular.module("djangoAppAngular", []);

//configure my app (configure the module I've created)
app.config(function ($interpolateProvider) {
  //here I set how I call angular variables from html
  //because default angular setting ( {{}} )
  //overrides with django setting ( {{}} )
  $interpolateProvider.startSymbol("{$");
  $interpolateProvider.endSymbol("$}");
});

//global vars 
app.value('$app', {"title": "my first machete"});

//define controllers 
app.controller('mainController', function($scope, $app){
  $scope.data = [
    {id: 101, name: "computador", valor: 30000},
    {id: 102, name: "celular", valor: 24500},
    {id: 103, name: "memoria usb", valor: 78000},
    {id: 104, name: "cuaderno", valor: 125000}
  ];
  //add "save" button 
  $scope.save = function(producto) {
    var p = {
      id: producto.id, 
      name: producto.name, 
      valor: producto.valor, 
    };
    $scope.data.push(p);
    producto.id = "";
    producto.name = "";
    producto.valor = "";
    $scope.status = "Elemento guardado!";
  };
});
app.controller('productsController', function($scope, $app){
  //
});