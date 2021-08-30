import random

print("Welcome to the guessing game!")

secret_number = random.randint(1,99)
round = 1
attempts = 3
print(secret_number)

for round in range(1, attempts + 1):
    print("Attempt {} of {}".format(round, attempts))
    guess = int(input("Try to guess the number in a range of 1 to 99: "))
    print ("you entered the number", guess)

    guessed = guess == secret_number
    bigger = guess < secret_number
    smaller = guess > secret_number

    if(guessed):
        print("Correct! You guessed the number")
        break
    elif(bigger):
        print("try a bigger number")
    else:
        print("try a smaller number")
    round += 1
print("Game Over")