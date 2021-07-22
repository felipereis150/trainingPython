import random

print("Welcome to the guessing game!")

secret_number = random.randint(1,99)
total_attempts = 3
remaining_attempts = total_attempts
print(secret_number)

while(remaining_attempts >0):
    print("Attempt", remaining_attempts, "of", total_attempts)
    guess = int(input("Try to guess the number in a range of 1 to 99: "))
    print ("you entered the number", guess)

    guessed = guess == secret_number
    bigger = guess < secret_number
    smaller = guess > secret_number

    if(guessed):
        print("Correct! You guessed the number")
    elif(bigger):
        print("try a bigger number")
    else:
        smaller
    remaining_attempts -= 1
    print(total_attempts)
print("Game Over")