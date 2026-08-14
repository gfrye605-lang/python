# Vars
current_age = input("How old are you?: ")
new_age = None

# Functions
def change_age():
    new_age = current_age + 18
    print("You will be", new_age, "in 18 year")

# Data Sanitization
if current_age != int:
    asking_again = True
    while asking_again:
        try: 
            current_age = int(current_age)
            asking_again = False
            change_age()
        except ValueError:
            print("That's not a number! Please input a number!")
            current_age = input("How old are you?: ")