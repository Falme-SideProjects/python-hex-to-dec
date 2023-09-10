import sys

# Text like "0x30 0x40 0x50" convert to array
def TrimHexString(originalString):

    #Split the values to an array
    hexValues = originalString.split()

    # Check if need to trim the 0x from hex text
    for index,val in enumerate(hexValues):
        # If does have 0x, remove it
        if val[:2] == "0x":
            hexValues[index] = val[2:]

    #return final list array
    return hexValues


# Join all hex arrays to a single string 
def ConcatenateHexList(hexList):
    return "".join(hexList)

# Get the first value from command line to trim and join
hexConcatenated = ConcatenateHexList(TrimHexString(sys.argv[1]))

# decode the hex to ascii and show results
result = bytes.fromhex(hexConcatenated).decode("utf-8")
print(result)
