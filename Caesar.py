
"""
Demonstration text for program's output:
Do you wish to encrypt or decrypt a message?  encrypt
Enter your message:  The sky above the port was the color of television, tuned to a dead channel.
Enter the key number (1-26)  13
Your translated text is:  Gur fxl nobir gur cbeg jnf gur pbybe bs gryrivfvba, gharq gb n qrnq punaary.
"""

def main():
	
	while(True):
		en_de_crypt = raw_input('Do you wish to "encrypt" or "decrypt" a message? ')
		if (en_de_crypt == 'encrypt') or (en_de_crypt =='Encrypt') or (en_de_crypt =='decrypt') or (en_de_crypt =='Decrypt'):
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
              
def crypt(cryptInput):
	#returns boolean value, true if encrypt, false if decrypt
	
	truth = False
	
	if (cryptInput == 'encrypt') or (cryptInput =='Encrypt'):
	    truth = True
	    return truth
	elif (cryptInput == 'decrypt') or (cryptInput =='Decrypt'):
	    truth = False
	    return truth
	else:
		pass

def encryption(plaintext, size):
	#takes in message string and the key size, and runs caesar cipher
		
	cipher = list(plaintext) 
	
	for i in range(len(cipher)):
		cipher[i] = ord(cipher[i])
		
		if cipher[i] is 32:
		    cipher[i] = chr(cipher[i])
		elif cipher[i] > 64 and cipher[i] < 91:
		    temp = cipher[i] + size
		    if temp >= 91:
		        temp -= 90
		        temp += 64
		        cipher[i] = chr(temp)
		    else:
		        cipher[i] = chr(temp)    
		    
		elif cipher[i] > 96 and cipher[i] < 123:
		    temp = cipher[i] + size
		    if temp >= 123:
		        temp -= 122
		        temp += 96
		        cipher[i] = chr(temp)
		    else:
		        cipher[i] = chr(temp)
		 
		else:
		    cipher[i] = chr(cipher[i])
	
	output= ''.join(cipher)
	
	return output
	

def decryption(ciphertext, size):
	#takes in the ciphertext and key size, performs reverse caeasar cipher
	
	plain = list(ciphertext) 
	
	for i in range(len(plain)):
		plain[i] = ord(plain[i])
		
		if plain[i] is 32:
		    plain[i] = chr(plain[i])
		elif plain[i] > 64 and plain[i] < 91:
		    temp = plain[i] - size
		    if temp <= 64:
		        temp += 26
		        plain[i] = chr(temp)
		    else:
		        plain[i] = chr(temp)    
		    
		elif plain[i] > 96 and plain[i] < 123:
		    temp = plain[i] - size
		    if temp <= 96:
		        temp += 26
		        plain[i] = chr(temp)
		    else:
		        plain[i] = chr(temp)
		 
		else:
		    plain[i] = chr(plain[i])
	
	output= ''.join(plain)
	
	return output
		
		
if __name__ == '__main__': 
    main()
