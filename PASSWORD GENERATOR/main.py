#  User Input: Prompt the user to specify the desired length of the password.
#  Generate Password: Use a combination of random characters to generate a password of the specified length.
#  Display the Password: Print the generated password on the screen #

import random

def get_password_length():
    while True:
        try:
            length = int(input("Enter the length of the password you require: "))
            if length <= 0:
                print("Password length cannot be zero or negative! Please try again.")
            else:
                return length
        except ValueError:
            print("Please input numeric value only!")

def generate_password(length):
    key_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*_-"
    password_string = ''
    for _ in range(length):
        password_string += random.choice(key_string)
    return password_string

if __name__ == "__main__":
    password_length = get_password_length()
    password = generate_password(password_length)
    print("Your Password:", password)
    