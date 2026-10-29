import time
import os

# Vars
word = ""
won = False
running = False
current_phase = 0
i_guess = ""
phases = [""" 
____
|/   |
|   
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____
"""]

# Utilities
def update_scrn():
    global running
    global won
    if current_g == word:
        won = True
    try:   
        os.system('cls' if os.name == 'nt' else 'clear')
        print(phases[current_phase])
        print(f"WORD: {current_g}        Guesses: {i_guess}       \n")
    except IndexError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You lose!")
        running = False

def correct_guess(g):
    global current_g
    i = 0
    for i, letter in enumerate(word):
        if letter == g:
            cg_list = list(current_g)
            cg_list[i] = g
            current_g = "".join(cg_list)
            update_scrn()       

def incorrect_guess(g):
    global current_phase
    global i_guess
    current_phase += 1
    if len(i_guess) == 0:
        i_guess = g
    else:
        i_guess += ", "+g
    update_scrn()

# Intro
print("Welcome to Hangman!")
time.sleep(2)
word = input("Enter your word: ")
current_g = "#" * len(word)
print("Word received, beginning game!")
time.sleep(2)
update_scrn()

# Game Logic
running = True
while running:
    if won == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You won! The word was", word)
        break
    guess = input("Guess a letter: ")
    if len(guess) > 1 or len(guess) == 0:
        print("Must be a one letter response!")
        continue
    if guess not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("Reponse must be a letter!")
        continue
    if guess in current_g or guess in i_guess:
        print("You already guessed that!")
        continue
    elif guess in word:
        correct_guess(guess)
    elif guess not in word:
        incorrect_guess(guess)
    
