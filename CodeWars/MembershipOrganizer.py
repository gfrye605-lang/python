data = [(45, 12), (55, 21), (19, -2), (104, 20)]

def open_or_senior(data):
    output = []
    for num1, num2 in data:
        if num1 >= 55 and num2 > 7:
            output.append("Senior")
        elif num1 < 55 or num2 < 7:
            output.append("Open")
        else:
            output.append("Open")
    return output
open_or_senior(data)

print(open_or_senior(data))