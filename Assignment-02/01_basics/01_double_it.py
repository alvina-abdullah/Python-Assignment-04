
def main():

    curr_value = int(input("Enter a number: "))  
    
    while curr_value < 1000:
        curr_value = curr_value * 2  # Value ka double karna
        print(curr_value, end=" ")  # Print in one line

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()