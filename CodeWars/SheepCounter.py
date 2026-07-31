sheep = [True,  True,  True,  False,
        True,  True,  True,  True ,
        True,  False, True,  False,
        True,  False, False, True ,
        True,  True,  True,  True ,
        False, False, True,  True ]

def count_sheeps(sheep):
    running = True
  # May the force be with you
    while running:
        c = sheep.count(True)
        running = False
        print(c)
    return(c)

count_sheeps(sheep)