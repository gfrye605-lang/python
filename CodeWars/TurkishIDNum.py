def check_valid_tr_number(number):
    if isinstance(number, str):
        try:
            number = int(number)
        except ValueError:
            return False
            
    number = str(number)
    print(len(number))
    print(number)
    if number[0] == "0":
        return False
    elif len(number) != 11:
        return False
    
    num1 = int(number[0])
    num2 = int(number[1])
    num3 = int(number[2])
    num4 = int(number[3])
    num5 = int(number[4])
    num6 = int(number[5])
    num7 = int(number[6])
    num8 = int(number[7])
    num9 = int(number[8])
    num10 = int(number[9])
    num11 = int(number[10])
    
    sum1 = num1 + num3 + num5 + num7 + num9
    sum1 = sum1 * 7
    sum2 = num2 + num4 + num6 + num8
    value = sum1 - sum2

    if value % 10 == number[10]:
        part1 = True
    else:
        part1 = False
    
    ten_digits_sum = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    
    if ten_digits_sum % 10 == num10:
        part2 = True
    else:
        part2 = False
    
    
    if part1 and part2:
        return True
    else:
        return False
    