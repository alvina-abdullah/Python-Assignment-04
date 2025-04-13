def double(num):
    return num * 2

def main():
    num = int(input("Enter a number:"))
    result = double(num)
    print(f"Double that is {result}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()