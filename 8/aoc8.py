from collections import defaultdict
from string import ascii_uppercase as alpha
#import networkx as nx

workingDir = "G:/Python/adventofcode2018/8/"
USE_EXAMPLE = False
HEADER_LENGTH = 2

with open(workingDir + 'input2') as inFile:
    master = [int(n) for n in inFile.read().split(' ')]
    inFile.close()

print(master)

# Function to parse the "tree"
# Input: List, of integers (a subset of the master list)
# Returns: Sum of metadata, value of metadata
def getData(inputList):
    numChildren, numMeta = inputList[:HEADER_LENGTH]
    sumMeta = 0

    print("\nEnter getData. numChildren: {0}\tnumMeta:{1}".format(numChildren, numMeta))
    print("inputList:", inputList)

    if numChildren > 0:
        payload = inputList[HEADER_LENGTH:-numMeta]
        print("payload:", payload)
        for n in range(numChildren):
            #print(getData(payload))
            sumMeta += getData(payload)
    elif numChildren == 0:
        print("no child nodes. Sum of metadata:", sum(inputList[-numMeta:]))
        sumMeta += sum(inputList[-numMeta:])
    # print("\nchild nodes: {0} metadata entries: {1}".format(numChildren, numMeta))
    # print("metadata:", metadata)
    # print("length of header + metadata:", len(inputList[:HEADER_LENGTH] + metadata))
    # payload = inputList[HEADER_LENGTH:-numMeta]
    # print("payload:", payload)

    return sumMeta

sumMeta = getData(master)

# ----- PART 1 ------
# Display the sum of all metadata entries.
print("Sum of metadata:", sumMeta)