import unittest
import Caesar

class TestCryptMethods(unittest.TestCase):
    """Tests for Caesar.py"""
    cryptInput = ['encrypt', 'Encrypt', 'decrypt', 'Decrypt', 'blah', 'WHOCARES']
    encryptInput = ['foo', 'bar', 'Hello World', 'xyz', '101010111']
    decryptInput = ['ktt', 'gfw', 'Mjqqt Btwqi', 'cde', '101010111']
    
    def setUp(self):
        pass
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
        for i in range(len(encryptInput)):
            result.append(Caesar.encryption(self.encryptInput[i]))
    
    #TODO: test encryption runs appropriately
  
        
        
    def test_decryption(self):
        pass
    
    #TODO: test decryption runs appropriately

if __name__ == "__main__":
    unittest.main()    
