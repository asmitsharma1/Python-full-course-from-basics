import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Prompt user to guess the number
user_guess = int(input("Guess the number between 1 and 10: "))

# Provide feedback based on the guess
if user_guess == random_number:
    print("Congratulations! Your guess is correct.")
else:
    print(f"Sorry, the number was {random_number}. Try again!")
