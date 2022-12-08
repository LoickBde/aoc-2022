import numpy as np

def calculateScenicScore(treePosInLine, line):
    treeHeight = line[treePosInLine]
    visibleTreesPartOne = 0
    visibleTreesPartTwo = 0

    if treePosInLine < len(line)-1:
        for i in range(treePosInLine+1, len(line), 1):
            visibleTreesPartOne += 1
            if treeHeight <= line[i]:
                break

    if treePosInLine > 0:
        for i in range(treePosInLine-1, -1, -1):
            visibleTreesPartTwo += 1
            if treeHeight <= line[i]:
                break
    
    return visibleTreesPartOne * visibleTreesPartTwo

rawForest = []
with open('input.txt') as f:
    rawForest =  [[int(tree) for tree in line.rstrip()] for line in f]

forest = np.array(rawForest)
forestHeight, forestWidth = forest.shape

currentScenicScore = 0
highestScenicScore = 0
for height, width in np.ndindex(forestHeight, forestWidth):
        currentTreeRow = forest[height, :]
        currentTreeCol = forest[:, width]
        currentScenicScore = calculateScenicScore(width, currentTreeRow) * calculateScenicScore(height, currentTreeCol)
        if currentScenicScore > highestScenicScore: highestScenicScore = currentScenicScore

print(f"Highest scenic score possible for any tree: {highestScenicScore}")