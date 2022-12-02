rawRounds = []
totPts = 0; 
refScoreTable = {
    'BX': 1, #l r
    'CY': 2, #l p
    'AZ': 3, #l s
    'AX': 4, #d r
    'BY': 5, #d p
    'CZ': 6, #d s
    'CX': 7, #w r
    'AY': 8, #w p
    'BZ': 9, #w s
}

with open('input.txt') as f:
    rawRounds =  [line.rstrip().replace(" ", "") for line in f]

for i in range(0, len(rawRounds)):
    totPts += refScoreTable[rawRounds[i]]
        
print(totPts)
