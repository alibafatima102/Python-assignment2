import random

DONE_LIKELIHOOD = 0.3  # You can adjust this to change stopping chance

def done():
    """Randomly returns True with likelihood DONE_LIKELIHOOD."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # Stop counting immediately
        print(i, end=' ')
    # If loop completes, just return naturally

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()
