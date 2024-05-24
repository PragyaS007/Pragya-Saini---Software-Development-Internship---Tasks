import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            # Prompt the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the guess to the secret number and provide feedback
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    guessing_game()
