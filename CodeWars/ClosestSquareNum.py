def nearest_sq(n):
    squares = [i**2 for i in range(1, 101)]
    num_plus = n
    num_minus = n
    finding_num_plus = True

    while finding_num_plus:
        if num_plus in squares:
            return(num_plus)
        else:
            num_plus += 1
        if num_minus in squares:
            return(num_minus)
        else:
            num_minus -= 1