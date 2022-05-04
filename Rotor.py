def decodeWiring(encoding):

    charWiring = list(encoding)
    wiring = [None] * len(charWiring)
    for x in wiring:
        wiring[x] = charWiring[x] - 65
    return wiring


def __init__(self, name, encoding, rotorPOS, notchPOS, ringSetting):

    self.name = name
    #self.forwardWiring[] =
    #self.backwardWiring[] =
    self.rotorPOS = rotorPOS
    self.notchPOS = notchPOS
    self.ringSetting = ringSetting