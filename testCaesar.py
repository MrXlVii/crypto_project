import unittest
import Caesar

class TestCryptMethods(unittest.TestCase):
    """Tests for Caesar.py"""
    cryptInput = ['encrypt', 'Encrypt', 'decrypt', 'Decrypt', 'blah', 'WHOCARES']
    encryptInput = ['foo', 'bar', 'Hello World', 'xyz', '101010111']
    decryptInput = ['ktt', 'gfw', 'Mjqqt Btwqi', 'cde', '101010111']
    
    def test_crypt(self):
        result = []
        
        for i in range(len(self.cryptInput)):
            result.append(Caesar.crypt(self.cryptInput[i]))
        self.assertTrue(result[0])
        self.assertTrue(result[1])
        self.assertFalse(result[2])
        self.assertFalse(result[3])
        #self.assertRaises
        #self.assertRaises
        
    def test_encryption(self):
        result = []
        
        for i in range(len(self.encryptInput)):
            result.append(Caesar.encryption(self.encryptInput[i], 5))
            self.assertEqual(result[i], self.decryptInput[i])
        
        
    def test_decryption(self):
        pass
    
    #TODO: test decryption runs appropriately

if __name__ == "__main__":
    unittest.main()    
