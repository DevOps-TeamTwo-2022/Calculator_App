import os

def askInput():
    
  print("Simple Calculator\n===============================\n")
  print("Calculatable features\n===============================")
  print("1) Addition")
  print("2) Subtraction")
  print("3) Division")
  print("4) Multiplication")
  print("5) Exponents, Power of")
  print("\n0) Exit\n")    
    
  userInput = input("Enter Selection: ")
    
  userInput = str(userInput)
    
  checkUserInput(userInput)
    
def checkUserInput(userInput):    
  if userInput == "1" or userInput == "1)":
    clearScreen()
    addition()
        
  elif userInput == "2" or userInput == "2)":
    clearScreen()
    subtraction()
        
  elif userInput == "3" or userInput == "3)":
    clearScreen()
    multiplication()
        
  elif userInput == "4" or userInput == "4)":
    clearScreen()
    division()
        
  elif userInput == "5" or userInput == "5)":
    clearScreen()
    exponents()
        
  elif userInput == "0" or userInput == "0)":
    quit()
    
  else:
    clearScreen()
    print("\nInvalid input!\n")
    askInput()
        
def inputNumber():
  theInput = input("Enter number: ")
    
  theInput = int(theInput)
    
  return theInput

def addition():
  print("Addition\n===============================\n")

  firstNumber = inputNumber()

  print("\n",firstNumber, "+","\n")
  
  secondNumber = inputNumber()

  clearScreen()

  print("Result\n===============================\n")

  print(firstNumber, "+", secondNumber, "=", firstNumber + secondNumber,"\n")
    
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')    

while True:
  askInput()