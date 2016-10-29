
"""
Demonstration text for program's output:


Do you wish to encrypt or decrypt a message?

encrypt

Enter your message:

The sky above the port was the color of television, tuned to a dead channel.

Enter the key number (1-26)

13

Your translated text is:

Gur fxl nobir gur cbeg jnf gur pbybe bs gryrivfvba, gharq gb n qrnq punaary.
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
		
if __name__ == '__main__': main()
