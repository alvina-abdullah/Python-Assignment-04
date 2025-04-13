import random

IN_NUMBERS: int = 10  # Generate 10 numbers
MIN_VALUE: int = 1    # Minimum value 1
MAX_VALUE: int = 100  # Maximum value 100

def main():
    #Generate 10 random numbers in one line
    for _ in range(IN_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

    print()  # Newline for better formatting

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()