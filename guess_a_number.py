import random
random_number = random.randint(1, 10)
print (random_number)
guess_count = 0
while guess_count < 6:
    guess = (int(input("I am thinking of a number between 1 and 10. What's your guess?: ")))
    guess_count += 1
    if random_number == guess:
        print ('you got it right')
        x = False
    elif random_number > guess: 
        print ("I'm thinking of a larger number")
    elif random_number < guess:
        print ("I'm thinking of a smaller number")