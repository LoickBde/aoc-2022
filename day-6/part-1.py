SOP_MARKER_LENGTH = 4
signal = ''

def checkDuplicateChars(s):
    chars = {}
    for char in s:
        if chars.get(char,None) != None:
            chars[char]+=1
        else:
            chars[char] = 1
    duplicates = [key for key, value in chars.items() if value>1]
    if len(duplicates) > 0:
        return True
    return False

with open('input.txt') as f:
    signal =  f.readline().rstrip()

firstPacketCharIndex = ''
for i in range (0, len(signal)):
    sopMarker = signal[i: i + SOP_MARKER_LENGTH]
    if not checkDuplicateChars(sopMarker):
        firstPacketCharIndex = i + SOP_MARKER_LENGTH
        break

print(f"Nb char before packet : {firstPacketCharIndex}")