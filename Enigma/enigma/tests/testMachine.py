import unittest
from enigma.machine import Rotor, Core

class TestRotorMethods(unittest.TestCase):
    #Test for Rotor object
    c1= ['A', 'B', 'C']
    c2= ['D', 'E', 'F']
    c3= ['G']
      
    
    def test_Init(self):
        R1 = Rotor(self.c1)
        self.assertEqual(R1.rotorNum, 1)
        R2 = Rotor(self.c2)
        self.assertEqual(R2.rotorNum, 2)
        R3 = Rotor(self.c3)
        self.assertEqual(R2.rotorNum, 3)
         
        for i in range(4,100):
           R = Rotor(self.c1)
             
        self.assertEqual(R.rotorNum, 99)
         
        print R1.data
        self.assertEqual(R1.data, self.c1, 'failed to install correct rotor config')
        print R2.data
        self.assertEqual(R2.data, self.c2, 'failed to install correct rotor config')
        print R3.data
        self.assertEqual(R3.data, self.c3, 'failed to install correct rotor config')
    
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
    
    def test_SetStart(self):
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

class TestCoreMethods(unittest.TestCase):
    #Test for Core object

    c1= ['A', 'B', 'C']
    c2= ['D', 'E', 'F']
    c3= ['G']


    def test_Init(self):
        R1 = Rotor(self.c1)
        R2 = Rotor(self.c2)
        R3 = Rotor(self.c3)

        coreImpl = Core(R1, R2, R3)
        
        self.assertEqual(coreImpl.r1.data, self.c1)
        self.assertEqual(coreImpl.r2.data, self.c2)
        self.assertEqual(coreImpl.r3.data, self.c3)
    
    def test_Config(self):
        R1 = Rotor(self.c1)
        R2 = Rotor(self.c2)
        R3 = Rotor(self.c3)

        core = Core(R1, R2, R3) 
        
        core.config(R1, R2, R3, 2, 1, 0)
        print core.r1.current
        print core.r2.current
        print core.r3.current

        self.assertEqual(core.r1.current, 'C', 'failed to assign first rotor')
        self.assertEqual(core.r2.current, 'E', 'failed to assign second rotor')
        self.assertEqual(core.r3.current, 'G', 'failed to assign third rotor')
        
        core.config(R3, R1, R2, 0, 0, 0)
        self.assertEqual(core.r1.current, 'G', 'failed rotor reassignment')
        self.assertEqual(core.r2.current, 'A', 'failed rotor reassignment')
        self.assertEqual(core.r3.current, 'D', 'failed rotor reassignment')
             
    def test_Encrypt(self):
        pass
    
    def test_Decrypt(self):
        pass
    

if __name__ == "__main__":
    unittest.main()

