import sys

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
          "X": 8, "Z": 10}

# Get the Scrabble rack from the command line.
if len(sys.argv) < 2:
    print("please supply a rack.")
    exit(1)

rack = sys.argv[1]
print "test1"
# Turn the words in the sowpods.txt file into a Python list.
wordlist = []
print "test2"
try:
    with open("sowpods.txt", "r") as f:
        for line in f:
            wordlist.append(line.strip())

except EnvironmentError:
    print("can't find sowpods.txt.")
    exit(1)
    print "test4"

# Find all of the valid words that can be made with the letters in the rack.
valid_words = []
print "test5"
for word in wordlist:
    candidate = True
    rack_letters = list(rack)
    
    for letter in word:
        if letter not in rack_letters:
            candidate = False
            
            break # stop checking
        else:
            rack_letters.remove(letter)
    if candidate == True:
        print "test8"
        # get scores
        total = 0
        print "test9"
        for letter in word:
            total = total + scores[letter]
        valid_words.append([total, word])
        print "test10"

# Print the valid words, sorted by Scrabble score.
valid_words.sort()
print "test11"
for entry in valid_words:
    print "test12"
    score = entry[0]
    word = entry[1]
    print(str(score) + " " + word)
    print "test13"
