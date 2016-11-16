
import unittest
from Rotor import Rotor


class testRotor(unittest.TestCase):
     #test for Rotor.py
     
     c1= ['A', 'B', 'C']
     c2= ['D', 'E', 'F']
     c3= []
     
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
         self.assertEqual(R1.config, self.c1)
         print R2.config
         self.assertEqual(R2.config, self.c2)
         print R3.config
         self.assertEqual(R3.config, self.c3)
     
     def test_Rotate(self):
         pass
     
     def test_Set_Start(self):
         pass
     
     def test_Display_Position(self):
         pass
         
if __name__ == "__main__":
    unittest.main()
         
