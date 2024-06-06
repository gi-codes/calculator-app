# Calculator app 
# to be able to add digits 

# number_1 = 10, number_2 = 5, operation = "+"
def calculator(x, y, operation):
  answer = 0
  
  try:
    x = float(x)
    y = float(y)
  except Exception:
    raise ValueError("num1 and num2 should be numbers")

  if(operation == "plus"):
    answer = x + y
  elif(operation == "subtract"):
    answer = x - y
  elif(operation== "multiply"):
    answer = x * y
  elif(operation== "divide"):
    if y == 0:
      raise ValueError("Cannot divide by zero")
    else:
      answer = x / y
  else:
    raise ValueError("Please provide a math operation; +, -, *, / ")
  
  print(f"the result will be {answer}")
  return answer

