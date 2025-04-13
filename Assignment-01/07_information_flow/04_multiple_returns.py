# Function to get user data
def get_user_data():
    first_name = input("What is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()
    email = input("What is your email address?: ").strip()
    
    return first_name, last_name, email  # Returning a tuple

def main():
    # Call the function and store the returned tuple
    user_data = get_user_data()
    
    # Display the collected data
    print("Received the following user data:", user_data)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()