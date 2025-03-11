function divide(a, b) {
    if (b === 0) throw new Error("Divisor cannot be zero");
    return a / b;
}

try {
    console.log(divide(10, 2));
} catch (error) {
    console.error("Cannot divide by zero");
}

try {
    console.log(divide(10, 0));
} catch (error) {
    console.error("Cannot divide by zero");
}
