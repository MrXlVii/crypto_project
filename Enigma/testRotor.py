#TODO: handle R(1,2,3) are not global variables error due to setUp()/tearDown()


import unittest
from Rotor import Rotor


class testRotor(unittest.TestCase):
    #test for Rotor.py
       
    c1= ['A', 'B', 'C']
    c2= ['D', 'E', 'F']
    c3= ['G']
      
    def test_Instance(self):
        R1 = Rotor(self.c1)
        self.assertEqual(R1.rotorNum, 1)
        R2 = Rotor(self.c2)
        self.assertEqual(R2.rotorNum, 2)
        R3 = Rotor(self.c3)
        self.assertEqual(R2.rotorNum, 3)
         
        for i in range(4,100):
           R = Rotor(self.c1)
             
        self.assertEqual(R.rotorNum, 99)
         
        print R1.config
        self.assertEqual(R1.config, self.c1, 'failed to install correct rotor config')
        print R2.config
        self.assertEqual(R2.config, self.c2, 'failed to install correct rotor config')
        print R3.config
        self.assertEqual(R3.config, self.c3, 'failed to install correct rotor config')
         
    def test_Set_Start(self):
        R1 = Rotor(self.c1)
        R2 = Rotor(self.c2)
        R3 = Rotor(self.c3) 
         
        P1 = 0
        P2 = 1
        P3 = 35
         
        R1.setStart(P1)
        R2.setStart(P2)
        R3.setStart(P3)
         
        self.assertEqual(R1.POSITION, P1, 'incorrect position')
        self.assertEqual(R2.POSITION, P2, 'incorrect position')
        self.assertEqual(R3.POSITION, P3, 'does not account for modulo--optional')
     
    def test_Rotate(self):
        R1 = Rotor(self.c1)
        R2 = Rotor(self.c2)
        R3 = Rotor(self.c3)
             
        R1.setStart(0)
        R2.setStart(0)
        R3.setStart(0)
         
        R1.rotate()
        self.assertEqual(R1.POSITION, 1)
         
        for i in range(0,100):
            R2.rotate()
        self.assertEqual(R2.POSITION, 100)
        
        #TODO: Determine how we'd like to handle modulo positions 
        R3.rotate()
        self.assertEqual(R3.POSITION, 0, 'should not rotate, there is only one value')
             
         
if __name__ == "__main__":
    unittest.main()
         
