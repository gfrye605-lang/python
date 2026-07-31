number = 15

def solution(number):
# Handle negatives & zeros
    if number <= 0:
        return 0

    total_sum = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum = total_sum + i
            print(total_sum)
    return total_sum

solution(number)