import Tkinter as Tk
from Tkinter import * 


class Rotor(object):
    """Basic Rotor class for Enigma Machine."""

    def __init__(self, data):
        self.data = data
        self.POSITION = 0   #Current position on Rotor
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
            print "There is no Rotor object to rotate."
        
#---------------------------------------------------------------------------------------------

class Core(object):
    
    def __init__(self, first, second, third):
        self.r1 = first
        self.r2 = second
        self.r3 = third

    def config(self, first, second, third, p1, p2, p3):
        #Sets the current rotor configuration and positions of each respective Rotor.
        
        self.r1 = first
        self.r2 = second
        self.r3 = third
        
        self.r1.POSITION = p1
        self.r2.POSITION = p2
        self.r3.POSITION = p3
        
    def encrypt(self, plain):
        #TODO: determine why some symbols appear in cipher
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
                cipher[i] -= 32 #Changes lowercase to uppercase to keep with Enigma-style output.
                temp = (cipher[i] + ord(self.r1.current) + ord(self.r2.current) + ord(self.r3.current)) % 65
                temp += 65
                if temp >= 91:
                    temp -= 90
                    temp += 64
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
                plain[i] -= 32 #Changes lowercase input to uppercase to keep with Enigma-style output.
                temp = (plain[i] - ord(self.r1.current) - ord(self.r2.current) - ord(self.r3.current)) % 26
                temp += 65
                if temp <= 64:
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

"""
This is the letter arrangement from the 1930 Enigma I.

"""

class Machine:

#TODO: Step 1: Welcomes, prompts to begin or quit.
#Step 2: Ask for Rotor configuration (I-II-III, I-III-II, II-I-III, II-III-I, III-I-II, or III-II-I).
#Step 3: Ask for position for each rotor (0-25).
#Step 4: Ask whether the user wishes to encrypt or decrypt.
#Step 5: Ask the user to input the plaintext/ciphertext.
#TODO: Step 6: Returns the appropriate text. 
#TODO: Step 7: Prompts to continue the program with the rotor settings, different settings, or to quit.

    def __init__(self, master):
        self.master = master
        self.core = None
        self.R1 = Rotor(['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'])
        self.R2 = Rotor(['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'])
        self.R3 = Rotor(['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'])

        frame = Frame(master)
        frame.pack()        

        q1 = Label(master, text = 'Which rotor configuration are you using?')
        q1.pack()
        listbox = Listbox(master, selectmode = SINGLE)
        listbox.pack()

        for item in ['I-II-III', 'I-III-II', 'II-I-III', 'II-III-I', 'III-I-II', 'III-II-I']:
            listbox.insert(END, item)

        listbox.bind('<<ListboxSelect>>', self.onConfigClick)

        q2 = Label(text = 'Which position will each rotor be set to?')
        q2.pack()
        lb1 = Listbox(selectmode = SINGLE)
        lb2 = Listbox(selectmode = SINGLE)
        lb3 = Listbox(selectmode = SINGLE)
        lb1.pack()
        lb2.pack()
        lb3.pack()
        

        for item in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']:
            lb1.insert(END, item)
            lb2.insert(END, item)
            lb3.insert(END, item)

        lb1.bind('<<ListboxSelect>>', self.onP1Click)
        lb2.bind('<<ListboxSelect>>', self.onP2Click)
        lb3.bind('<<ListboxSelect>>', self.onP3Click)

        confirm = Button(text = 'Confirm', command = self.messageInput)
        confirm.pack()

    def messageInput(self):
        #TODO: Kill previous frame, reveal only entry box.
        greeting = Label(text = 'Would you like to encrypt or decrypt this message?')
        greeting.pack(side = TOP)

        e = Entry()
        e.pack()

        #TODO: Create a frame for the (en/de)crypt buttons
        encryptButton = Button(text = 'Encrypt', fg = 'black', command = lambda: self.enBut(e.get()))
        encryptButton.pack()
        decryptButton = Button(text = 'Decrypt', fg = 'black', command = lambda: self.deBut(e.get()))
        decryptButton.pack()

    def enBut(self, plain):
        cipher = self.core.encrypt(plain)
        print cipher
        output = Label(text = cipher)
        output.pack()
        
    def deBut(self, cipher):
        plain = self.core.decrypt(cipher)
        print plain
        output = Label(text = plain)
        output.pack()

    def onConfigClick(self, evt):
        #Initializes the Core and Rotor configuration on click
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print index, value

        rotorCon = { 
            0: Core(self.R1, self.R2, self.R3),
            1: Core(self.R1, self.R3, self.R2),
            2: Core(self.R2, self.R1, self.R3),
            3: Core(self.R2, self.R3, self.R1), 
            4: Core(self.R3, self.R1, self.R2),
            5: Core(self.R3, self.R2, self.R1)
        }
        self.core = rotorCon.get(index)
        
    def onP1Click(self, evt):
        #Sets the first Rotor's position on click
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print index, value
        self.core.r1.POSITION = index

    def onP2Click(self, evt):
        #Sets the second Rotor's position on click
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print index, value
        self.core.r2.POSITION = index

    def onP3Click(self, evt):
        #Sets the third Rotor's position on click
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print index, value
        self.core.r3.POSITION = index

root = Tk()
machine = Machine(root)
root.mainloop()

if __name__ == "__main___":
    main()
