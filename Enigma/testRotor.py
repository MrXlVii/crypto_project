#TODO: handle R(1,2,3) are not global variables error due to setUp()/tearDown()


import unittest
from Rotor import Rotor


class testRotor(unittest.TestCase):
     #test for Rotor.py
       
     def setUp(self):
         c1= ['A', 'B', 'C']
         c2= ['D', 'E', 'F']
         c3= ['G']
         
         R1 = Rotor(c1)
         R2 = Rotor(c2)
         R3 = Rotor(c3)
         
     def tearDown(self):
         pass
         
     def test_Instance(self):
         self.assertEqual(R1.rotorNum, 1)
         self.assertEqual(R2.rotorNum, 2)
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
         
         tearDown()
     
     def test_Set_Start(self): 
         P1 = 0
         P2 = 1
         P3 = 35
         
         R1.setStart(P1)
         R2.setStart(P2)
         R3.setStart(P3)
         
         self.assertEqual(Rotor.POSITION, P1, 'incorrect position')
         self.assertEqual(Rotor.POSITION, P2, 'incorrect position')
         self.assertEqual(Rotor.POSITION, P3, 'does not account for modulo--optional')
     
     def test_Rotate(self):
         R1.setStart(0)
         R2.setStart(0)
         R3.setStart(0)
         
         R1.rotate()
         self.assertEqual(R1.POSITION, 1)
         
         for i in range(0,100):
             R2.rotate()
         self.assertEqual(R2.POSITION, 99)
         
         R3.rotate()
         self.assertEqual(R3.POSITION, 0, 'should not rotate, there is only one value')
             
         
if __name__ == "__main__":
    unittest.main()
         
