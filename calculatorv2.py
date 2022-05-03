
"""-------------------------- Calculator --------------------------"""

# defining the scope of the functions for sum, subtracion, multiplying, and diving
def add(x, y):
  return(x + y)
def subtraction(x, y):
  return(x - y)
def multiplication(x,  y):
  return(x * y)
def divide(x, y):
  return(x / y)

print("1 - sum\n2 - subtraction\n3 - multiplication\n4 - divide")
choice = int(input("enter the operation from 1 to 4: "))

first_number = float(input("enter the first number: "))
second_number = float(input("enter the second number: "))

if choice == 1:
    print(first_number, "+", second_number, "=", add(first_number, second_number))
elif choice == 2:
  print(first_number, "-", second_number, "=", subtraction(first_number, second_number))
elif choice == 3:
  print(first_number, "*", second_number, "=", multiplication(first_number, second_number))
elif choice == 4:
  print(first_number, "/", second_number, "=", divide(first_number, second_number))
else:
    print("invalid operation")