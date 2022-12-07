DISK_SPACE = 70000000
UPDATE_NEEDED_SPACE = 30000000

cli = []
filesTree = {}

def updateDirSize(tree, cwd, fileSize):
    cwdCopy = cwd.copy()
    for _ in range(0, len(cwdCopy)):
        readableCwd = '/' + '/'.join(cwdCopy)
        tree[readableCwd] = tree.get(readableCwd, 0) + fileSize
        cwdCopy.pop()
    tree['/'] = tree.get('/', 0) + fileSize

with open('input.txt') as f:
    cli =  [line.rstrip() for line in f]

cwd = []
for line in cli:
    items = line.split(' ')
    if items[0] == '$':
        if items[1] == 'cd': 
            if items[2] == '..':
                cwd.pop()
            elif items[2] == '/':
                cwd.clear()
            else:
                cwd.append(items[2])
    elif items[0].isnumeric() == True:
        updateDirSize(filesTree, cwd, int(items[0]))

spaceToFree = UPDATE_NEEDED_SPACE - (DISK_SPACE - filesTree.get('/'))
smallestDirSizeToDelete = DISK_SPACE
for key, value in filesTree.items():
    if value < smallestDirSizeToDelete and value >= spaceToFree:
        smallestDirSizeToDelete = value

print(f"Smallest dir size to delete: {smallestDirSizeToDelete}")