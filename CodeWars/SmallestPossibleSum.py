def solution(lst):
    smallest = float("inf")
    second_smallest = float("inf")

    for x in lst:
        if x < smallest:
            second_smallest = smallest
            smallest = x
        elif x < second_smallest:
            second_smallest = x
    print(smallest + second_smallest)
    return smallest + second_smallest

solution([1, 21, 55])