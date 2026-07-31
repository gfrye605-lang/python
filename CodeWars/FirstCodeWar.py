number = int(input("Type a number "))

def make_negative( number ):
    if number > 0:
        number = -number
        print("Positive to negative", number)
    elif number < 0:
        print("Already negative", number)
    elif number == 0:
        print("Number is zero", number)
    return number

make_negative(number)