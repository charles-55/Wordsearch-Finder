def scanSrc(name):
    src = open(name, "r")
    grid = []

    for line in src:
        grid.append(line.split())
    
    return grid

def printGrid(grid):
    line = ""
    for i in grid:
        for j in i:
            line += f"{j} "
        print(line)
        line = ""
    print()

def findWord(grid, target):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if scanHor(grid, i, j, target) is not None:
                return scanHor(grid, i, j, target)
            elif scanVer(grid, i, j, target) is not None:
                return scanVer(grid, i, j, target)
            elif scanDiag(grid, i, j, target) is not None:
                return scanDiag(grid, i, j, target)
    
    return "Not found"

def scanHor(grid, i, j, target):
    temp, tempRev = "", ""
    if (j + len(target)) <= len(grid[0]):
        for k in range(len(target)):
            temp += grid[i][j + k]
            tempRev = grid[i][j + k] + tempRev
        if (temp == target) or (tempRev == target):
            return [i, j]
    
    return None

def scanVer(grid, i, j, target):
    temp, tempRev = "", ""
    if (i + len(target)) <= len(grid[0]):
        for k in range(len(target)):
            temp += grid[i + k][j]
            tempRev = grid[i + k][j] + tempRev
        if (temp == target) or (tempRev == target):
            return [i, j]
    
    return None

def scanDiag(grid, i, j, target):
    if ((i + len(target)) <= len(grid[0])) and ((j + len(target)) <= len(grid[0])):
        temp, tempRev = "", ""
        for k in range(len(target)):
            temp += grid[i + k][j + k]
            tempRev = grid[i + k][j + k] + tempRev
        if (temp == target) or (tempRev == target):
            return [i, j]
    if ((i - len(target) + 1) >= 0) and ((j + len(target)) <= len(grid[0])):
        temp, tempRev = "", ""
        for k in range(len(target)):
            temp += grid[i - k][j + k]
            tempRev = grid[i - k][j + k] + tempRev
        if (temp == target) or (tempRev == target):
            return [i, j]
    
    return None

if __name__ == "__main__":
    name = input("Name of wordsearch file (with extension): ")
    grid = scanSrc(name)
    #printGrid(grid)
    print(findWord(grid, input("Word to find: ")))
