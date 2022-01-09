import time, random, copy, sys

def conwaysGame():
    try:
        WIDTH, HEIGHT = 80, 25
        alive, dead = "O", " "

        newCells = []
        for x in range(WIDTH):
            column = []
            for y in range(HEIGHT):
                if random.randint(0 ,1) == 1:
                    column.append(alive)
                else:
                    column.append(dead)
            newCells.append(column)


        while True:
            time.sleep(0.01)

            currentCells = copy.deepcopy(newCells)

            for y in range(HEIGHT):
                for x in range(WIDTH):
                    print(currentCells[x][y],end = "")
                print("")
            print(('-')*WIDTH)


            for y in range(HEIGHT):
                for x in range(WIDTH):
                    aliveCells = 0
                    leftCell = (x - 1) % WIDTH
                    rightCell = (x + 1) % WIDTH
                    upperCell = (y - 1) % HEIGHT
                    lowerCell = (y + 1) % HEIGHT

                    if currentCells[leftCell][upperCell] == alive:
                        aliveCells += 1
                    if currentCells[leftCell][lowerCell] == alive:
                        aliveCells += 1
                    if currentCells[leftCell][y] == alive:
                        aliveCells += 1
                    if currentCells[x][upperCell] == alive:
                        aliveCells += 1
                    if currentCells[x][lowerCell] == alive:
                        aliveCells += 1
                    if currentCells[rightCell][upperCell] == alive:
                        aliveCells += 1
                    if currentCells[rightCell][lowerCell] == alive:
                        aliveCells += 1
                    if currentCells[rightCell][y] == alive:
                        aliveCells += 1


                    if currentCells[x][y] == alive and (aliveCells == 2 or aliveCells == 3):
                        newCells[x][y] = alive
                    elif currentCells[x][y] == dead and aliveCells == 3:
                        newCells[x][y] = alive
                    else:
                        newCells[x][y] = dead

    except KeyboardInterrupt:
        print("\n\nPress any key to restart the simulation or 'q' to quit: ")
        if input().lower() == 'q':
            print("Goodbye!")
            sys.exit()
        else:
            conwaysGame()


conwaysGame()
