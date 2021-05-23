menuElements = ["*** Menu ***"," ", "1. Encrypt string ", "2. Decrypt string", "3. Brute force decryption", "4. Quit", " "]

inputString = "auvtbeqh iqdeua"

keyWord = "tucker"
offset = 19
pos = 0 - offset
posStart = pos

plainText = []

encrypting = False
decrypting = False
bruteForce = False
usingProgram = True


while usingProgram == True:

    offsetInRange = False
    commandInRange = False
    
    ASCIITranslation = []
    outputString = ""

    while commandInRange == False:
        for i in range(len(menuElements)):
            print (menuElements[i])
        command = int(input(">"))

        
        #Checks that the number the user enters is between 1 and 4
        if command < 1 or command > 4:  
            print ("Invalid choice, please enter either 1, 2, 3, or 4.\n")
                
        #If the user input between 1 and 4, it lets the user leave the loop
        else:
            commandInRange = True

    #Checks what number the user enters and enables that process in the program or exits the user from the program
    if command == 1:
        encrypting = True
    elif command == 2:
        decrypting = True
    elif command == 3:
        bruteForce = True
    elif command == 4:
        usingProgram = False
    

    while encrypting == True:   
        for i in range(0, 26):
            ASCIITranslation.append("_")

        for i in range(97, 123):
            plainText.append(i)

        for i in keyWord:
            if not ASCIITranslation.count(ord(i)) > 0:
                ASCIITranslation[pos] = ord(i)
                pos += 1
                if pos > 25:
                    pos -= 26

        for i in plainText:
            if not ASCIITranslation.count(i) > 0:
                ASCIITranslation[pos] = i
                pos += 1
                if pos > 25:
                    pos -= 26

        for i in inputString:
            if not i == " ":
                outputString += chr(ASCIITranslation[plainText.index(ord(i))])
            else:
                outputString += " "
                
        print (outputString)
        encrypting = False


        

    while decrypting == True:  
        for i in range(0, 26):
            ASCIITranslation.append("_")

        for i in range(97, 123):
            plainText.append(i)

        for i in keyWord:
            if not ASCIITranslation.count(ord(i)) > 0:
                ASCIITranslation[pos] = ord(i)
                pos += 1
                if pos > 25:
                    pos -= 26

        for i in plainText:
            if not ASCIITranslation.count(i) > 0:
                ASCIITranslation[pos] = i
                pos += 1
                if pos > 25:
                    pos -= 26

        for i in inputString:
            if not i == " ":
                outputString += chr(plainText[ASCIITranslation.index(ord(i))])
            else:
                outputString += " "
                
        print (outputString)
        decrypting = False


