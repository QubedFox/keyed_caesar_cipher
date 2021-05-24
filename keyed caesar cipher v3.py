# menuElements = ["*** Menu ***"," ", "1. Encrypt string ", "2. Decrypt string", "3. Brute force decryption", "4. Quit", " "]

# inputString = "auvtbeqh iqdeua"

# keyWord = "tucker"
# offset = 19
# pos = 0 - offset
# posStart = pos

# plainText = []

# encrypting = False
# decrypting = False
# bruteForce = False
# usingProgram = True

# while usingProgram == True:

#     offsetInRange = False
#     commandInRange = False
    
#     cipherText = []
#     outputString = ""

#     while commandInRange == False:
#         for i in range(len(menuElements)):
#             print (menuElements[i])
#         command = int(input(">"))

        
#         #Checks that the number the user enters is between 1 and 4
#         if command < 1 or command > 4:  
#             print ("Invalid choice, please enter either 1, 2, 3, or 4.\n")
                
#         #If the user input between 1 and 4, it lets the user leave the loop
#         else:
#             commandInRange = True

#     #Checks what number the user enters and enables that process in the program or exits the user from the program
#     if command == 1:
#         encrypting = True
#     elif command == 2:
#         decrypting = True
#     elif command == 3:
#         bruteForce = True
#     elif command == 4:
#         usingProgram = False
    
#     #-----ENCRYPTION-----
#     while encrypting == True:
#         #Initialises cipherText list with 26 empty spaces
#         for i in range(0, 26):
#             cipherText.append("_")

#         #Creates list of ASCII values for the plaintext alphabet
#         # i.e. [97, 98, 99, 100, 101, ... , 122]
#         for i in range(97, 123):
#             plainText.append(i)

#         #Adds the letters in the keyword to the cipherText without
#         #repeating letters that appear twice.
#         for i in keyWord:
#             #Checks if the letter it's appending appears more than once
#             #in the ciphertext
#             if not cipherText.count(ord(i)) > 0:
#                 cipherText[pos] = ord(i)
#                 pos += 1
#                 if pos > 25:
#                     pos -= 26

#         #Adds the rest of the alphabet after the keyword letters
#         for i in plainText:
#             #Checks if the letter it's appending appears more than once
#             #in the ciphertext
#             if not cipherText.count(i) > 0:
#                 cipherText[pos] = i
#                 pos += 1
#                 if pos > 25:
#                     pos -= 26

#         #Encrypts the users input string with the ciphertext
#         for i in inputString:
#             #Checks if the character is a space
#             if not i == " ":
#                 #Gets the index for the character to be encrypted in the
#                 #plaintext and passes that index to the ciphertext, encrypting
#                 #the character
#                 outputString += chr(cipherText[plainText.index(ord(i))])
#             else:
#                 outputString += " "
                
#         print (outputString)
#         encrypting = False


        
#     #-----DECRYPTION-----
#     while decrypting == True:
#         #Initialises cipherText list with 26 empty spaces
#         for i in range(0, 26):
#             cipherText.append("_")

#         #Creates list of ASCII values for the plaintext alphabet
#         # i.e. [a, b, c, d, e, ... , z]
#         for i in range(97, 123):
#             plainText.append(i)

#         #Adds the letters in the keyword to the cipherText without
#         #repeating letters that appear twice.
#         for i in keyWord:
#             #Checks if the letter it's appending appears more than once
#             #in the ciphertext
#             if not cipherText.count(ord(i)) > 0:
#                 cipherText[pos] = ord(i)
#                 pos += 1
#                 if pos > 25:
#                     pos -= 26

#         #Adds the rest of the alphabet after the keyword letters
#         for i in plainText:
#             #Checks if the letter it's appending appears more than once
#             #in the ciphertext
#             if not cipherText.count(i) > 0:
#                 cipherText[pos] = i
#                 pos += 1
#                 if pos > 25:
#                     pos -= 26

#         #Decrypts the users input string with the ciphertext
#         for i in inputString:
#             #Checks if the current character is a space
#             if not i == " ":
#                 #Gets the index for the encryted character in the ciphertext
#                 #and passes that same index to the plaintext, decrytping the
#                 #character
#                 outputString += chr(plainText[cipherText.index(ord(i))])
#             else:
#                 outputString += " "
                
#         print (outputString)
#         decrypting = False

class KeyedCaesarCipher:
    def __init__(self) -> None:
        self.__plain = []
        self.__cipher = []

    def initialiseKeys(self):
        #Initialises cipherText list with 26 empty spaces
        for i in range(0, 26):
            self.__cipher.append("_")

        #Creates list of ASCII values for the plaintext alphabet
        # i.e. [a, b, c, d, e, ... , z]
        for i in range(97, 123):
            self.__plain.append(i)

    def createCipher(self, keyword, offset):
        self.initialiseKeys()
        pos = 0 - offset

        #Adds the letters in the keyword to the cipherText without
        #repeating letters that appear twice.
        for i in keyword:
            #Checks if the letter it's appending appears more than once
            #in the ciphertext
            if not self.__cipher.count(ord(i)) > 0:
                self.__cipher[pos] = ord(i)
                pos += 1
                if pos > 25:
                    pos -= 26

        #Adds the rest of the alphabet after the keyword letters
        for i in self.plain:
            #Checks if the letter it's appending appears more than once
            #in the ciphertext
            if not self.__cipher.count(i) > 0:
                self.__cipher[pos] = i
                pos += 1
                if pos > 25:
                    pos -= 26


    def encrypt(self, plainText):
        cipherText = ""

        #Encrypts the users input string with the ciphertext
        for i in plainText:
            #Checks if the character is a space
            if not i == " ":
                #Gets the index for the character to be encrypted in the
                #plaintext and passes that index to the ciphertext, encrypting
                #the character
                cipherText += chr(self.__cipher[self.__plain.index(ord(i))])
            else:
                cipherText += " "
                
        return cipherText

    def decrypt(self, cipherText):
        plainText = ""

        #Decrypts the users input string with the ciphertext
        for i in cipherText:
            #Checks if the current character is a space
            if not i == " ":
                #Gets the index for the encryted character in the ciphertext
                #and passes that same index to the plaintext, decrytping the
                #character
                plainText += chr(self.__plain[self.__cipher.index(ord(i))])
            else:
                plainText += " "

        return plainText
                
