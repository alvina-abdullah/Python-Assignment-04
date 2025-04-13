import random  # Random module 

def main():
 
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print(*random_numbers)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()