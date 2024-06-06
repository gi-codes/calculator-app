let num1 = 10;
let num2 = 15;
let op = "plus";

const answerBlock = document.getElementById("answer-block");

const display = document.getElementById("display");


// function that runs on clicking the equals button
const equalsButtonClick = () => {
  console.log("button was clicked!");

  num2= display.value 

  fetchFromBackend().then((res) => {
    console.log(res.answer);
    answerBlock.innerText = res.answer;
    display.value = res.answer;
  });
};

// function that calls the backend
const fetchFromBackend = async () => {
  const result = await fetch(
    `http://localhost:5000/calculate?num1=${num1}&num2=${num2}&op=${op}`
  );
  return result.json();
};

function numberButtonClick(input){
    display.value += input;
    console.log(input)
}

const opButtonClick = (input) => {
  console.log(input)
  op= input
  num1= display.value 
  clearButtonClick()
}

const clearButtonClick = () => {
  console.log("cleared")
  display.value = ""
}