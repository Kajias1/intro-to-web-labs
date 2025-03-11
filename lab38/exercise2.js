const numbers = [12, 71, 28, 59, 26, 83, 14];

let sum = 0;

for (let i = 0; i < numbers.length; i++) {
    console.log("Current number:", numbers[i]);
    if (numbers[i] % 2 === 0) {
        sum += numbers[i];
    }
}

console.log("Total sum of even numbers:", sum);
