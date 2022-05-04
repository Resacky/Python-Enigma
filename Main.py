import Keyboard


def menu():
    print("Welcome to my version of the Enigma machine via Python 1.0")

    # Here is code to modify the configuration

    while True:

        message = input("Please write your message: \n").upper()

        # here goes code to actually encrypt

        menuInput = input(
            "Would you like to encrypt another message with the same configuration or change the config?\n")

        if menuInput == "EXIT":
            break
        elif menuInput == "CHANGE CONFIG":
            menu()


menu()
