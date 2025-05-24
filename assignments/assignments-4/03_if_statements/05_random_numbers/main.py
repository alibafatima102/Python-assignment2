import random

def main():
    for _ in range(10):
        number = random.randint(1, 100)
        print(number, end=' ')
    print()  # for newline after printing all numbers

if __name__ == "__main__":
    main()
