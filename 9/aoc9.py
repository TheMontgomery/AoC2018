from collections import defaultdict, deque
import time

start_time = time.time()
workingDir = "G:/Python/adventofcode2018/9/"
USE_EXAMPLE = False
#scores = defaultdict(int)

with open(workingDir + "input") as inFile:
    line = inFile.read().split()
    numPlayers = int(line[0])
    lastMarble = int(line[6])
    inFile.close()

print("numPlayers:{0}\tlastMarble:{1}\n".format(numPlayers, lastMarble))

def solve(numPlayers, lastMarble):
    scores = defaultdict(int)
    circle = deque([0])
    player = 0
    current = 0
    for i in range(1, lastMarble+1):

        # If any remainder, proceed with placing
        # Rotate the whole circle counterclockwise by 1, then place marble.
        if i % 23:
            circle.rotate(-1)
            circle.append(i)
            current = i
        else:
            print("\tScore!")
            circle.rotate(7)
            #circle.append(i)
            addScore = circle.pop()
            print("\tPlayer {0} will receive {1} + {2} points".format(player, addScore, i))
            scores[player] += addScore + i
            circle.rotate(-1)
            current = circle[-1]
        #print("[{0}]\t{1}".format(player+1, circle))
        #print("Curent marble: {0}".format(current))
        #print("Current marble:", current, "   Position:", circle.index(current),"\n")
        player += 1
        player %= numPlayers

    highScore = max(scores.values())
    winner = max(scores.keys(), key=lambda x: scores[x])
    return highScore, winner

# ----- PART 1 -----
# Identify highest score after all marbles are placed.
highScore, winner = solve(numPlayers, lastMarble)
#print("\nPart 1:\tHighest score:", max(scores.values()), "\tWinning player:", max(scores.keys(), key=lambda x: scores[x]))
print("\nPart 1:\t Highest score: {0}\tWinning player: {1}".format(highScore, winner))
print("--- %s seconds ---" % (time.time() - start_time))


# ---- PART 2 ----
# Need to find the high score if the last marble were 100 times larger?
start_time = time.time()
highScore, winner = solve(numPlayers, lastMarble * 100)
print("\nPart 2:\t Highest score: {0}\tWinning player: {1}".format(highScore, winner))
print("--- %s seconds ---" % (time.time() - start_time))