from collections import defaultdict
import time
from re import findall

workingDir = "G:/Python/adventofcode2018/10/"
TIME_RANGE = 15000
start_time = time.time()

with open(workingDir + "input") as inFile:
    points = [line.rstrip('\n') for line in inFile]
    points = [[int(n) for n in findall(r'-?\d+', line)] for line in points]
    inFile.close()

# Determine the bounds of the window
# max_x = max_y = 1
# min_x = min_y = 15000
# keySec = 0
# for point in points:
#     max_x = max(max_x, point[0])
#     max_y = max(max_y, point[1])
#     min_x = min(min_x, point[0])
#     min_y = min(min_y, point[1])

# print("Bounds:\nMin X: {0}\nMax X: {1}\nMin Y: {2}\nMax Y: {3}".format(min_x, max_x, min_y, max_y))
areas = []

for sec in range(1, TIME_RANGE):
    min_x, max_x, min_y, max_y = 10000, 0, 10000, 0
    for x, y, vel_x, vel_y in points:
        #print("Time: {0}\tx: {1}\ty: {2}\tvel x: {3}\tvel y: {4}".format(sec, x, y, vel_x, vel_y))
        max_x = max(max_x, x + (sec * vel_x))
        max_y = max(max_y, y + (sec * vel_y))
        min_x = min(min_x, x + (sec * vel_x))
        min_y = min(min_y, y + (sec * vel_y))
    searchArea = [max_x, min_x, max_y, min_y]
    areas.append(searchArea)

    #print("Time: {0}\tsearchArea: {1}\t(max_x - min_x) * (max_y - min_y): {2}".format(sec, searchArea, (max_x - min_x) * (max_y - min_y)))
    # if (max_x - min_x) * (max_y - min_y) <= searchArea:
    #     print("Continue search")
    #     #Continue
    # # If areas is increasing, we have passed optimal second
    # else:
    #     keySec = sec - 1
    #     break

bestSec = areas.index(min(areas, key=lambda x: x[0] - x[1] * x[2] - x[3])) + 1
max_x, min_x, max_y, min_y = areas[bestSec-1]
print("Part 1:")
print("Second of convergence:", bestSec, "max_x: {0}\tmin_x: {1}\tmax_y: {2}\tmin_y: {3}".format(max_x, min_x, max_y, min_y))

display = [[' '] * (max_x - min_x + 1) for i in range(max_y - min_y + 1)]
for (x, y, vel_x, vel_y) in points:
    display[y + (vel_y * bestSec) - min_y][x + (vel_x * bestSec) - min_x] = '#'


for row in display:
    print(''.join(row))
print("\n--- %s seconds ---" % (time.time() - start_time))