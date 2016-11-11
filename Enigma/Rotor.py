"""
Rotor class for Enigma Machine

"""

class Rotor
    'Basic Rotor class for Enigma Machine'
    rotorNum = 0

    def __init__(self, config):
        self.config = config
        self.POSITION = 0
        Rotor.rotorNum += 1
        
    def rotate(self):
        'Increments the current Rotor position'
        self.POSITION += 1
        
    def setStart(self, position):
        'Takes starting position from 0 to n on the Rotor'
        self.POSITION = position
        
    def displayPosition(self):
        'returns the value at current Rotor position'
        return self.config[self.POSITION] 
    
