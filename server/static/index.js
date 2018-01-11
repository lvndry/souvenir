submit = document.getElementById('submit');
input = document.getElementById('message');
console.log('input: ' + input);

sendMessage = function() {
  message = input.value
  console.log(message);
}
submit.addEventListener('click', sendMessage);
