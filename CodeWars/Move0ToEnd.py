import time
def move_zeros(lst):
    def add_zero(zeros):
        time.sleep(.001)
        while zeros > 0:
            lst.append(0)
            print(lst)
            zeros -= 1
    print(lst)
    zero_counter = 0
    running = True
    while running:
        if 0 in lst:
            lst.remove(0)
            zero_counter += 1
            print(zero_counter)
            print(lst)
        elif 0 not in lst:
            add_zero(zero_counter)
            running = False
    return lst

move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])