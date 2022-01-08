import random, time, copy

WIDTH, HEIGHT = 20, 20
nextCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append("#")
        else:
            column.append(' ')
    nextCells.append(column)

while True:
    time.sleep(1)
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end="")
        print()
    print("||||||||||||||||||||||||||")
    print("||||||||||||||||||||||||||")
    

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCord = (x - 1) % WIDTH
            rightCord = (x + 1) % WIDTH
            aboveCord = (y - 1) % HEIGHT
            belowCord = (y + 1) % HEIGHT

            aliveNeighbors = 0
            if currentCells[leftCord][aboveCord] == "#":
                aliveNeighbors += 1
            if currentCells[x][aboveCord] == "#":
                aliveNeighbors +=1
            if currentCells[leftCord][belowCord] == "#":
                aliveNeighbors += 1
            if currentCells[x][belowCord] == "#":
                aliveNeighbors +=1
            if currentCells [leftCord][y] == "#":
                aliveNeighbors +=1
            if currentCells [rightCord][y] == "#":
                aliveNeighbors +=1
            if currentCells[rightCord][aboveCord] == "#":
                aliveNeighbors +=1
            if currentCells[rightCord][aboveCord] == "#":
                aliveNeighbors +=1
            


            if currentCells[x][y] == "#" and (aliveNeighbors == 2 or aliveNeighbors == 3):
                nextCells[x][y] == "#"
            elif currentCells[x][y] == " " and aliveNeighbors == 3:
                nextCells[x][y] = "#"
            else:
                nextCells[x][y] = " "
    