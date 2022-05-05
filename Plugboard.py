import Keyboard

# Python is weird where in order to create a list with x amount of size, you need to give it "some"
# value

plugboard = [None] * len(Keyboard.keys)


def plug(charMessage):
    result = indexASCII(charMessage)
    result = plugboard[result]
    return result


def isKeySwapped(key):
    if plugboard[key] == Keyboard.keys[key]:
        return False
    else:
        return True


def indexASCII(charASCII):
    for x in range(len(Keyboard.keys)):
        if charASCII == Keyboard.keys[x]:
            return x


def printPlug():
    for x in plugboard:
        print(chr(x), end=" ")
    print("\n")


def plugConfig():

    # Once the list of plugboard is created with 26 elements of 'none', we are iterating within each index and adding 'x'
    # which is the iteration and then adding '65' to it to place it to the corresponding ASCII of captial letters.
    for x in range(len(Keyboard.keys)):
        plugboard[x] = x + 65
        print(chr(plugboard[x]), end=" ")
    print("\n")

    while True:

        userInput = input("What two characters would you like to swap?\n").upper()

        if len(userInput) > 2:
            print("Error found, need to input a MAX of two characters")
            continue
        elif len(userInput) < 2:
            print("Error found, need to input a MIN of two characters")
            continue

        # This section of code here is grabbing the first and second letter of the users input of the 2 letters they want
        # to swap, and subtracting '65' to grab the correct index location of the 'keyboard' list.
        char1 = ord(userInput[0]) - 65
        char2 = ord(userInput[1]) - 65

        if isKeySwapped(char1) or isKeySwapped(char2):
            print("Error found. One of the two keys are already swapped and unable to swap again")
            continue

        temp = plugboard[char1]
        plugboard[char1] = plugboard[char2]
        plugboard[char2] = temp

        while True:

            menuInput = input("Would you like to swap more characters? (Y/N)\n").upper()

            if menuInput == "Y":
                break
            elif menuInput == "N":
                printPlug()
                return
            else:
                print("Sorry invalid input. Please provide proper input.")
                continue
