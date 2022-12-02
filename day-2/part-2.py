rawRounds = []
totPts = 0; 

refRoundIssueTable = {
    'AX': 'S', 
    'BX': 'R', 
    'CX': 'P', 
    'AY': 'R', 
    'BY': 'P', 
    'CY': 'S', 
    'AZ': 'P', 
    'BZ': 'S', 
    'CZ': 'R', 
}
refObjectUsedScoreTable = {
    'R': 1, 
    'P': 2, 
    'S': 3, 
}
refScoreTable = {
    'X': 0, 
    'Y': 3, 
    'Z': 6, 
}

with open('input.txt') as f:
    rawRounds =  [line.rstrip().replace(" ", "") for line in f]

for rawRound in rawRounds:
    totPts += refScoreTable[rawRound[1]] + refObjectUsedScoreTable[refRoundIssueTable[rawRound]]
        
print(totPts)
