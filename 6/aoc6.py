from collections import defaultdict
import time

workingDir = "G:/Python/adventofcode2018/6/"
manhattanThreshold = 10000
areas = defaultdict(int)
infinite_points = set()
points = set()
pointIds = {}
max_x = max_y = 0
min_x = min_y = 0
start_time = time.time()
#coords = {} # defaultdict(list)
with open(workingDir + 'input') as inFile:
    i = 0
    for line in inFile:
        # Store each set of coordinates as a Tuple (x, y)
        # Update the maximum X and Y values with each point to avoid duplicate effort ;)
        x, y = map(int, line.rstrip().split(", "))
        # print("line:", line, "x:", x, "y:", y)
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
        points.add((x, y))
        pointIds.update({i: (x,y)})
        i += 1
    inFile.close()

#print(pointIds)

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
    d_min = None

    for point in arr:
        d = distance(p, point)
        if not nearest:
            nearest = point
            d_min = d
        else:
            if d < d_min:
                nearest = point
                d_min = d
            elif d == d_min:
                nearest = None
                break
    return nearest


# Determine if point extends to infinity
def is_finite(p):
    return min_x < p[0] < max_x and min_y < p[1] < max_y


# ----- PART 1 -----
# Find the "area" (total number of squares) for all points that don't extend to infinity
# Use the Manhattan Distance to find the closest point to each location in the grid
d_sum_under_min = 0         # Sum of distances < 10000 for part 2
for i in range(max_x + 1):
    for j in range(max_y + 1):
        # d = min(points, key=lambda r: distance((i, j), r))
        # d = sorted([distance((i,j), point),  for point in points])
        d = sorted([(distance((i,j), point), pointId) for pointId, point in pointIds.items()])
        # print(d)
        # print(sum(pair[0] for pair in d))

        if len(d) == 1 or d[0][0] != d[1][0]:
            pointId = d[0][1]
            areas[pointId] += 1

            if i == 0 or i == max_x or j == 0 or j == max_y:
                infinite_points.add(pointId)

        # For part 2; find sum of distances; if under threshold (32 for test, 10000 for real set), increment area
        if sum(pair[0] for pair in d) < manhattanThreshold:
            d_sum_under_min += 1
        #areas[d] += 1
        #if d: areas[d] += 1
        # print(f"Position: ({i}, {j}) \tNearest point: {d}")

# for i, area in areas.items():
#     if i not in infinite_points:
#         print("pointId:", i, "Area:", area)

#         return max(size for coord_id, size in region_sizes.items() if coord_id not in infinite_ids)
#bestPoint, bestArea = max(pointId, area in areas.items() if pointId not in infinite_points)
#pointId = max(i in areas.items() if i not in infinite_points, key=lambda x: x[1])
#pointId = max(area for area, point in areas.items() if point not in infinite_points)
# print(areas, areas.keys(), areas.items())
# print(filter(lambda y: y not in infinite_points, areas))
# pointId = max(filter(lambda y: y not in infinite_points, areas.items()), key=lambda x: x[1])
# print(max((size, pointId) for pointId, size in areas.items() if pointId not in infinite_points))

pointId = max((size, pointId) for pointId, size in areas.items() if pointId not in infinite_points)[1]
#print(max(areas.items(), key=lambda x: x[1] if x[0] not in infinite_points))

print("Part 1 Solution:\nCoordinates:", pointIds[pointId], "\nArea:", areas[pointId])
print("--- %s seconds ---" % (time.time() - start_time))


# ----- PART 2 -----
# Find a "region" closest to as many points as possible
# E.g., need to find the sum of Manhattan distances to all points, get the
start_time = time.time()

print("Part 2 Solution:\n", d_sum_under_min)
print("--- %s seconds ---" % (time.time() - start_time))