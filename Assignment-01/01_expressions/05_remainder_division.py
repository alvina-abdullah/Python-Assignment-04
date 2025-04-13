def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter a number to be divided: "))
    divisor: int = int(input("Please enter a number to divide by: "))

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (module)
    
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
