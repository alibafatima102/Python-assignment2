def main():
    affirmation = "I am capable of doing anything I put my mind to."

    print("Please type the following affirmation:")
    while True:
        user_input = input()
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation. Please type the following affirmation:")

# Required to run the program
if __name__ == "__main__":
    main()
