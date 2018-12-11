#import numpy as np
import math
from collections import defaultdict, namedtuple
from itertools import combinations

workingDir = "G:/Python/adventofcode2018/6/"
coordList = []
coords = set()
with open(workingDir + 'input2') as inFile:
    pointnames ="ABCDEFGH"
    for line in inFile:
        x, y = line.rstrip().split(", ")
        # print("line:", line, "x:", x, "y:", y)
        coordList.append((int(x),int(y)))
    inFile.close()

print(coordList)
# Calculate distance between 2 points
# Inputs a and b are tuples of 2 numbers (x, y).
def distance(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return abs(x1 - x2) + abs(y1 - y2)

# Find nearest neighbors
# Inputs: tuple of point coordinates (p), and List of coordinates to check (arr)
def findNearest(p, arr):
    nearest = None
    isTie = False

    for point in arr:
        d = distance(p, point)


# Determine if point extends to infinity
def isInfinite(p):
    infinite = False

# for i, j in combinations(coordList, 2):
#     print("coordinate pair: ", i, j)
#     print("Manhattan distance: ", distance(i, j))

maxX = max(coordList, key=lambda x: x[0])[0]
minX = min(coordList, key=lambda x: x[0])[0]
maxY = max(coordList, key=lambda y: y[1])[1]
minY = min(coordList, key=lambda y: y[0])[1]
print("max X:", maxX, 'max Y:', maxY)
print("min X:", minX, 'min Y:', minY)

for i in range(minX, maxX):
    for j in range(minY, maxY):
        d = min(coordList, key=lambda r: distance((i, j), r))
        print(f"Position: ({i}, {j}) \tMin distance: {d}")