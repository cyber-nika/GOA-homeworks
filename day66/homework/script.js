// === COMPARISONS ===

// 1) Check if two numbers are equal
let num1 = 10, num2 = 10;
console.log("Equal:", num1 == num2); // true

// 2) Check if a number is greater than another
let a = 15, b = 10;
console.log("Greater:", a > b); // true

// 3) Check if a number is less than or equal to another
let x = 5, y = 5;
console.log("Less than or equal:", x <= y); // true

// 4) Check if two numbers are not equal
let m = 20, n = 25;
console.log("Not equal:", m != n); // true

// 5) Check if a number is greater than or equal to 100
let score = 120;
console.log(">= 100:", score >= 100); // true

// === CONFIRM BOXES ===

// 7) Confirm on page load
let onLoadConfirm = confirm("Do you want to continue?");
alert("Your answer was: " + onLoadConfirm);

// 8) Confirm on button click
function askConfirmation() {
  let result = confirm("Are you sure?");
  console.log("Button confirm result:", result);
}

// 9) Confirm result shown in alert (already handled on load)

// === FORM HANDLING ===

// 10) Log value of input with name="username"
document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const username = this.elements["username"].value;
  console.log("Username:", username);
});

// 11) Clear email input
function clearEmail() {
  document.getElementsByName("email")[0].value = "";
}

// 12) Alert phone input
function alertPhone() {
  const phone = document.getElementsByName("phone")[0].value;
  alert("Phone number: " + phone);
}
