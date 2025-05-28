// ===== 1–6: Working with Objects =====

// 1) Create an empty object
const emptyObj = {};

// 2) Create an object with your name, age, and city
const person = {
  name: "Alice",
  age: 30,
  city: "New York"
};

// 3) Access the value of a property in an object
console.log("Name:", person.name); // or person['name']

// 4) Add a new property to an existing object
person.country = "USA";
console.log("Updated object with country:", person);

// 5) Create a nested object
const user = {
  id: 1,
  profile: {
    username: "alice123",
    email: "alice@example.com"
  }
};
console.log("Nested object email:", user.profile.email);

// 6) Change the value of an existing property
person.age = 31;
console.log("Updated age:", person.age);


// ===== 8–11: Logical Operators =====

// 8) Check if two numbers are both greater than 10
let num1 = 15, num2 = 20;
console.log("Both > 10:", num1 > 10 && num2 > 10); // true

// 9) Check if at least one of two conditions is true
let a = 5, b = 12;
console.log("At least one > 10:", a > 10 || b > 10); // true

// 10) Use the NOT operator to invert a boolean value
let isOnline = true;
console.log("Inverted isOnline:", !isOnline); // false

// 11) Combine multiple logical operations
let x = 8, y = 12, z = 20;
console.log("Complex logic:", (x > 5 && y < 15) || z === 25); // true


// ===== 12–16: Type Conversion =====

// 12) Convert a number to a string using String()
let num = 123;
let numStr = String(num);
console.log("Number to string:", numStr, typeof numStr);

// 13) Convert a boolean to a string using String()
let isHappy = false;
let boolStr = String(isHappy);
console.log("Boolean to string:", boolStr, typeof boolStr);

// 14) Convert a string to a number
let strNum = "456";
let convertedNum = Number(strNum);
console.log("String to number:", convertedNum, typeof convertedNum);

// 15) Use Number() to convert a boolean
let boolValue = true;
let numFromBool = Number(boolValue);
console.log("Boolean to number:", numFromBool); // 1

// 16) Number() on a non-numeric string
let badString = "hello";
let result = Number(badString);
console.log("Non-numeric string to number:", result); // NaN
