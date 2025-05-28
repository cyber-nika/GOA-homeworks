function compareNums(num1, num2) {
  let result = `შედარება ${num1} და ${num2}:\n`;
  result += `${num1} > ${num2} => ${num1 > num2}\n`;
  result += `${num1} >= ${num2} => ${num1 >= num2}\n`;
  result += `${num1} < ${num2} => ${num1 < num2}\n`;
  result += `${num1} <= ${num2} => ${num1 <= num2}\n`;
  result += `${num1} == ${num2} => ${num1 == num2}\n`;
  result += `${num1} === ${num2} => ${num1 === num2}\n`;
  result += `${num1} != ${num2} => ${num1 != num2}\n`;
  result += `${num1} !== ${num2} => ${num1 !== num2}\n`;
  result += `------------------------------\n`;

  document.getElementById('output').textContent += result;
}
compareNums(5, 10);
compareNums(20, '20');
compareNums(15, 15);
