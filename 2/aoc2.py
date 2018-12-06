from difflib import SequenceMatcher
from collections import Counter, defaultdict

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
    print("Box ID: ", box, "\t", charCount)

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