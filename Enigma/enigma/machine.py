class Rotor(object):
    """Basic Rotor class for Enigma Machine"""

    def __init__(self, data):
        self.data = data
        self.POSITION = 0   #current position on Rotor

#HAVENT RUN TESTS ON NEW PROPERTY ADDITIONS

    @property
    def current(self):
        return self.current

    @current.setter
    def current(self, position):
        self.current = self.data[self.POSITION] 
        
    def rotate(self):
        if len(self.data) > 1:
            self.POSITION += 1
            
        else:
            print "the rotor is not large enough to rotate"
            pass
        
    def setStart(self, position):
        #Takes starting position from 0 to n on the Rotor
        #TODO: figure out why self.current isn't updating with updated position
        self.POSITION = position
        self.current = 
        
        
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
        
        self.r1.setStart(p1)
        self.r2.setStart(p2)
        self.r3.setStart(p3)
        
    def encrypt(self, plain):
        #TODO: make the nth rotor rotor modulo the n+1th
        #TODO: work out the modulo math

        cipher = list(plain)
                
        for i in range(len(cipher)):
            cipher[i] = ord(cipher[i])

            if cipher[i] is 32:
		        cipher[i] = chr(cipher[i])
            elif cipher[i] > 64 and cipher[i] < 91:
                temp = (cipher[i] + ord(r1.current) + ord(r2.current) + ord(r3.current)) % 64 
		        #flag here for potential math error
                if temp >= 91:
                    temp -= 90
                    temp += 64
                    cipher[i] = chr(temp)
                else:
                    cipher[i] = chr(temp)

            elif cipher[i] > 96 and cipher[i] < 123:
                temp = (cipher[i] + ord(r1.current) + ord(r2.current) + ord(r3.current)) % 96
                #flag for potential math error
                if temp >= 123:
                    temp -= 122
                    temp += 96
                    cipher[i] = chr(temp)
                else:
                    cipher[i] = chr(temp)

            else:
                cipher[i] = chr(cipher[i])

        output = ''.join(cipher)
        return output
        
    def decrypt(self, cipher):
        #TODO: make the n-1th Rotor rotate modulo the nth
        #TODO: work out the modulo math
        
        plain = list(ciphertext)
        
        for i in range(len(plain)):
            plain[i] = ord(plain[i])

        if plain[i] is 32:
            plain[i] = chr(plain[i])
        elif plain[i] > 64 and plain[i] < 91:
            temp = (plain[i] - ord(r1.current) - ord(r2.current) - ord(r3.current)) % 64
            #Flagged for potential modulo error
            if temp <= 64:
                temp += 26
                plain[i] = chr(temp)
            else:
                plain[i] = chr(temp)

        elif plain[i] > 96 and plain[i] < 123:
            temp = (plain[i] - ord(r1.current) - ord(r2.current) - ord(r3.current)) % 96
            #Flagged for potential modulo error
            if temp <= 96:
                temp += 26
                plain[i] = chr(temp)
            else:
                plain[i] = chr(temp)

        else:
            plain[i] = chr(plain[i])

        output= ''.join(plain)
        return output
    


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
