function handleSubmit(event) {
  event.preventDefault(); 

  const input = document.getElementById("userInput");
  const value = input.value;

  console.log("input:", value);
}
