def generate_passwords(ammount, length):
    print(ammount, length)


if __name__ == '__main__':
    print("Password Generator")
    print("==================")
    number_of_passwords = int(input("Number of password you will like to generate? \n>>"))
    password_length = int(input("Password length?\n>>"))
    generate_passwords(number_of_passwords, password_length)
