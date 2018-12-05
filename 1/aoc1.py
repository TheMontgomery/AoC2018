
# Starting frequency of 0; will accumulate all input lines for net frequency change
freqSum = "0"
workingDir = "G:/Python/adventofcode2018/1/"

# Each line of the file is a string beginning with + or -, followed by an integer
inputFile = open(workingDir + "input")
for line in inputFile:
        freqSum = freqSum + line.rstrip()                # Concatenate all lines, remove newline

# Once all numbers with +/- signs are appended, evaluate to get the total:
print(eval(freqSum))