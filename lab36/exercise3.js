if (true) {
    var varVariable = "I am using var";
}
console.log(varVariable); // Accessible outside the block

if (true) {
    let letVariable = "I am using let";
}
console.log(letVariable); // ReferenceError

if (true) {
    const constVariable = "I am using const";
}
console.log(constVariable); // ReferenceError
