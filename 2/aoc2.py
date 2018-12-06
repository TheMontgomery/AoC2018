from collections import Counter, defaultdict
from itertools import combinations

# Need to find IDs with exactly 2 or 3 counts of the any one letter.
workingDir = "G:/Python/adventofcode2018/2/"
twoChars, threeChars = 0, 0
boxIds = defaultdict(str)

# Read each box ID into a defaultdict
with open(workingDir + "input") as inFile:
    boxIds = [line.strip() for line in inFile]
    inFile.close()

# Part 1:
# Find all box IDs that contain exactly 2 or exactly 3 of any one character.
# Then, compute a checksum, of the number of 2-count IDs multiplied by the number of 3-count IDs.
for box in boxIds:
    found2 = False
    found3 = False
    charCount = Counter(box)
    #print("Box ID: ", box, "\t", charCount)

    for letter in charCount:
        if charCount[letter] == 2:
            found2 = True
        if charCount[letter] == 3:
            found3 = True

    if found2:
        twoChars += 1
    if found3:
        threeChars += 1

print("\n\nBoxes with exactly 2 duplicate chars: ", twoChars)
print("Boxes with exactly 3 duplicate chars: ", threeChars)
print("\nChecksum : ", twoChars * threeChars)


# Part 2:
# Box IDs are strings of 26 characters long. Need to find two box IDs that differ by only 1 character.
# E.G., 25 of 26 characters should be in the same position.
# The answer to submit will be the characters that the two Box IDs have in common.

# Use itertools combinations to get all possible pairs of box IDs
for box1, box2 in combinations(boxIds, 2):
    #print(box1, ",", box2)

    # Box IDs should be same length, but just in case, we'll only match across the minimum length
    #minLen = min(len(box1), len(box2))
    # If common chars are 1 less than total length of boxID, we have a match!
    #commonChars = [i for i,j in zip(box1,box2) if i == j]
    commonChars = list()
    for i,j in zip(box1,box2):
        if i == j:
            commonChars.append(i)
    if len(box1) - len(commonChars) == 1:
        print("Found box IDs:\n", box1, "\n", box2)
        print("Common characters:", "".join(commonChars))
        break

