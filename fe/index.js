let num1 = 10;
let num2 = 15;
let op = "plus";

const answerBlock = document.getElementById("answer-block");

// function that runs on clicking the equals button
const equalsButtonClick = () => {
  console.log("button was clicked!");

  fetchFromBackend().then((res) => {
    console.log(res);
    answerBlock.innerText = res;
  });
};

// function that calls the backend
const fetchFromBackend = async () => {
  const result = await fetch(
    `http://localhost:5000/calculate?num1=${num1}&num2=${num2}&op=${op}`
  );
  return result.text();
};

const display = document.getElementById("display");

function equalsButtonClick(input){
    display.value += input;
}