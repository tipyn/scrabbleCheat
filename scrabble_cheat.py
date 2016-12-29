# Import any modules needed

import sys

# Score dictionary

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


# Open sowpods.txt words file, make a list and get rid of line break

f = open("sowpods.txt", "r")

words = []

for line in f:
    line = line.strip()
    words.append(line)

f.close()


# Scrabble rack

test line

# In case user forgets to supply a Scrabble rack 


# Find all words from the word file that are made of letters from the Scrabble rack


# Score the words that the above code finds
