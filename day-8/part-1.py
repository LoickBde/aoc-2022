import numpy as np

rawForest = []
with open('input.txt') as f:
    rawForest =  [[int(tree) for tree in line.rstrip()] for line in f]

forest = np.array(rawForest)
forestHeight, forestWidth = forest.shape
interiorForestHeight, interiorForestWidth = forestHeight-1, forestWidth-1
visibleTrees = (forestHeight-2)*2 + (forestWidth-2)*2 + 4

for iHeight, iWidth in np.ndindex(interiorForestHeight-1, interiorForestWidth-1):
        height, width = iHeight+1, iWidth+1
        currentTreeHeight = forest[height, width]
        currentTreeRow = forest[height, :]
        currentTreeCol = forest[:, width]

        treesOnLeft = currentTreeRow[:width]
        treesOnRight = currentTreeRow[width+1:]
        treesOnTop = currentTreeCol[:height]
        treesOnBot = currentTreeCol[height+1:]

        if (currentTreeHeight > treesOnTop.max() 
            or currentTreeHeight > treesOnRight.max() 
            or currentTreeHeight > treesOnBot.max() 
            or currentTreeHeight > treesOnLeft.max()
        ):
            visibleTrees +=1        

print(f"Nb of visible trees: {visibleTrees}")