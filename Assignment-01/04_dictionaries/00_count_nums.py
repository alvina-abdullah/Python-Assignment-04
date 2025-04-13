def main():
    # Dictionary to store the count of numbers
    num_counts = {}

    while True:
        user_input = input("\n Enter a number (or press Enter to stop):")      
        
        # Stop input if user presses Enter without typing anything
        if user_input == "":
            break
        
        # Convert input to an integer
        number = int(user_input)
        
        # Increase count in dictionary
        if number in num_counts:
            num_counts[number] += 1
        else:
            num_counts[number] = 1

    # Print the count of each number
    print("\nNumber occurrences:")
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()