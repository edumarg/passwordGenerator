import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+-=/?.,"


def generate_passwords(ammount, length):
    passwords = []
    while ammount > 0:
        password = ""
        number = length
        while number > 0:
            char = random.choice(chars)
            password = password + char
            number -= 1
        passwords.append(password)
        ammount -= 1
    return passwords


def set_number_of_passwords():
    while True:
        try:
            number = int(input("Number of password you will like to generate? \n>>"))
            if number > 20 or not number > 1:
                raise ValueError
            return number
            break
        except ValueError:
            print("Please enter a valid number between 1-20")


def set_password_length():
    while True:
        try:
            length = int(input("Password length?\n>>"))
            if length > 26 or not length >= 6:
                raise ValueError
            return length
            break
        except ValueError:
            print("Please enter a valid number between 6 and 26")


if __name__ == '__main__':
    print("Password Generator")
    print("==================")
    number_of_passwords = set_number_of_passwords()
    print(number_of_passwords)
    # password_length = int(input("Password length?\n>>"))
    password_length = set_password_length()
    print(" ")
    print("Your passwords:")
    print("===============")
    passwords = generate_passwords(number_of_passwords, password_length)
    for password in passwords:
        print(f'Password #{passwords.index(password) + 1 }: {password}')
