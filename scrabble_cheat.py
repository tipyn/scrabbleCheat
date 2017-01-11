# Import sys module so we can run the script from the CLI

import sys

# Score dictionary

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


# Open sowpods.txt words file, make a list and get rid of line break

#f = open("sowpods.txt", "r")

#words = []

#for line in f:
#	line = line.strip()
#	words.append(line)

#f.close()

#print("is this working? line 26")

# Using a with statement instead

words = []

with open('sowpods.txt', 'r') as f:
	for line in f: 
		words.append(line.strip())

# Scrabble rack

scrabbleRack = sys.argv[1] 

print("is this working? line 41")

# In case user forgets to supply a Scrabble rack 

if len(scrabbleRack) < 2:
	print("Please provide at least two letters from your Scrabble rack")
	exit(1)

print(words)
print("is this working? line 49")
# Find all words from the word file that are made of letters from the Scrabble rack

rack_words = []
print("is this working? line 53")
for word in words:
	print("is this working? line 58")
	candidate = True
	letters = list(scrabbleRack)
	for letter in word:
		if letter not in letters:
			candidate = False 
			break
		else: 
			letters.remove(letter)
		if candidate == True:
		# Score the words that the above code finds
			total = 0
		for letter in word:
			total = total + scores[letter]
		rack_words.append([total, word])

		print("is this working? line 71")

# Print the words found and sort by score

rack_words.sort()

for entry in rack_words:
	score = entry[0]
	word = entry[1]
	print(str(score) + " " + word)

	print("is this working? line 82")
