import unittest
from enigma.machine import Rotor, Core


class TestRotorMethods(unittest.TestCase):
    #Test for Rotor object
    c1 = ['A', 'B', 'C']
    c2 = ['D', 'E', 'F']
    c3 = ['G']

    def test_Init(self):
        R1 = Rotor(self.c1)
        R2 = Rotor(self.c2)
        R3 = Rotor(self.c3)

        print R1.data
        self.assertEqual(R1.data, self.c1,
                         'failed to install correct rotor config'
                         )
        print R2.data
        self.assertEqual(R2.data, self.c2,
                         'failed to install correct rotor config'
                         )
        print R3.data
        self.assertEqual(R3.data, self.c3,
                         'failed to install correct rotor config'
                         )
        print R1.current
        self.assertEqual(R1.current, self.c1[0])
        print R2.current
        self.assertEqual(R2.current, self.c2[0])
        print R3.current
        self.assertEqual(R3.current, self.c3[0])

    def test_Rotate(self):
        R1 = Rotor(self.c1)
        R2 = Rotor(self.c2)
        R3 = Rotor(self.c3)

        R1.POSITION = 0
        R2.POSITION = 0
        R3.POSITION = 0

        R1.rotate()
        self.assertEqual(R1.POSITION, 1)

        for i in range(100):
            R2.rotate()

        self.assertEqual(R2.POSITION, 1)

        R3.rotate()
        self.assertEqual(R3.POSITION, 0, 'It should rotate and remain 0')

    def test_SetStart(self):
        R1 = Rotor(self.c1)
        R2 = Rotor(self.c2)
        R3 = Rotor(self.c3)

        P1 = 0
        P2 = 1
        P3 = 0

        R1.POSITION = P1
        R2.POSITION = P2
        R3.POSITION = P3

        self.assertEqual(R1.POSITION, P1, 'incorrect position')
        self.assertEqual(R2.POSITION, P2, 'incorrect position')


class TestCoreMethods(unittest.TestCase):
    #Test for Core object

    c1 = ['A', 'B', 'C']
    c2 = ['D', 'E', 'F']
    c3 = ['G']

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
        print core.r1.POSITION
        print core.r2.POSITION
        print core.r3.POSITION

        self.assertEqual(core.r1.current, 'C', 'failed to assign first rotor')
        self.assertEqual(core.r2.current, 'E', 'failed to assign second rotor')
        self.assertEqual(core.r3.current, 'G', 'failed to assign third rotor')

        core.config(R3, R1, R2, 0, 0, 0)
        self.assertEqual(core.r1.current, 'G', 'failed rotor reassignment')
        self.assertEqual(core.r2.current, 'A', 'failed rotor reassignment')
        self.assertEqual(core.r3.current, 'D', 'failed rotor reassignment')

    def test_Encrypt(self):
    # Changed to A-B-C bc hand tests are difficult to solve for with A-...-J
        x1 = ['A', 'B', 'C']
        x2 = ['A', 'B', 'C']
        x3 = ['A', 'B', 'C']

        R1 = Rotor(x1)
        R2 = Rotor(x2)
        R3 = Rotor(x3)

        core = Core(R1, R2, R3)

        temp = core.encrypt('ABC')
        self.assertEqual(temp, 'ACE')

        core.config(R1, R2, R3, 0, 0, 0)
        temp2 = core.encrypt('HELLO WORLD')
        self.assertEqual(temp2, 'HFNMQ YRVMF')

    def test_Decrypt(self):
        x1 = ['A', 'B', 'C']
        x2 = ['A', 'B', 'C']
        x3 = ['A', 'B', 'C']

        R1 = Rotor(x1)
        R2 = Rotor(x2)
        R3 = Rotor(x3)

        core = Core(R1, R2, R3)
        core.config(R1, R2, R3, 0, 0, 0)

        temp = core.decrypt("ACE")
        self.assertEqual(temp, "ABC")

        core.config(R1, R2, R3, 0, 0, 0)
        temp2 = core.decrypt('HFNMQ YRVMF')
        self.assertEqual(temp2, 'HELLO WORLD')

if __name__ == "__main__":
    unittest.main()
