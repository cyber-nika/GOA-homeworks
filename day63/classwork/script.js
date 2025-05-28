function greet() {
    const userName = prompt("დაწერეთ თქვენი სახელი:");
    const paragraph = document.getElementById("greetParagraph");
    paragraph.textContent = `Welcome ${userName}!`;
}

document.getElementById("greetParagraph").addEventListener("click", greet);
