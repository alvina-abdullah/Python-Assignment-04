def main():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even")
        else:
            print(f"{num} odd")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()