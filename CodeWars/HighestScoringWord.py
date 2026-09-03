def high(x):
    letter_scores = {" ": 0}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Assign letter scores
    for i, letter in enumerate(alphabet, 1):
        letter_scores[letter] = i
        i += 1
    
    # Seperate letters into list
    letters = x.split()
    print(letters)
    
    # Loop through list and calculate the value and each letter & word, adding them to its score, then adding them to a dict
    current_score = 0
    word_scores = {}
    for word in letters:
        for letter in word:
            current_score += letter_scores.get(letter)
        else:
            word_scores[word] = current_score
            current_score = 0
    print("wordscores: ",word_scores)
    
    highest_key = max(word_scores, key=word_scores.get)

    return(highest_key)
        
    
    
        