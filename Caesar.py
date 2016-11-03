
"""
Demonstration text for program's output:
Do you wish to encrypt or decrypt a message?  encrypt
Enter your message:  The sky above the port was the color of television, tuned to a dead channel.
Enter the key number (1-26)  13
Your translated text is:  Gur fxl nobir gur cbeg jnf gur pbybe bs gryrivfvba, gharq gb n qrnq punaary.
"""

"""
en_de_crypt = ''
inputMessage = ''
keySize = ''
"""

def main():
	#TODO: test that program cycles correctly
	
	while(True):
		en_de_crypt = raw_input('Do you wish to "encrypt" or "decrypt" a message? ')
		if en_de_crypt is 'encrypt' or 'Encrypt' or 'decrypt' or 'Decrypt':
			break
		else:
			print "you need to write 'encrypt' or 'decrypt'"
			continue

	while(True):
		inputMessage = raw_input('Enter your message: ')
		if inputMessage is None:
			print "you need to enter a message"
			continue
		else:
			break
	
	while(True):
		keySize = raw_input('Enter the key number (1-26): ')
		keySize = int(keySize)
		if keySize is None:
			print "you need to enter a key number"
			continue
		elif type(keySize) is int:
			if keySize > 26 or keySize < 1:
				print "enter a value between 1 and 26"
				continue
			else:
			    logic = crypt(en_de_crypt)
			    break

		else:
			print "Enter an integer key number (1-26)"
			pass
			
	if logic is True:
	    cipher= encryption(inputMessage, keySize)
	    print cipher
	elif logic is False:
	    plain= decryption(inputMessage, keySize)
	    print plain
	else:
	    pass
        #throw exception
              
def crypt(cryptInput):
	#returns boolean value, true if encrypt, false if decrypt

	if cryptInput is 'encrypt' or 'Encrypt':
		return True
	elif cryptInput is 'decrypt' or 'Decrypt':
		return False
	else:
		pass
		#throw exception

def encryption(plaintext, size):
	#takes in message string and the key size, and runs caesar cipher
	
	cipher = list(plaintext) 
	
	for i in range(len(cipher)):
		cipher[i] = chr(ord(cipher[i]) + size)
	
	output= ''.join(cipher)
	
	return output
	

def decryption(ciphertext, size):
	#takes in the ciphertext and key size, performs reverse caeasar cipher
	
	plaintext = list(ciphertext) 
	
	for i in range(len(plaintext)):
		plaintext[i] = chr(ord(plaintext[i]) - size)
	
	output= ''.join(plaintext)	
	
	return output
		
		
if __name__ == '__main__': 
    main()
