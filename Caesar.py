
"""
Demonstration text for program's output:

Do you wish to encrypt or decrypt a message?  encrypt
Enter your message:  The sky above the port was the color of television, tuned to a dead channel.
Enter the key number (1-26)  13
Your translated text is:  Gur fxl nobir gur cbeg jnf gur pbybe bs gryrivfvba, gharq gb n qrnq punaary.
"""



def main():
	#TODO: test that program cycles correctly
	
	while(True):
		en_de_crypt = raw_input('Do you wish to "encrypt" or "decrypt" a message?')
		if en_de_crypt is 'encrypt' or 'Encrypt' or 'decrypt' or 'Decrypt':
			break
		else:
			print "you need to write 'encrypt' or 'decrypt'"
			pass

	while(True):
		inputMessage = raw_input('Enter your message:')
		if inputMessage is None:
			print "you need to enter a message"
			continue
		else:
			break
	
	while(True):
		keySize = raw_input('Enter the key number (1-26)')
		if keySize is None:
			print "you need to enter a key number"
			continue
		elif type(keySize) is int:
			if keySize > 26 or keySize < 1:
				print "enter a value between 1 and 26"
				continue
			else:
				break
		else:
			print "Enter an integer key number (1-26)"
			pass
			
			
	#TODO: print 'Your translated text is: " + value
	
	

def crypt(cryptInput):
	#returns boolean value, true if encrypt, false if decrypt

	if en_de_crypt is 'encrypt' or 'Encrypt':
		return True
	elif en_de_crypt is 'decrypt' or 'Decrypt':
		return False
	else:
		#throw exception

def encryption(plaintext, size):
	#takes in message string and the key size, and runs caesar cipher
	
	cipher = list(plaintext.copy()) 
	
	for i in range(len(cipher))
		cipher[i] = char(ord(cipher[i]) + size)
	
	return cipher
	

def decryption(ciphertext, size):
	#takes in the ciphertext and key size, performs reverse caeasar cipher
	
	plaintext = list(ciphertext.copy()) 
	
	for i in range(len(plaintext))
		plaintext[i] = char(ord(plaintext[i]) - size)
	
	return plaintext
		
		
if __name__ == '__main__': main()
