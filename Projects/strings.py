# Tests out various string methods
string1 = "I love cats!"

print(string1[::-1])
print(string1.split())
print(len(string1))
print(string1.find("o"))


# Finds the first and last e in the entered sentence
lala = input("Enter a sentence. ")

first = lala.find("e")
last = lala.rfind("e")

first = str(first)
last = str(last)

print(first + "-" + last)


# Finds & displays the third, third to last, and fourth character of an input
lala = input("Input a word. ")

third = lala[2]
third_to_last = lala[-3]
fourth = lala[3]

print(third + third_to_last + fourth)