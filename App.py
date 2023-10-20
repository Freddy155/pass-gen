import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;:'\"<>,.?/"

def generate_password():
    password_length = int(input("Enter the desired password length: "))
    all_characters = uppercase_letters + lowercase_letters + numbers + special_characters
    password = "".join(random.choice(all_characters) for _ in range(password_length))
    return password

if __name__ == "__main__":
    generated_password = generate_password()
    print("Generated Password: ", generated_password)
