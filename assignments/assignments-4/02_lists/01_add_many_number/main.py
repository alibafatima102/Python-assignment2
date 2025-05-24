def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    
    Args:
    numbers (list[int]): A list of integers.

    Returns:
    int: The sum of the integers in the list.
    """
    total_so_far = 0
    for number in numbers:
        total_so_far += number
    return total_so_far


def main():
    numbers = [1, 2, 3, 4, 5]  # Example list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Compute the sum
    print(sum_of_numbers)  # Output the result


if __name__ == "__main__":
    main()
