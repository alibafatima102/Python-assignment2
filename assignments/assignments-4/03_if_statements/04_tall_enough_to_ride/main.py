def main():
    MIN_HEIGHT = 50
    while True:
        height_str = input("How tall are you? ")
        if height_str == "":
            print("Goodbye!")
            break
        height = int(height_str)
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()
