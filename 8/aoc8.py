from collections import defaultdict
from string import ascii_uppercase as alpha
#import networkx as nx

workingDir = "G:/Python/adventofcode2018/8/"
USE_EXAMPLE = False

with open(workingDir + 'input') as inFile:
    master = [int(n) for n in inFile.read().split(' ')]
    inFile.close()

print(master)


def getData(i=0):
    #numChild, numMeta = [inputList.pop(0) for i in range(2)]
    numChild = master[i]
    numMeta = master[i + 1]
    children = defaultdict(int)
    i += 2
    metaSum, valueSum = 0, 0

    print("numChildren: {0}\tnumMeta: {1}\tpayload: {2}".format(numChild, numMeta, master[i:]))

    if numChild == 0:
        for n in range(numMeta):
            meta = master[i]
            metaSum += meta
            valueSum += meta
            i += 1
        print("No child nodes; returning:\ti: {0}\tmetaSum:{1}\tvalueSum:{2}".format(i, metaSum, valueSum))
        return i, metaSum, valueSum

    for n in range(numChild):
        i, val, meta = getData(i)
        children[n] = meta
        print("child n: {0}\tpos: {1}\tval: {2}\tchildren[n]: {3}\tmeta: {4}".format(n, i, val, children[n], meta))
        metaSum += val

    print("Current position: {0}\tmetaSum:{1}\tmaster[i]:{2}".format(i, metaSum, master[i]))
    #print("Contents of children:", dict(children))

    for n in range(numMeta):
        meta = master[i]
        metaSum += meta
        print("Metadata index: {0}\tMetadata value:{1}\tchildren[n]: {2}".format(n, meta, children[meta-1]))
        # try:
        #     valueSum += children[n-1]
        #     print("Metadata value: {0}\t Child value:{1}".format(master[i], children[meta]))
        # except IndexError:
        #     valueSum +=0

        valueSum += children[meta-1]
        #valueSum += children[meta]
        i += 1

    return i, metaSum, valueSum




_, metaSum, valueSum = getData()

# ----- PART 1 ------
# Display the sum of all metadata entries.

print("Part 1\tSum of metadata:", metaSum)

# ----- PART 2 -----
# Need to display the total "value" of all nodes.
# A node only has value if it has children; each node's metadata value points to a child node index.
# Value is only accrued if the metadata points to an existing child node of the given node.

print("Part 2\tTotal value:", valueSum)