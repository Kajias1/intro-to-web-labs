function parseJSON(jsonStr) {
    try {
        let parsedData = JSON.parse(jsonStr);
        console.log("Parsed Object:", parsedData);
    } catch (error) {
        console.error("Invalid JSON format");
    }
}

parseJSON('{"name": "Alice", "age": 25}'); // Valid case
parseJSON('{name: Alice, age: 25}');       // Error case
parseJSON('Invalid JSON String');          // Error case
