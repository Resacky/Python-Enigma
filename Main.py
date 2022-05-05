import Keyboard
import Plugboard
import Rotor


def rotorConfig():
    rotorName = input("Config for first rotor?\n")
    rotorPOS = input("Rotor's position\n")
    rotorSetting = input("Rotor's ring setting\n")
    return Rotor.CreateRotor(rotorName, rotorPOS, rotorSetting)


def menu():
    print("Welcome to my version of the Enigma machine via Python 1.0")

    # Plugboard config
    Plugboard.plugConfig()

    # Rotor config
    rotor1 = rotorConfig()
    rotor2 = rotorConfig()
    rotor3 = rotorConfig()

    while True:

        message = input("Please write your message: \n").upper()

        # here goes code to actually encrypt

        menuInput = input(
            "Would you like to encrypt another message with the same configuration or change the config?\n").upper()

        if menuInput == "EXIT":
            break
        elif menuInput == "CHANGE CONFIG":
            menu()


menu()
