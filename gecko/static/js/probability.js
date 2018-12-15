var rmsApp = angular.module('rms', []);

rmsApp.controller('RMSController', function($scope, $http) {

   $scope.fields = ['age', 'gender', 'smoke', 'drink']

   $scope.model_fields = {'age': 'age',
                          'gender': 'gender',
                          'smoke': 'is_smoker',
                          'drink': 'is_alcoholic'}

   $scope.plot_data = function(chart){
      console.log(chart)
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        console.log(chart)
        var data = google.visualization.arrayToDataTable(chart);
        var options = {
          title: 'My Daily Activities',
          is3D: true,
        };
        var get_container = document.getElementById('piechart_3d')
        var chart = new google.visualization.PieChart(get_container);
        get_container.width = "900px";
        get_container.height = "500px";
        chart.draw(data, options);
      }
   }

   $scope.plot_table = function(data){
        var headers='<thead>'
        var first_row = '<tr>'
        var second_row = '<tr>'
        angular.forEach(data, function(field) {
           headers += "<th>" + field[0] + "</th>"
           first_row += '<td>' + field[1] + '</td>'
           second_row += '<td>' + field[2] + '</td>'
        });
        headers += "</thead><tbody>"
        first_row += '</tr>'
        second_row += '</tr>'
        ht = headers + first_row + second_row + '</tbody>';
        $('#costlist').html(ht);
   }

   $scope.GetClaimProbablitiyField = function(){
      var request_data = {}
      angular.forEach($scope.fields, function(field) {
          value = $("#" + field).val();
          if(value != ''){
             query_model = $scope.model_fields[field]
             request_data[query_model] = value
          }
      });
      return request_data
   }

   $scope.GetClaimProbablitiy = function(){
      var data = $scope.GetClaimProbablitiyField()
      $http({
         method : "GET",
         data : data,
         url : "/calculation/",
         headers: {'Content-Type': 'application/x-www-form-urlencoded'}
       }).then(function mySuccess(response) {
           var response = response.data;
           $scope.plot_data(response.chart)
           $scope.plot_table(response.table)
         }, function myError(response) {
             alert("Unable to fetch data.")
       });
   }

});
