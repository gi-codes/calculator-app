# Calculator app 
# to be able to add digits 

# number_1 = 10, number_2 = 5, operation = "+"
def calculator(x, y, operation):
  answer = 0
  
#   x = int(input("choose x "))
#   y = int(input("choose y "))

#   print(f"the user chose  {x}")
#   print(f"the user chose  {y}") 

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

