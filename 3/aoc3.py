import re

# Defines the total cloth, 1000x1000 inches
CLOTHSIZE = 1000
cloth = []
for _ in range(CLOTHSIZE):
    cloth.append([0 for _ in range(CLOTHSIZE)])

workingDir = "G:/Python/adventofcode2018/3/"
# ------ PART 1 ------
# Input provides a list of claims for fabric (1000 x 1000 inches)
# Need to find total area of overlapping claims
# Format of input line:
#26 @ 594,575: 24x15
#id @ xPos,yPos: lenXheight


# Read each line of the file, parse into integers.
# Input:    line (string)
# Returns:  5-element Tuple of Integers: (id, x, y, width, height)
def parseLine(line):
    return(int(i) for i in re.findall(r'\d+', line))

with open(workingDir + "input") as inFile:
    #claims = [line.strip() for line in inFile]
    claims = []
    for record in inFile:
        claims.append(parseLine(record.strip()))
    inFile.close()


for claim in claims:
    claimId, x, y, width, height = claim
    #rint("ID:\t" , claimId, "\nX:\t", x, "\nY:\t", y, "\nWidth:\t", width, "\nHeight:\t", height)
    #claimAreas.append((x, y , width, height))

    # Iterate over each claimed area; increment corresponding coordinate values in the global cloth
    for i in range(x, x + width):
        for j in range (y, y + height):
            cloth[i][j] += 1

# Finally, iterate over the global cloth, and sum any coordinates with more than 1 claim
# for row in cloth:
#     for col in row:
#         if col > 1:
#             overlap.append(col)
# for row in cloth:
#     print(row)

overlap = [col for row in cloth for col in row if col > 1]
print("Total area of overlap: ", len(overlap))

# ----- PART 2 -----
# From the claims in the input, we are given that only ONE claim does not overlap any others
# Need to identify it with the claimId somehow
with open(workingDir + "input") as inFile:
    #claims = [line.strip() for line in inFile]
    claims = []
    for record in inFile:
        claims.append(parseLine(record.strip()))
    inFile.close()

for claim in claims:
    #print(list(claim))
    claimId, x, y, width, height = claim
    noOverlap = True
    for i in range(x, x + width):
        for j in range(y, y + height):
            if cloth[i][j] > 1:
                noOverlap = False

    if noOverlap:
        print("ClaimId without overlap: ", claimId)