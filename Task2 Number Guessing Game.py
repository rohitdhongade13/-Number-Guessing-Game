import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")
    a=input("Please Enter Your Good Name\n")
    print("Hello",a)

    secret_number = random.randint(1, 100)
    attempts = 0
   

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number ({secret_number}) in {attempts} attempts.")
            break

def main():
    guessing_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()

    while play_again == 'yes':
        guessing_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()

    print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()
