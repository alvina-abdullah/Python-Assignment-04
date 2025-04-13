Max_length = 3  # Define the maximum allowed length

def shorten(lst):
    while len(lst) > Max_length:
        removed_item = lst.pop()  # Last element remove
        print("Removed:", removed_item)  #print element

def main():
    lst = []  #
    
    # list input 
    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)

    print("Original list:", lst)  # 1 list print
    shorten(lst)  #Call shorten function 
    print("Shortened list:", lst)  # Final list printed

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()