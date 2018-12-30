from collections import defaultdict
import time
from re import findall

workingDir = "G:/Python/adventofcode2018/11/"
start_time = time.time()
SERIAL = 5093
GRIDSIZE = 300

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
powerSums = defaultdict(tuple)

# Calculate the power level for each cell
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


# For each cell, calculate the combined power of 3x3 area, keyed on the top-left point
# Max range is x-2 * y-2, due to 3x3 region
for i in range(1, GRIDSIZE-1):
    for j in range(1, GRIDSIZE-1):
        powerSum = 0
        for x in range(i, i+3):
            for y in range(j, j+3):
                powerSum += powerLevels[(x, y)]
        #print("Point: {0}, {1}\tSum of power levels: {2}".format(i, j, powerSum))
        powerSums[(i, j)] = powerSum


bestRegion = max(powerSums.items(), key=lambda k: k[1])
#bestRegion = max(powerSum, key=powerSum.get)
print("Part 1:")
print("Best point: {0}\tTotal power level: {1}".format(bestRegion[0], bestRegion[1]))