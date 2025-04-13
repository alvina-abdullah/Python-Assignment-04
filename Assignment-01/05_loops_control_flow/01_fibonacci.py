def main():
    Max_value = 10000  # Constant value

    # Starting values of Fibonacci sequence
    a, b = 0, 1
    
    # Print Fibonacci numbers until we reach MAX_VALUE
    while a < Max_value:
        print(a, end=" ")  # Print number with space
        a, b = b, a + b  

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()