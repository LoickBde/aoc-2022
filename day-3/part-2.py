ELFES_GROUP_SIZE = 3
rawRucksacksContent = []

def getCommonChar(strings):
    commonChar = set(strings[0]).intersection(*strings)
    return ''.join(commonChar)

with open('input.txt') as f:
    rawRucksacksContent =  [line.rstrip() for line in f]

commonChar = []
for i in range(0, len(rawRucksacksContent), ELFES_GROUP_SIZE):
    commonChar.append(getCommonChar(rawRucksacksContent[i : i + ELFES_GROUP_SIZE]))

prioritiesSum = 0
for char in commonChar:
    asciiCode = ord(char)
    prioritiesSum += asciiCode - 96 if asciiCode > 96 else asciiCode - 38

print(f"Sum of the priorities badge: {prioritiesSum}")