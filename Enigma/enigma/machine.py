import Tkinter as Tk
from Tkinter import * 


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
    
    def rotate(self):
        if len(self.data) != None:
            self.POSITION += 1
        else:
            print "There is no Rotor object to rotate"
        
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

        cipher = list(plain)

        for i in range(len(cipher)):
            cipher[i] = ord(cipher[i])

            if cipher[i] is 32:
                cipher[i] = chr(cipher[i])
                self.iterate()

            elif cipher[i] > 64 and cipher[i] < 91:
                temp = (cipher[i] + ord(self.r1.current) + ord(self.r2.current) + ord(self.r3.current)) % 65
                temp += 65
                if temp >= 91:
                    temp -= 90
                    temp += 64
                    cipher[i] = chr(temp)
                else:
                    cipher[i] = chr(temp)

                self.iterate()

            elif cipher[i] > 96 and cipher[i] < 123:
                temp = (cipher[i] + ord(self.r1.current) + ord(self.r2.current) + ord(self.r3.current)) % 97
                temp += 97
                if temp >= 123:
                    temp -= 122
                    temp += 96
                    cipher[i] = chr(temp)
                else:
                    cipher[i] = chr(temp)

                self.iterate()

            else:
                cipher[i] = chr(cipher[i])
                self.iterate()

        output = ''.join(cipher)
        return output
        
    def decrypt(self, cipher):
        
        plain = list(cipher)
        
        for i in range(len(plain)):
            plain[i] = ord(plain[i])

            if plain[i] is 32:
                plain[i] = chr(plain[i])
                self.iterate()

            elif plain[i] > 64 and plain[i] < 91:
                temp = (plain[i] - ord(self.r1.current) - ord(self.r2.current) - ord(self.r3.current)) % 26
                temp += 65
                if temp <= 64:
                    temp += 26
                    plain[i] = chr(temp)
                else:
                    plain[i] = chr(temp)

                self.iterate()
            elif plain[i] > 96 and plain[i] < 123:
                temp = (plain[i] - ord(self.r1.current) - ord(self.r2.current) - ord(self.r3.current)) % 26
                temp += 97
                if temp <= 96:
                    temp += 26
                    plain[i] = chr(temp)
                else:
                    plain[i] = chr(temp)
                self.iterate()

            else:
                plain[i] = chr(plain[i])
                self.iterate()

        output= ''.join(plain)
        return output
    
    def iterate(self):
        self.r3.rotate()
        if self.r3.POSITION == 0:
            self.r2.rotate()
            if self.r2.POSITION == 0:
                self.r1.rotate()

#-------------------------------------------------------------------------------------------

def main:
    #TODO: write GUI for the main method
    pass

"""
This is the letter arrange from the 1930 Enigma I

"""

R1 = Rotor(['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'])
R2 = Rotor(['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'])
R3 = Rotor(['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'])
    
class Machine:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

root = Tk()
machine = Machine(root)
root.mainloop()

if __name__ == "__main___":
    main()
