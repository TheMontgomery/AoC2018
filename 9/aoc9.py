from collections import defaultdict
#import networkx as nx

workingDir = "G:/Python/adventofcode2018/9/"
USE_EXAMPLE = False

with open(workingDir + "input2") as inFile:
    line = inFile.read().split()
    numPlayers = int(line[0])
    lastMarblePts = int(line[6])
    inFile.close()

print("numPlayers:{0}\tlastMarblePts:{1}".format(numPlayers, lastMarblePts))