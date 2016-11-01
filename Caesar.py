
"""
Demonstration text for program's output:

Do you wish to encrypt or decrypt a message?  encrypt
Enter your message:  The sky above the port was the color of television, tuned to a dead channel.
Enter the key number (1-26)  13
Your translated text is:  Gur fxl nobir gur cbeg jnf gur pbybe bs gryrivfvba, gharq gb n qrnq punaary.
"""



def main():

#TODO: make program cycle for correct input

en_de_crypt = raw_input('Do you wish to "encrypt" or "decrypt" a message?')
inputMessage = raw_input('Enter your message:')
keySize = raw_input('Enter the key number (1-26)')

print 'Your translated text is: " + value

def crypt(cryptInput):
	#returns boolean value, true if encrypt, false if decrypt

	if en_de_crypt is 'encrypt' or 'Encrypt':
		return True
	elif en_de_crypt is 'decrypt' or 'Decrypt':
		return False
	else:
		print 'Write either "encrypt" or "decrypt"'

def encryption(plaintext, size):
	#TODO: takes in message string and the key size, and runs caesar cipher
	
	cipher = list(plaintext.copy()) 
	
	for i in range(len(cipher))
		cipher[i] = char(ord(cipher[i]) + size)
	
	return cipher
	

def decryption(ciphertext, size):
	#TODO: takes in the ciphertext and key size, performs reverse caeasar cipher
	
	plaintext = list(ciphertext.copy()) 
	
	for i in range(len(plaintext))
		plaintext[i] = char(ord(plaintext[i]) - size)
	
	return plaintext
		
		
if __name__ == '__main__': main()
