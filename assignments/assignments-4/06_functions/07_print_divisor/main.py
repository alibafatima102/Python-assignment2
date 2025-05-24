def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

def main():
    user_input = input("Enter a number: ")
    try:
        num = int(user_input)
        print_divisors(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == '__main__':
    main()
