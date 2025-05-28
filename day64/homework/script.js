// Prompt for favorite hobby
const hobby = prompt("What is your favorite hobby?");
if (hobby) {
  alert(`Your favorite hobby is: ${hobby}`);
}

// Prompt for first and last name
const first = prompt("Enter your first name:");
const last = prompt("Enter your last name:");
if (first && last) {
  alert(`Full name: ${first} ${last}`);
}

// Prompt for a message and display in <p>
const userMsg = prompt("Enter a message to display on the page:");
if (userMsg) {
  document.getElementById("userMessage").textContent = userMsg;
}

// Prompt for favorite emoji
const emoji = prompt("What's your favorite emoji?");
if (emoji) {
  alert(`Thanks for sharing your favorite emoji: ${emoji}`);
}

// Prompt to set the document title
const pageTitle = prompt("Enter a word to set as the page title:");
if (pageTitle) {
  document.title = pageTitle;
}

// 6) Show input from form in alert
function showTextInput() {
  const input = document.getElementById("textInput").value;
  alert(`You entered: ${input}`);
}

// 7) Change background color from color input
document.getElementById("colorForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent form from reloading the page
  const color = document.getElementById("colorPicker").value;
  document.body.style.backgroundColor = color;
});

// 8) Combine first and last name from form inputs
function combineNames() {
  const first = document.getElementById("firstNameInput").value;
  const last = document.getElementById("lastNameInput").value;
  document.getElementById("fullNameDisplay").textContent = `${first} ${last}`;
}
