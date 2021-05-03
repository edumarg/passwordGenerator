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


if __name__ == '__main__':
    print("Password Generator")
    print("==================")
    number_of_passwords = int(input("Number of password you will like to generate? \n>>"))
    password_length = int(input("Password length?\n>>"))
    passwords = generate_passwords(number_of_passwords, password_length)
    for password in passwords:
        print(password)
