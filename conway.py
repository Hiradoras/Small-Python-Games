import time, random, copy


WIDTH, HEIGHT = 50, 20
newCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 1:
            column.append("#")
        else:
            column.append(" ")
    newCells.append(column)

while True:
    time.sleep(0.01)
    currentCells = copy.deepcopy(newCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end="")
        print("")
    print(("-")*WIDTH)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCell  = (x - 1) % WIDTH
            rightCell = (x + 1) % WIDTH
            aboveCell = (y - 1) % HEIGHT
            belowCell = (y + 1) % HEIGHT

            aliveCells = 0

            if currentCells[leftCell][aboveCell] == "#":
                aliveCells += 1
            if currentCells[leftCell][belowCell] == "#":
                aliveCells += 1
            if currentCells[leftCell][y] == "#":
                aliveCells += 1
            if currentCells[x][aboveCell] == "#":
                aliveCells += 1
            if currentCells[x][belowCell] == "#":
                aliveCells += 1
            if currentCells[rightCell][aboveCell] == "#":
                aliveCells += 1
            if currentCells[rightCell][belowCell] == "#":
                aliveCells += 1
            if currentCells[rightCell][y] == "#":
                aliveCells += 1

            if currentCells[x][y] == "#" and (aliveCells ==2 or aliveCells == 3):
                newCells[x][y] = "#"
            elif currentCells[x][y] == " " and aliveCells == 3:
                newCells[x][y] = "#"
            else:
                newCells[x][y] = " "
