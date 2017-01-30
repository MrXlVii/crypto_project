# cryptography-project

A repo to practice cryptography and cryptanalysis and to build skills to turn into a side project.

Projects:

    1. Caesar cipher
        - Primarily this is a program that encrypts and decrypts the caesar cipher which is a basic shift cipher.
        - Prompts the user for the appropriate input, then outputs the shifted ciphertext. 
        - Considered making the program loop until user exits, but it was more practice than anything else
        - Unit test is testCaesar.py
        
    2. Enigma Machine ver 1.0
        - Python module in the style of the Engima machine used in WW2.
        - Three Rotor Encryption Scheme:
            - i.e. each rotor has a different configuration of characters, the user picks starting position on rotor and one of six rotor configurations (for three)
  
      ** NOTE: **
            Differences between this 3-Rotor encryption/decryption scheme and the original Enigma Machine:
                - Letters can route to themselves 
                    --The original didn't allow for this, it's counter-intuitively more secure
                - Spaces, symbols, and punctuation stay the same
                    --The original had X route for each space, and punctuation was not included. It's a self-learning tool so I ignored symbols.
                - Letters are not reciprocal
                    --the original design decided that if A routes to N, then N subsequently routes to A, this is also a flaw that's not present.
        **I ignored the flaws because they didn't provide me with a conceptual understanding of the encryption scheme and only served to promote historical accuracy. 

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
                     -Methods:
                         a. init(self, master) -- constructor
                         b. begin(self) -- begins the main program loop
                         c. messageInput(self) -- takes user written input
                         d. enBut(self, plain) -- runs encryption button functionality with plaintext from user input
                         e. deBut(self, cipher) -- runs decryption button functionality with ciphertext from user input
                         f. onConfigClick(self evt) -- initializes the Core and Rotor configurations on button click
                         g. onP1Click(self, evt) -- sets first Rotor's position on click
                         h. onP2Click(self, evt) -- sets second Rotor's position on click
                         i. onP3Click(self, evt) -- sets third Rotor's position on click
                         j. quit(self) -- exits the program loop
                         k. same(self) -- continues through program loop with same Core and Rotor settings 
                         l. different(self) -- begins the program loop over to allow for changed settings
                         

        
        
