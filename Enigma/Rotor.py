"""
Rotor class for Enigma Machine

functions as Node in doubly linked list

"""

class Rotor:
    """Basic Rotor class for Enigma Machine"""
    rotorNum = 0

    def __init__(self, data, prev, next):
        self.data = data    #the contents of each rotor
        self.next = next    #the next Rotor in sequence
        self.prev = prev    #previous Rotor in sequence--for decryption
        self.POSITION = 0   #current position on Rotor
        Rotor.rotorNum += 1 #TODO: fix this bug
        
    def rotate(self):
        #Increments the current Rotor position. All calls to "data" are data[POSITION]
        if len(self.config) > 1:
            self.POSITION += 1
            
        else:
            print "the rotor is not large enough to rotate"
            pass
        
    def setStart(self, position):
        #Takes starting position from 0 to n on the Rotor
        self.POSITION = position 

