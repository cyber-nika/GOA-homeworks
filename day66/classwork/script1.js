const form = document.getElementById('myForm');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const inputValue = form.userInput.value;

  alert("შენ შეიყვანე: " + inputValue);
});
