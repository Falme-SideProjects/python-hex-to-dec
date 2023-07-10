import sys

#List/Dictionary of numbers above 9
#To be called from a loop
associationList = [
            ['A', 10],
            ['B', 11],
            ['C', 12],
            ['D', 13],
            ['E', 14],
            ['F', 15],
        ]

def ToDecimal(hexChar):
    
    #First try the string/char range of numbers
    #If there's a match of the key, return value
    for item in associationList:
        if item[0] == hexChar.upper():
            return item[1]

    #Try to return a valid number, if not, return -1
    try:
        return int(hexChar)
    except:
        return 0

def HexToDec():
    
    #Total Sum after calculations
    total = 0
 
    #Try to parse the user input, if cannot, show error
    try:
        #Go through all input chars backwards
        for x,char in enumerate(reversed(sys.argv[1])):
            
            #Multiply the respective position Hexadecimal
            #To the decimal value
            multiplier = ToDecimal(char) * pow(16,x)
            
            #Sum/Add to the final result
            total += multiplier

        print(total)
    except:
        print("Not valid arguments or missing argument")

HexToDec()
