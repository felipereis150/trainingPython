
"""-------------------------- Calculator --------------------------"""

print("Calculator")

print("1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide")
choice = int(input("Enter operation: "))

if choice ==1 :
  x = int(input("Enter X: "))
  y = int(input("Enter Y: "))
  result = x+y
  print(result)
elif choice == 2:
  x = int(input("Enter X: "))
  y = int(input("Enter Y: "))
  result = x-y
  print(result)
elif choice == 3:
  x = int(input("Enter X: "))
  y = int(input("Enter Y: "))
  result = x*y
  print(result)
elif choice == 4:
  x = int(input("Enter X: "))
  y = int(input("Enter Y: "))
  result = x/y
  print(result)
else:
  print("invalid operation")