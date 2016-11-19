# crytography-project

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
        FILES:
            1. Rotor.py
                -Unit test: testRotor
                -Methods:
                    a. rotate() - moves the Rotor one position
                    b. setStart() - sets the starting position for each rotor
            2. Core.py
                -Central hub for the logic of the Enigma Machine, in charge of encrypt/decrypt as well as rotor settings
                -Methods:
                    a. buildRotor() - adds rotor with appropriate rotor configuration
                    b. arrageRotors() - arrages the order of the individual Rotors
                    c. encrypt() - runs the encryption process
                    d. decrypt() - runs decryption process

        
        
