"""
Rotor class for Enigma Machine

"""

class Rotor:
    """Basic Rotor class for Enigma Machine"""
    rotorNum = 0

    def __init__(self, configuration):
        self.config = configuration
        self.POSITION = 0
        Rotor.rotorNum += 1
        
    def rotate(self):
        #Increments the current Rotor position
        if len(self.config) > 1:
            self.POSITION += 1
        else:
            print "the rotor is not large enough to rotate"
            pass
        
    def setStart(self, position):
        #Takes starting position from 0 to n on the Rotor
        self.POSITION = position 
    
