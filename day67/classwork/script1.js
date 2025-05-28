function userOperations() {

  const confirm1 = confirm("Do you accept the terms?");
  const confirm2 = confirm("Are you over 18?");

  const andResult = confirm1 && confirm2;
  const orResult = confirm1 || confirm2;

  console.log("Confirm 1:", confirm1);
  console.log("Confirm 2:", confirm2);
  console.log("AND Result:", andResult);
  console.log("OR Result:", orResult);
}

window.onload = userOperations;
