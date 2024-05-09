# Calculator app 
# to be able to add digits 

# number_1 = 10, number_2 = 5, operation = "+"
def calculator(x, y, operation):
  answer = 0
  
  user_x = int(input("choose x "))
  user_y = int(input("choose y "))

  print(f"the user chose  {user_x}")
  print(f"the user chose  {user_y}")

  result = user_x + user_y
  print(f"the result will be {result}")

#   if(operation == "+"):
#     answer = x + y
#   elif(operation == "-"):
#     answer = x - y
#   elif(operation== "*"):
#     answer = x * y
#   elif(operation== "/"):
#     answer = x / y
#   return answer




result = calculator(10, 5, "/")
# print(f"the result is: {result}")
#add user 