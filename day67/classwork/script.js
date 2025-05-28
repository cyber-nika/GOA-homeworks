const student = {
  name: "nika",
  surname: "chubunidze",
  academy: "GOA academy",
  city: "tbilisi",
  role: "student",
  favColor: "blue",
  fullName: function() {
    console.log(this.name + " " + this.surname);
  },
  showFavColor: function() {
    console.log(this.favColor);
  }
};
console.log(student);
console.log(student.city);
student.fullName();
student.favColor = "Green";
console.log(student.favColor);
