from art import logo

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

def calculator():
  print(logo)
  cont = True
  num1 = float(input("Whats the first number? "))
  operations = {"+":add,"-":subtract,"*":multiply,"/":divide}
  while(cont):
    for key in operations:
      print(key)
    s = input("Choose an above operation ")
    num2 = float(input("Whats the next number? "))
    
    if s not in operations.keys():
      print("Invalid operation")
    
    function = operations[s]
    ans = function(num1,num2)
    print(f"{num1} {s} {num2} = {ans}")
  
    ask = input(f"Do you want to continue with {ans} as the first number? Select N to begin a new calculation. Y/N \n").upper()
    if ask == "N":
      cont = False
      calculator()
    elif ask == "Y":
      num1 = ans
    else:
      print("Goodbye!")
      cont = False

calculator()
  