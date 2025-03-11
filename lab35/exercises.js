console.log("Using the for loop");
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

console.log("Using the while loop");
let num = 10;
while (num >= 1) {
    console.log(num);
    num--;
}

console.log("Using the do..while loop");
let userInput;
do {
    userInput = parseInt(prompt("Enter a number greater than 10: "), 10);
} while (userInput <= 10);
console.log("Valid input received:", userInput);

console.log("Looping through an array with for loop");
let fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"];
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

console.log("Using break in a loop");
let numbers = [1, 2, 4, 31, 7, 12, 5, 9];
for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] === 12) {
        console.log("Number 12 is found, stopping the loop.");
        break;
    }
    console.log(numbers[i]);
}

console.log("Using continue in a loop");
numbers = [1, 2, 3, 4, 5, 6, 7];
for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] === 5) continue;
    console.log(numbers[i]);
}
