# Write a letter_histogram program that asks the user for input,
# and prints a dictionary containing the tally of how many times
# each letter in the alphabet was used in the word. For example:

# $ python letter_histogram.py
# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

word= (input("Please enter a word: ").lower())

letter_histogram = {}

for letter in range(0, len(word)):
    if word[letter] in letter_histogram:
        letter_histogram[word[letter]] += 1
    else:
        letter_histogram[word[letter]] = 1

print (letter_histogram)
