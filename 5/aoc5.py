from collections import defaultdict, Counter
workingDir = "G:/Python/adventofcode2018/5/"

# Advent of Code 2018, Day 5
# Alchemical Reduction
# Input is a string representing a polymer; units of the same type & opposite polarity will react and destroy each other
# Example: aA  -> React, destroy
# Example: AA  -> Inert, nothing happens

# ----- PART 1 -----
# After all possible reactions, find total length of polymer.
with open(workingDir + "input3") as inFile:
    rawPolymer = inFile.read()
    inFile.close()

print(rawPolymer)
print(len(rawPolymer))

def opposite(a, b):
    return (a.lower() == b.lower() and a.swapcase() == b)


def polReduce(polymer):
    buffer = []

    for i, element in enumerate(polymer):

        if i == 0:
            buffer.append(element)              # Add each character
        #print(i, element, polymer[i-1])
        elif i > 0:                             # If previous character exists...
            #print(element, polymer[i-1], buffer[-1])
            if opposite(element, buffer[-1]):   # If polarities oppose, remove previous char, and continue
                #print("Opposite detected")
                buffer.pop()
            else:
                buffer.append(element)
        #print(buffer)

    #print(''.join(buffer))
    return ''.join(buffer)

reduced = polReduce(rawPolymer)

print("Length of original:", len(rawPolymer))
print("Reduced polymer:", reduced)
print("Reduced length:", len(reduced))
