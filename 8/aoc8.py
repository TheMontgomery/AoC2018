from collections import defaultdict
#import networkx as nx

workingDir = "G:/Python/adventofcode2018/8/"
USE_EXAMPLE = False
HEADER_LENGTH = 2

with open(workingDir + 'input2') as inFile:
    master = [int(n) for n in inFile.read().split(' ')]
    inFile.close()

print(master)
meta = defaultdict(list)
children = defaultdict(list)
payloads = defaultdict(list)
i = 0

# Function to parse the "tree"
# Input: List, of integers (a subset of the master list)
# Returns: Sum of metadata, value of metadata
def getData(inputList):
    numChildren, numMeta = inputList[:HEADER_LENGTH]

    print("child nodes: {0} metadata entries: {1}".format(numChildren, numMeta))

    metadata = inputList[-numMeta:]
    print("metadata:", metadata)
    print("length of header + metadata:", len(inputList[:2] + metadata))
    payload = inputList[2:-numMeta]
    print("payload:", payload)

    if numChildren == 0:
        return sum(metadata)
    # Evaluate each child
    for child in range(numChildren):
        return getData(payload)


getData(master)