class KeyedCaesarCipher:
    def __init__(self) -> None:
        self.__plain = []
        self.__cipher = []
        self.__keyword = ""

    def setKeyword(self, keyword):
        self.__keyword = keyword

    def __initialiseKeys(self):
        self.__cipher = []
        self.__plain = []

        #Initialises cipherText list with 26 empty spaces
        for i in range(0, 26):
            self.__cipher.append("_")

        #Creates list of ASCII values for the plaintext alphabet
        # i.e. [a, b, c, d, e, ... , z]
        for i in range(97, 123):
            self.__plain.append(i)


    def createCipher(self, offset):
        self.__initialiseKeys()
        pos = 0 - offset

        #Adds the letters in the keyword to the cipherText without
        #repeating letters that appear twice.
        for i in self.__keyword:
            #Checks if the letter it's appending appears more than once
            #in the ciphertext
            if not self.__cipher.count(ord(i)) > 0:
                self.__cipher[pos] = ord(i)
                pos += 1
                if pos > 25:
                    pos -= 26

        #Adds the rest of the alphabet after the keyword letters
        for i in self.__plain:
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


    def bruteForce(self, cipherText):
        result = []

        for i in range(0, 25):
            self.createCipher(i)
            result.append("Offset: " + str(i) + ", Plaintext: " + self.decrypt(cipherText))
        
        return result



kcc = KeyedCaesarCipher()
kcc.setKeyword('tucker')
print(kcc.bruteForce('auvtbeqh iqdeua'))