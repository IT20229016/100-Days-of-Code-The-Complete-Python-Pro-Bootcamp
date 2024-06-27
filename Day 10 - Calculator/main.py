from art import logo

print(logo)

#Calculator


#add
def add(n1, n2):
  return n1 + n2


#subtract
def subtract(n1, n2):
  return n1 - n2


#devide
def devide(n1, n2):
  return n1 / n2


#multiply
def multiply(n1, n2):
  return n1 * n2


operations = {"+": add, "-": subtract, "/": devide, "*": multiply}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for operator in operations:
  print(operator)
