from collections import defaultdict, Counter
workingDir = "G:/Python/adventofcode2018/5/"

# Advent of Code 2018, Day 5
# Alchemical Reduction
# Input is a string representing a polymer; units of the same type & opposite polarity will react and destroy each other
# Example: aA  -> React, destroy
# Example: AA  -> Inert, nothing happens

# ----- PART 1 -----
# After all possible reactions, find total length of polymer.
with open(workingDir + "input") as inFile:
    rawPolymer = inFile.read().strip("\n")
    inFile.close()


def opposite(a, b):
    return (a.lower() == b.lower() and a.swapcase() == b)


def polReduce(polymer):
    buffer = []

    for i, element in enumerate(polymer):

        if i == 0:
            buffer.append(element)              # Add each character
        #print(i, element, polymer[i-1])
        elif i > 0:                             # If previous character exists...
            #print(element, len(buffer), buffer[-1])
            if len(buffer) and opposite(element, buffer[-1]):   # If opposite, remove previous char & don't append new
                #print("Opposite detected")
                buffer.pop()
            else:
                buffer.append(element)

    return ''.join(buffer)

reduced = polReduce(rawPolymer)

print("Length of original:", len(rawPolymer))
print("Reduced polymer:", reduced)
print("Reduced length:", len(reduced))


# ----- PART 2 -----
# Need to find which element type can be removed to produce the minimum reduced polymer size

unitreduce = defaultdict(int)
alpha = 'abcdefghijklmnopqrstuvwxyz'

def polReduceUnit(polymer, letter):
    p = polymer.replace(letter.lower(), '')
    p = p.replace(letter.upper(), '')
    return polReduce(p)

for letter in alpha:
    reduced = polReduceUnit(rawPolymer, letter)
    #print("letter:", letter, "\tlength:", len(reduced), "\treduced:", reduced)
    unitreduce[letter] = len(reduced)

print("Optimal letter:", min(unitreduce.items(), key=lambda i: i[1]))

