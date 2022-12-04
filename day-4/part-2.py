def verifyOverlap(sectionAssignement):
    min1 = int(sectionAssignement[0][0])
    max1 = int(sectionAssignement[0][1])
    min2 = int(sectionAssignement[1][0])
    max2 = int(sectionAssignement[1][1])
    section1 = range(min1, max1 + 1)
    section2 = range(min2, max2 + 1)
    
    if min1 in section2 or max1 in section2: 
        return True
    if min2 in section1 or max2 in section1: 
        return True
    return False

sectionAssignements = []
with open('input.txt') as f:
    content = f.read().splitlines()
    sectionAssignements =  [
        [
            line.split(',')[0].split('-'), 
            line.split(',')[1].split('-')
        ] for line in content
    ]

overlapSectionAssigement = 0
for sectionAssignement in sectionAssignements: 
    if verifyOverlap(sectionAssignement) :
        overlapSectionAssigement += 1

print(f"Nb of assignment pairs overlaped: {overlapSectionAssigement}")