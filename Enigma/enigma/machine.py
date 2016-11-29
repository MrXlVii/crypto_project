class Rotor(object):
    """Basic Rotor class for Enigma Machine"""
    rotorNum = 0

    def __init__(self, data):
        self.POSITION = 0   #current position on Rotor
        
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
        
        
#---------------------------------------------------------------------------------------------

def class Core(object):

    def config(self, first, second, third, p1, p2, p3):
        #TODO: plan optimum way to parse the rotor config
        pass
        
    def encrypt(self, plain):
        #TODO: implement
        pass
    
    def decrypt(self, cipher):
        #TODO: implement
        pass
    


#-------------------------------------------------------------------------------------------

"""
This is initialization for the rotor objects

This is the letter arrange from the 1930 Enigma I

"""

R1 = Rotor([E, K, M, F, L, G, D, Q, V, Z, N, T, O, W, Y, H, X, U, S, P, A, I, B, R, C, J])
R2 = Rotor([A, J, D, K, S, I, R, U, X, B, L, H, W, T, M, C, Q, G, Z, N, P, Y, F, V, O, E])
R3 = Rotor([B, D, F, H, J, L, C, P, R, T, X, V, Z, N, Y, E, I, W, G, A, K, M, U, S, Q, O]) 	

#-------------------------------------------------------------------------------------------
def main():
    pass


if __name__ == "__main___":
    main()
ssag
