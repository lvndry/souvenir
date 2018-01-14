var submit = document.getElementById('submit');
var input = document.getElementById('souvenir');
var datepicker = document.getElementById('date');

var sendMessage = function() {
  message = input.value //TODO: verify integrity
  date = datepicker.value

  console.log(date);
  console.log(message);

  $.ajax({
    url: "http://localhost:5000/message/new",
    type: 'POST',
    data: {message: input.value, date: date },
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
    url: "http://localhost:5000/message/show/all",
    type: 'GET',
    data: {message: input.value, date: date },
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

submit.addEventListener('click', sendMessage);
