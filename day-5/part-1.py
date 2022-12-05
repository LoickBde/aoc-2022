import numpy as np

NB_SPACE_BETWEE_STACKS_LINE = 4
rawStacks = []
rawInstructions = []

def parseStacks(rawStacks):
    parsedStacks = []
    for i in range(0, len(rawStacks) - 1):
        line = rawStacks[i]
        parsedStacks.append([line[i:i+NB_SPACE_BETWEE_STACKS_LINE] 
            for i in range(0, len(line), NB_SPACE_BETWEE_STACKS_LINE)]) 
    parsedStacks = np.array(parsedStacks)
    parsedStacks = np.transpose(parsedStacks)
    parsedStacks = np.fliplr(parsedStacks)
    for iy, ix in np.ndindex(parsedStacks.shape):
        parsedCart = parsedStacks[iy, ix].rstrip().replace('[', '').replace(']','')
        parsedStacks[iy, ix] = parsedCart
    parsedStacks = [[item for item in line if item] for line in parsedStacks]
    return parsedStacks

def parseInstruction(rawInstructions):
    instructions = [[int(word) for word in line.split() if word.isdigit()] for line in rawInstructions]
    return instructions

with open('input.txt') as f:
    stacksFlag = True
    for line in f: 
        if line == '\n':
            stacksFlag = False
            continue
        if stacksFlag == True : rawStacks.append(line)
        else : rawInstructions.append(line.rstrip())

stacks = parseStacks(rawStacks)
instructions = parseInstruction(rawInstructions)

for nb, source, dest in instructions:
    for i in range(nb):
        stacks[dest-1].append(stacks[source-1].pop())

print(''.join([stack[len(stack)-1] for stack in stacks]))