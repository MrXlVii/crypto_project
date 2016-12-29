class Rotor(object):
    """Basic Rotor class for Enigma Machine"""

    def __init__(self, data):
        self.data = data
        self.POSITION = 0   #current position on Rotor
        self.current = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, current):
        self._current = self.data[self.POSITION]

    @property
    def POSITION(self):
        return self._POSITION

    @POSITION.setter
    def POSITION(self, POSITION):
        if POSITION >= len(self.data):
            POSITION = POSITION % len(self.data)
            self._POSITION = POSITION
            self._current = self.data[self.POSITION]
        elif POSITION < 0:
            POSITION = len(self.data)-1
            self._POSITION = POSITION
            self._current = self.data[self.POSITION]

        else:
            self._POSITION = POSITION
            self._current = self.data[self.POSITION]
    
    def rotate(self, logic):
        if logic is True:
            if len(self.data) != None:
                self.POSITION += 1
            else:
                print "There is no Rotor object to rotate"
        elif logic is False:
            if len(self.data) != None:
                self.POSITION -=1
            else:
               print "There is no Rotor object to rotate"
        else:
            print "We don't know which way to turn"
            #TODO: Throw exception   
        
#---------------------------------------------------------------------------------------------

class Core(object):
    
    def __init__(self, first, second, third):
        self.r1 = first
        self.r2 = second
        self.r3 = third

    def config(self, first, second, third, p1, p2, p3):
        #sets the current rotor configuration and positions of each respective rotor
        
        self.r1 = first
        self.r2 = second
        self.r3 = third
        
        self.r1.POSITION = p1
        self.r2.POSITION = p2
        self.r3.POSITION = p3
        
    def encrypt(self, plain):
        #TODO: work out the modulo math

        cipher = list(plain)

        for i in range(len(cipher)):
            cipher[i] = ord(cipher[i])

            if cipher[i] is 32:
                cipher[i] = chr(cipher[i])
                self.iterate(True)

            elif cipher[i] > 64 and cipher[i] < 91:
                temp = (cipher[i] + ord(self.r1.current) + ord(self.r2.current) + ord(self.r3.current)) % 65
                temp += 65
		        #flag here for potential math error
                if temp >= 91:
                    temp -= 90
                    temp += 64
                    cipher[i] = chr(temp)
                else:
                    cipher[i] = chr(temp)

                self.iterate(True)

            elif cipher[i] > 96 and cipher[i] < 123:
                temp = (cipher[i] + ord(self.r1.current) + ord(self.r2.current) + ord(self.r3.current)) % 97
                temp += 97
                #flag for potential math error
                if temp >= 123:
                    temp -= 122
                    temp += 96
                    cipher[i] = chr(temp)
                else:
                    cipher[i] = chr(temp)

                self.iterate(True)

            else:
                cipher[i] = chr(cipher[i])
                self.iterate(True)

        output = ''.join(cipher)
        return output
        
    def decrypt(self, cipher):
        #TODO: work out the modulo math
        
        plain = list(cipher)
        
        for i in range(len(plain)):
            plain[i] = ord(plain[i])

        if plain[i] is 32:
            plain[i] = chr(plain[i])
            self.iterate(False)

        elif plain[i] > 64 and plain[i] < 91:
            temp = (plain[i] - ord(self.r1.current) - ord(self.r2.current) - ord(self.r3.current)) % 65
            temp += 65
            #Flagged for potential modulo error
            if temp <= 64:
                temp += 26
                plain[i] = chr(temp)
            else:
                plain[i] = chr(temp)

            self.iterate(False)
        elif plain[i] > 96 and plain[i] < 123:
            temp = (plain[i] - ord(self.r1.current) - ord(self.r2.current) - ord(self.r3.current)) % 97
            temp += 97
            #Flagged for potential modulo error
            if temp <= 96:
                temp += 26
                plain[i] = chr(temp)
            else:
                plain[i] = chr(temp)
            self.iterate(False)

        else:
            plain[i] = chr(plain[i])
            self.iterate(False)

        output= ''.join(plain)
        return output
    
    def iterate(self, logic):
        self.r3.rotate(logic)
        if self.r3.POSITION == 0:
            self.r2.rotate(logic)
            if self.r2.POSITION == 0:
                self.r1.rotate(logic)

#-------------------------------------------------------------------------------------------

"""
This is initialization for the rotor objects

This is the letter arrange from the 1930 Enigma I

"""

R1 = Rotor(['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'])
R2 = Rotor(['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'])
R3 = Rotor(['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']) 	

#-------------------------------------------------------------------------------------------
def main():
    #TODO: write main method
    pass


if __name__ == "__main___":
    main()
