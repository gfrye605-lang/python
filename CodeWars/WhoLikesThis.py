def likes(names):
    try:
        print(names[0])
    except IndexError:
        return("no one likes this")
    string = ""
    # Get the first two names
    if len(names) >= 4:
        name1 = names[0]
        name2 = names[1]
        string = f"{name1}, {name2}"
        string += f" and {len(names)-2} others like this"
        return string
    else:
        if len(names) == 1:
            string += str(names[0]) + " likes this"
        elif len(names) == 2:
            string += names[0]+ " and "+ names[1]+ " like this"
        elif len(names) == 3:
            string += str(names[0])+", "+ str(names[1])+ " and "+ str(names[2])+ " like this"
    return string