# Function to check the stock of a given fruit
def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "orange": 250,
        "mango": 700
    }
    return inventory.get(fruit.lower(), 0)  # Return stock count or 0 if not found

def main():
    # Prompt the user for input
    fruit = input("Enter a fruit: ").strip()

    # Get the number of fruit in stock
    stock = num_in_stock(fruit)

    # Print appropriate message based on stock availability
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()