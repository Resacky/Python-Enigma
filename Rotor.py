import Keyboard

#add remaining methods

name = ''
forwardWiring = ''
backwardWiring = ''
rotorPOS = ''
notchPOS = ''
ringSetting = ''


def reset():
    rotorPOS = 0


# This method is to create the individual rotors with already pre-generated configurations
def CreateRotor(name, rotorPOS, ringSetting):
    name = name.upper()

    if name == "I":
        return __init__(name, "EKMFLGDQVZNTOWYHXUSPAIBRCJ", rotorPOS, 16, ringSetting)
    elif name == "II":
        return __init__(name, "AJDKSIRUXBLHWTMCQGZNPYFVOE", rotorPOS, 4, ringSetting)
    elif name == "III":
        return __init__(name, "BDFHJLCPRTXVZNYEIWGAKMUSQO", rotorPOS, 21, ringSetting)
    elif name == "IV":
        return __init__(name, "ESOVPZJAYQUIRHXLNFTGKDCMWB", rotorPOS, 9, ringSetting)
    elif name == "V":
        return __init__(name, "VZBRGITYUPSDNHLXAWMJQOFECK", rotorPOS, 25, ringSetting)
    elif name == "VI":
        return __init__(name, "JPGVOUMFYQBENHZRDKASXLICTW", rotorPOS, 0, ringSetting)

        @override
        def isAtNotch(self):
            return self.rotorPOS == 12 or self.rotorPOS == 25

    elif name == "VII":
        return __init__(name, "NZJHGRCXMYSWBOUFAIVLPEKQDT", rotorPOS, 0, ringSetting)

        @override
        def isAtNotch(self):
            return self.rotorPOS == 12 or self.rotorPOS == 25

    elif name == "VIII":
        return __init__(name, "FKQHTLXOCBJSPDZRAMEWNIUYGV", rotorPOS, 0, ringSetting)

        @override
        def isAtNotch(self):
            return self.rotorPOS == 12 or self.rotorPOS == 25

    else:
        return __init__("Identity", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", rotorPOS, 0, ringSetting)


def decodeWiring(encoding):
    return [x - 65 for x in list(encoding)]


def inverseWiring(primaryWiring):
    inverse = [None] * len(primaryWiring)
    i = 0
    for x in primaryWiring:
        inverse[x] = i
        i += 1
    return inverse


def __init__(self, name, encoding, rotorPOS, notchPOS, ringSetting):
    self.name = name
    self.forwardWiring = decodeWiring(encoding)
    self.backwardWiring = inverseWiring(self.forwardWiring)
    self.rotorPOS = rotorPOS
    self.notchPOS = notchPOS
    self.ringSetting = ringSetting
