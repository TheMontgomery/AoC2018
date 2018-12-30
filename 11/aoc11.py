from collections import defaultdict
import time
from re import findall

workingDir = "G:/Python/adventofcode2018/11/"
start_time = time.time()
SERIAL = 18
GRIDSIZE = 52

def getPower(x, y):
    #print("x: {0}\ty: {1}".format(x, y))
    rackId = x + 10
    #print("rackId:", rackId)
    powerLevel = rackId * y
    #print("powerLevel:", powerLevel)
    powerLevel += SERIAL
    #print("powerLevel:", powerLevel)
    powerLevel *= rackId
    #print("powerLevel:", powerLevel)
    powerLevel = ((powerLevel // 100) % 10)
    #print("powerLevel:", powerLevel)
    powerLevel -= 5
    #print("powerLevel:", powerLevel)
    return powerLevel

print(getPower(3,5))

powerLevels = defaultdict(tuple)

for i in range(1, GRIDSIZE + 1):
    for j in range (1, GRIDSIZE + 1):
        #print("Coordinates: {0},{1}\tpowerLevel: {2}".format(i, j, getPower(i, j)))
        powerLevels[(i, j)] = getPower(i, j)

#print(powerLevels)

display = [['   ']*5 for i in range(5)]

for i in range(32, 37):
    for j in range(44, 49):
        #print("{0}, {1}: ".format(i,j), powerLevels[(i, j)])
        #display[i-32][j-44] = str(powerLevels[(i, j)]).rjust(3)
        display[j - 44][i - 32] = str(powerLevels[(i, j)]).rjust(3)

for row in display:
    print(''.join(row))