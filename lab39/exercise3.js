function startCounter() {
  let counter = 1;
  const intervalId = setInterval(() => {
    console.log(`Counter: ${counter}`);
    counter++;
    if (counter > 5) {
      clearInterval(intervalId);
      startCounter();
    startCounter();
    }
  }, 1000);
}

startCounter();
