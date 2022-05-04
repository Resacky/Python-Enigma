def decodeWiring(encoding):
    return [x - 65 for x in list(encoding)]


def __init__(self, name, encoding, rotorPOS, notchPOS, ringSetting):

    self.name = name
    #self.forwardWiring[] =
    #self.backwardWiring[] =
    self.rotorPOS = rotorPOS
    self.notchPOS = notchPOS
    self.ringSetting = ringSetting