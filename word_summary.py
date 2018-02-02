sentence = (input("please enter a sentence: ").lower())
sentence_histogram = {}

for word in range(0, len(sentence)): 
    if sentence[word] in sentence_histogram:
        sentence_histogram[sentence_histogram[word]] += 1
    else:
        sentence_histogram[sentence[word]] = 1

print (sentence_histogram)