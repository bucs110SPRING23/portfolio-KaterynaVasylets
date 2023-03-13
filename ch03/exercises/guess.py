import random
number = random.randint (1,10)
chances = 3
for i in range (chances):
    guess = input("Guess a number between 1 and 10")
    guess = int(guess)
    if guess == (number):
        print("yes")
        break
    elif (guess > number):
        print ("too much")
    elif (guess < number):
        print ("too low, try again")
     
