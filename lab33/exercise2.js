var username = "Alice";
let age = 25;
const country = "USA";

console.log(username, age, country);

username = "Bob";
age = 30;
// country = "Canada" <- will throw an error: assignment to constant variable

console.log(username, age, country);