def main():
    lst = []  # Empty list to store user inputs
    
    while True:
        value = input("Enter a value: ")  # Taking input from user
        
        if value == "":  # If user presses enter without typing anything, exit loop
            break
        
        lst.append(value)  # Adding value to the list

    print("Here's the list:", lst)  # Printing the final list
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()