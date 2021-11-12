import random
number = random.randint(0,9)
chances = 0
print("Number guessing game")

while chances < 5:
    guess = int(input("Enter your guess: ")) 
    print(guess)
    if guess == number:
        print("Congratulations! You win")
        break
    elif guess < number:
        print("Your guess was too low: Enter a no. higher than ",guess)
    else :
        print("Your guess was too high: Enter a no. lower than ",guess)
    chances=chances+1

if not chances < 5:
    print("Sorry! You lost")    