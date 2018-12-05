import os.path
import ctypes
__author__ = "Monty Secor"
# Starting frequency of 0; will accumulate all input lines for net frequency change
freqSum = "0"
intFreqSum = 0
boolFreqFound = False
workingDir = "G:/Python/adventofcode2018/1/"

# Store all frequency totals
listFrequencies = []

# Each line of the file is a string beginning with + or -, followed by an integer
inputFile = open(workingDir + "input")
for line in inputFile:
        freqSum = freqSum + line.rstrip()                # Concatenate all lines, remove newline
        intFreqSum = eval(freqSum)

        if line not in

        if intfreqSum in listFrequencies:
                print("Repeating frequency: " + str(intfreqsum))
                boolFreqFound = True
                break
        else:
                listFrequencies.append(intFreqSum)

while not boolFreqFound:
        for freq in listFrequencies:
                freqSum = freqSum + freq
                intFreqSum = eval(freqSum)

                if intFreqSum in


# Once all numbers with +/- signs are appended, evaluate to get the total:
print(eval(freqSum))
#ctypes.windll.user32.MessageBoxW(0, "Frequency result: " + eval(freqSum), "Frequency Shift", 0)