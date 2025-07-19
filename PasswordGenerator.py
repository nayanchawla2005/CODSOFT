import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for better security."

    # Combine character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

# Run the program
main()
