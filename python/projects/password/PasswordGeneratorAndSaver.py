import random


class Password():
    def PasswordGenerate():
        # maximum length of password needed
        # this can be changed to suit your password length
        MAX_LEN = 12

        # Represented as chars to enable easy string concatenation
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOWCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                              'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                              'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                              'z']

        UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                'Z']

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                   '*', '(', ')', '<']
        COMBINED_LIST = DIGITS + UPPERCASE_CHARACTERS + LOWCASE_CHARACTERS + SYMBOLS

        # randomly select at least one character from each character set above
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPPERCASE_CHARACTERS)
        rand_lower = random.choice(LOWCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)

        # combine the character randomly selected above
        # at this stage, the password contains only 4 characters but
        # we want a 12-character password
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

        for x in range(MAX_LEN):
            password = random.choice(COMBINED_LIST)
            print(password, end="")

        choice1 = input("\ndo you want to save this password(y/n): ")
        choice1 = choice1.lower()
        if choice1 == "y":
            choice2 = input("which account password is this")
            with open("password.txt", "a") as f:
                f.write(f"account : {choice2} | password:{password}\n")
        elif choice1 == "n":
            print("okk we will not save your password")
        else:
            print("invalid choice")

    def PasswordSave():
        account = input(f"{name} which account password you want to save :")
        password = input(f"what is the password: ")
        with open("password.txt", "a") as f:
            f.write(f"account : {account} | password:{password}\n")


name = input("enter your name: ")
choice = input(
    f"ok {name} do you want to a generate (g)new password or save a new password(s): ")
choice = str(choice)
choice = choice.lower()
if choice == "g":
    Password.PasswordGenerate()
elif choice == "s":
    Password.PasswordSave()
else:
    print("invalid choice")
