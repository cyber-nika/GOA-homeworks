function showAge() {
    alert("I am 15 years old.");
  }
  
  function changeImage() {
    var img = document.getElementById("image");
    if (img.src === "https://upload.wikimedia.org/wikipedia/en/9/96/Meme_Man_on_transparent_background.webp") {
      img.src = "https://upload.wikimedia.org/wikipedia/en/9/96/Meme_Man_on_transparent_background.webp";
    } else {
      img.src = "https://preview.redd.it/1o8zqjm9bqc81.png?auto=webp&s=df1f71e2b420eb084958de96459f284c00053ad1";
    }
  }
  