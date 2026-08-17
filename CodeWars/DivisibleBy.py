def divisible_by(numbers, divisor):
    i = 0
    p = []
    getting_numbers = True
    for getting_numbers in numbers:
        current_num = numbers[i]
        print(current_num)
        ans = current_num % divisor
        print(ans)
        if ans == 0:
            p.append(current_num)
            print(p)
            i += 1
        elif ans != 0:
            print("Number not divisible by", divisor)
            i += 1
        if IndexError:
            getting_numbers = False
        else:
      #      print(numbers[i])    
            i += 1
pass

divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1)