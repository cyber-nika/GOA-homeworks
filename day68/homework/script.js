// 2) Check if a Number is Positive, Negative, or Zero
const numInput = Number(prompt("Enter a number:"));
if (numInput > 0) {
  alert("The number is positive.");
} else if (numInput < 0) {
  alert("The number is negative.");
} else {
  alert("The number is zero.");
}

// 3) Check User’s Age for Voting Eligibility
const age = Number(prompt("Enter your age:"));
if (age >= 18) {
  alert("You can vote!");
} else {
  alert("You are not eligible to vote.");
}

// 4) Compare Two Numbers
const firstNum = Number(prompt("Enter the first number:"));
const secondNum = Number(prompt("Enter the second number:"));

if (firstNum > secondNum) {
  alert("The first number is larger.");
} else if (secondNum > firstNum) {
  alert("The second number is larger.");
} else {
  alert("Both numbers are equal.");
}
