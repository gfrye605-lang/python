# Resources
import time
import sys

# Confirmation
ans = input("Would you like to use the calculator? Y/n ")
if ans == "Y" or "y": 
    print("Okay!")
else:
    sys.exit()

# Collecting & Storing num & op
num1 = int(input("What is your first number? ")) # Asks & stores first number
op = input("What is your operation? ") # Asks & stores operation
num2 = int(input("What is your second number? "))

# Calulator logic
allowed_ops = ["+","-","/","x"]
result = None
def calculate(num1, op, num2):
    if op not in allowed_ops:
        print("Invalid Operiaion. Valid operations are\n+, -, /, x")
    elif op == "+":
        num1 + num2
    return result
    
# Serve user their answer
def resultt(result):
    print("Calculating...")
    print(result)
resultt()