var submit = document.getElementById('submit');
var input = document.getElementById('souvenir');
var datepicker = document.getElementById('date');

var sendMessage = function() {
  memory = input.value //TODO: verify integrity
  date = datepicker.value

  $.ajax({
    url: "http://localhost:5000/memory/new",
    type: 'POST',
    data: {title: title.value, memory: input.value, date: date},
    dataType: 'json'
  })
  .done(function(data) {
    console.log(data);
    console.log("success");
  })
  .fail(function(err) {
    console.log(err);
    console.log("error");
  })
  .always(function() {
    console.log("complete");
  });
}

var getAll = function () {
  $.ajax({
    url: "http://localhost:5000/memory/show/all",
    type: 'GET',
    dataType: 'json'
  })
    .done(function(data) {
      console.log(data);
      console.log("success");
    })
    .fail(function(err) {
      console.log(err);
      console.log("error");
    })
    .always(function() {
      console.log("complete");
    });
}

var getOne = function (id) {

}

var updateOne = function(id) {

}

// submit.addEventListener('click', sendMessage);
$("#sam").click(function(){
    window.location = '/memory/show/all';
})

$("#nm").click(function(event) {
  window.location = '/memory/new';
});
