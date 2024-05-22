const buttonClick = () => {
  console.log("button was clicked!");
};

const fetchFromBackend = async () => {
  const result = await fetch("http://localhost:5000");
  const res = result.text();
  console.log(res);
};

fetchFromBackend();
