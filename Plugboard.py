import Keyboard

plugboard = []

while True:

    userInput = input("What two characters would you like to swap\n").upper()

    if len(userInput) > 2:
        print("Error found, need to input a MAX of two characters")
        continue
    elif len(userInput) < 2:
        print("Error found, need to input a MIN of two characters")
        continue

    char1 = ord(userInput[0]) - 65
    char2 = ord(userInput[1]) - 65

    #if statement to check if the keys are swapped:

    temp = char1
    char1 = char2
    char2 = temp

    print(char1)
    print(char2)
