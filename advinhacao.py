import random

print("Bem vindo jogo de advinhação")

secret_number = random.randint(1,99)
print(secret_number)

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

print("Game over. Run the program to play again")