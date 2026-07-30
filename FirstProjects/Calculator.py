# Resources
import time
import sys

# Default Vars
num1 = None
num2 = None
op = None
allowed_ops = ["+","-","/","x","%","//"]
running = False

     
# Confirmation
ans = input("Would you like to use the calculator? Y/n ")   
if ans == "Y" or ans == "y":
    print("Okay!")
    running = True
else:
    sys.exit()

while running:
# Collecting & Sanitizing & Storing num & op
    def collect_num():
        run_num1 = True
        run_num2 = True
        run_op = True
        while run_num1:
            num1 = input("What is your first number? ") # Asks & stores first number
            try:
                num1 = int(num1)
                run_num1 = False   
            except ValueError:
                try:
                    num1 = float(num1)
                    run_num1 = False
                except ValueError: 
                    print("Not a valid input! Please input a number!")

        while run_op:
            op = input("What is your operation? ") # Asks & stores operation
            if op not in allowed_ops:
                print("Invalid Operiaion. Valid operations are\n+, -, /, x, %")
            elif op in allowed_ops:
                run_op = False

        while run_num2:
            num2 = input("What is your second number? ") # Asks & stores second number
            try:
                num2 = int(num2)
                run_num2 = False
            except ValueError:
                try:
                     num2 = float(num2)
                     run_num2 = False
                except ValueError:
                    print("Not a valid input! Please input a number!")
        return num1, op, num2

# Calulator logic
    def calculate(num1, op, num2):
        print("\nCalculating...")
        time.sleep(1.5)
        if op == "+":
            answer = num1 + num2
        elif op == "-":
            answer = num1 - num2
        elif op == "x":
            answer = num1 * num2
        elif op == "%":
            answer = num1 % num2
        elif op == "//":
            if num2 == 0:
                print("You cannot divide by a zero!")
                return
            answer = num1 // num2
        elif op == "/":
            if num2 == 0:
             print("You cannot divide by zero!")
             return
            answer = round(num1 / num2, 3)

        print("\nResult for", collected_num1,collected_op,collected_num2,":", answer)

        again = input("Would you like to use the calculator again? Y/n ")  

        if again == "Y" or again == "y":
            print("\nOkay!")
        elif again == "N" or again == "n":
            print("\nGoodbye")
            sys.exit()

    collected_num1, collected_op, collected_num2 = collect_num()

    calculate(collected_num1, collected_op, collected_num2)