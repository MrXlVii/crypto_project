"""

The housing for the Rotors, functions as a doubly linked list

"""

def class Core:

    head= None
    tail= None
    
    def append(self, data):
        newRotor = Rotor(data, None, None)
        
        if self.head is None:
            self.head = self.tail = newRotor
        else:
            newRotor.prev = self.tail
            newRotor.next = None
            self.tail.next = newRotor
            self.tail = newRotor
          
    def remove(self, value):  
        pass
    
    def show(self):  
        pass
        
    
