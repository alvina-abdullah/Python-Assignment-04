def main():
    
    side1 = float(input("Enter the Length of side 1: "))
    side2 = float(input("Enter the Length of side 2: "))
    side3 = float(input("Enter the Length of side 3: "))

    perimeter = side1 + side2 + side3
    print(f"The perimeter of the triangle is {perimeter}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()