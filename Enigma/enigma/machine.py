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
        #TODO: Determine what to do with lowercase
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
        #TODO: Determine what to do with lowercase
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

"""
This is the letter arrangement from the 1930 Enigma I

"""

class Machine:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        R1 = Rotor(['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'])
        R2 = Rotor(['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'])
        R3 = Rotor(['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'])        

        q1 = Label(text = 'Which rotor configuration are you using?')
        q1.pack()
        listbox = Listbox(selectmode = SINGLE)
        listbox.pack()

        for item in ['I-II-III', 'I-III-II', 'II-I-III', 'II-III-I', 'III-I-II', 'III-II-I']:
            listbox.insert(END, item)

        listbox.bind("<Double-Button-1>") #determine what to bind to

        rotorCon = { 0: Core(R1, R2, R3), 1: Core(R1, R3, R2), 2: Core(R2, R1, R3), 3: Core(R2, R3, R1), 4: Core(R3, R1, R2), 5: Core(R3, R2, R1)}
        core = rotorCon[listbox.curselection()] #needs to be changed

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

        lb1.bind() #Figure out what to bind to
        lb2.bind()
        lb3.bind()
        
        p1 = lb1.curselection()
        p2 = lb2.curselection()
        p3 = lb3.curselection()

        confirm = Button(text = 'Confirm', command = lambda: messageInput(core, p1, p2, p3))
        confirm.pack()

    def messageInput(self, core, p1, p2, p3):
        #TODO: kill previous frame, reveal only entry box

        greeting = Label(text = 'Would you like to encrypt or decrypt this message?')
        greeting.pack(side = TOP)

        e = Entry()
        e.pack()

        self.enBut = Button(text = 'Encrypt', fg = 'black', command = lambda: enBut(core, e.get()))
        self.enBut.pack()
        self.deBut = Button(text = 'Decrypt', fg = 'black', command = lambda: deBut(core, e.get()))
        self.deBut.pack()

    def enBut(self, core, plain):
        cipher = core.encrypt(plain)
        output = Label(text = cipher)
        
    def deBut(self, core, cipher):
        plain = core.decrypt(cipher)
        output = Label(text = plain)

#TODO: step 2, Ask for rotor settings, i.e. configuration and position (possibly use buttons)
    #Use 
#TODO: step 1, Welcome, encrypt or decrypt
    #Use two buttons
#TODO: step 3. Ask for message input
    #Use text entry
#TODO: step 4, display output

root = Tk()
machine = Machine(root)
root.mainloop()

if __name__ == "__main___":
    main()
