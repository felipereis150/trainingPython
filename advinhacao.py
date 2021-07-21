import random

print("Bem vindo jogo de advinhação")

secret_number = random.randint(1,99)

guess = int(input("Try to guess the number in a range of 1 to 99: "))
print ("you entered the number", guess)

if guess == secret_number:
    print("Correct! You guesse the number")
elif guess < secret_number:
    print("try a small number")
else:
    print("try a greater number")

print("Game over. Run the program to play again")