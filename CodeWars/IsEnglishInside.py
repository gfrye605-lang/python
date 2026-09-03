def sp_eng(sentence): 
    word = "english"
    if word.casefold() in sentence.casefold():
        return True
    else:
        return False

print(sp_eng("5345englis"))
