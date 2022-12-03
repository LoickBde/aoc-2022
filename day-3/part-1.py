rawRucksacksContent = []

def getRuckstackCompartementContent(rawRucksackContent):
    strLength = len(rawRucksackContent)
    strMiddle = int(strLength/2)
    return rawRucksackContent[:strMiddle], rawRucksackContent[strMiddle:]

def getCommonChar(string1, string2): 
    for char in string1: 
        if char in string2: 
            return char

with open('input.txt') as f:
    rawRucksacksContent =  [line.rstrip() for line in f]

commonChar = []
for rawRucksackContent in rawRucksacksContent:
    rucksackPart1, rucksackPart2 = getRuckstackCompartementContent(rawRucksackContent)
    commonChar.append(getCommonChar(rucksackPart1, rucksackPart2))

prioritiesSum = 0
for char in commonChar:
    asciiCode = ord(char)
    prioritiesSum += asciiCode - 96 if asciiCode > 96 else asciiCode - 38

print(f"Sum of the priorities: {prioritiesSum}")