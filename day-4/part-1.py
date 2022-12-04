def sortSectionAssignement(sectionAssignement):
    sortedAssignements = [*sectionAssignement[0], *sectionAssignement[1]]
    sortedAssignements = [ int(x) for x in sortedAssignements ]
    sortedAssignements.sort()
    return sortedAssignements

def verifyOverlap(sectionAssignement, sortedSectionAssignement):
    if (int(sectionAssignement[0][0]) == sortedSectionAssignement[0] and 
        int(sectionAssignement[0][1]) == sortedSectionAssignement[len(sortedSectionAssignement)-1]): 
            return True
    if (int(sectionAssignement[1][0]) == sortedSectionAssignement[0] and 
        int(sectionAssignement[1][1]) ==  sortedSectionAssignement[len(sortedSectionAssignement)-1]):
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
    if verifyOverlap(sectionAssignement, sortSectionAssignement(sectionAssignement)) :
        overlapSectionAssigement += 1

print(f"Nb of assignment pairs overlaped: {overlapSectionAssigement}")