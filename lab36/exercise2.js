let message = "Hello from global scope";

function helloGlobal() {
    let localMessage = "Hello from function(local) scope";
    console.log(localMessage);
}

helloGlobal();
console.log(message);
console.log(localMessage);
