from collections import defaultdict
__author__ = "Monty Secor"
# Starting frequency of 0; will accumulate all input lines for net frequency change
intFreqSum = 0
intIterations = 0
boolFreqFound = False                           # Starting condition, not found
workingDir = "G:/Python/adventofcode2018/1/"

# Store all frequency totals
listFrequencies = []
listNetFreq = set()

# Store all input file entries in a list, to iterate over later:
with open(workingDir + "input") as inputFile:
        listFrequencies = list(line.rstrip() for line in inputFile)
        print("Initial load complete. Number of lines:" + str(len(listFrequencies)))

while not boolFreqFound:
        for frequency in listFrequencies:
                intFreqSum += int(frequency)
                if intFreqSum not in listNetFreq:
                        listNetFreq.add(intFreqSum)
                else:
                        print("First repeating frequency: " + str(intFreqSum))
                        print("Iterations: " + str(intIterations))
                        boolFreqFound = True
                        break
        intIterations += 1
        print("Current net frequency: " + str(intFreqSum))