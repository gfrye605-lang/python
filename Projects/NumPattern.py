def number_pattern(n):
    send_back = []
    if not isinstance (n, int):
        return("Argument must be an integer value.")
    if n <= 0:
        return("Argument must be an integer greater than 0.")    
    elif n > 0:  
        for num in range(n):
            send_back.append(n)
            n -= 1
        send_back = send_back[::-1]
        export = ' '.join(str(x) for x in send_back)
        print(export)
        return(export)
number_pattern(4)