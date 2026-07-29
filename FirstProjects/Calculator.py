# Resources
import time
import sys

# Confirmation
ans = input("Would you like to use the calculator? Y/n ")
if ans == "Y": 
    print("Okay!")
else:
    sys.exit()

# Collecting & Storing num & op
num1 = int(input("What is your first number? ")) # Asks & stores first number
op = input("What is your operation? ") # Asks & stores operation
num2 = int(input("What is your second number? "))

# Calulator logic
if num1 or num2 != int:
    print("Please enter a number!")

# Serve user their answer
print("Calculating...")
time.sleep(3000)