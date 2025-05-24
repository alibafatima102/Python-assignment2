import random

def main():
    # Generate a random number between 0 and 99
    number_to_guess = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess > number_to_guess:
            print("Your guess is too high")
        elif guess < number_to_guess:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break

# Required to run the main() function
if __name__ == "__main__":
    main()
