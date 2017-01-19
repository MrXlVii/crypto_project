# cryptography-project

A repo to practice cryptography and cryptanalysis and to build skills to turn into a side project.

Projects:

    1. Caesar cipher
        - Primarily this is a program that encrypts and decrypts the caesar cipher which is a basic shift cipher.
        - Prompts the user for the appropriate input, then outputs the shifted ciphertext. 
        - Considered making the program loop until user exits, but it was more practice than anything else
        - Unit test is testCaesar.py
        
    2. Enigma Machine [work in progress]
        - OOP working model of the Engima machine used in WW2.
        - Three Rotor Encryption Scheme:
            - i.e. each rotor has a different configuration of characters, the user picks starting position on rotor and one of six rotor configurations (for three)
  
**UPDATE: Restructuring the project for better organization, putting Rotor and Core objects into a singular module, below is subject to flux

        FILES:
            1. Machine.py
                -Primary module, contains all of the following classes
                *Rotor*
                    -Methods:
                        a. init(self, data) - constructor
                        b. rotate(self) - moves the Rotor one position
                *Core*
                    -Central hub for the logic of the Enigma Machine, in charge of encrypt/decrypt as well as rotor settings
                    -Methods:
                        a. init(self, first, second, third) -- constructor takes in three Rotors for initialization
                        b. config(self, first, second, third, p1, p2, p3) 
                            -arrages the order of the individual Rotors and their positions
                        c. encrypt(self, plain) - runs the encryption process
                        d. decrypt(self, cipher) - runs decryption process
                        e. iterate(self) - rotates the rotor objects.
                 *App*
                     -GUI for the Enigma machine, progresses in four stages
                     -Stages:
                         a. Welcomes, prompts to begin or quit
                         b. Asks for Rotor configuration (I-II-III, I-III-II, II-I-III, II-III-I, III-I-II, or III-II-I)
                         c. Asks for position for each rotor (0-25)
                         d. Asks whether the user wishes to encrypt or decrypt
                         e. Asks the user to input the plaintext/ciphertext
                         f. Returns the appropriate text
                         g. prompts to continue the program with the rotor settings, different settings, or to quit
                         

        
        
