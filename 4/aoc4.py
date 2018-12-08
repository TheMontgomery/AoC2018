from datetime import datetime
from collections import defaultdict

workingDir = "G:/Python/adventofcode2018/4/"
dateFormat = "%Y-%m-%d %H:%M"


# ----- PART 1 -----
# Input file is an unsorted list of date/timestamps, each logging an action (guard starts shift, falls asleep, wakes up)
# Need to sort the inputs chronologically, then parse out w
# Example lines :
# [1518-06-18 00:04] Guard #859 begins shift
# [1518-06-26 00:38] falls asleep

# Takes an input file, reads it into a list, and then sorts by date.
# Returns sorted list
def sortDateTime(file_path):
    with open(file_path) as infile:
        log_entries = infile.read().splitlines()
        log_entries.sort()
        # print(log_entries)
        return log_entries


# Record the frequency of each minute in the midnight hour asleep, indexed by guard ID
guards = defaultdict(list)
# Record each guard's total minutes asleep, indexed by guard ID
timeAsleep = defaultdict(int)

records = sortDateTime(workingDir + "input2")
for record in records:
    timestamp, guardAction = record.split("] ")

    if "Guard #" in guardAction:
        # Parse guard ID, add to dictionary
        guardId = int(guardAction.split()[1].replace("#", ""))
        print("guardID: ", guardId)
    elif "falls asleep" in guardAction:
        # Get start time for sleep
        sleepStart = datetime.strptime(timestamp.replace("[", ""), dateFormat)
        print("Guard sleep start:", sleepStart.minute)
    elif "wakes up" in guardAction:
        # Get end time for sleep, record total minutes asleep
        sleepEnd = datetime.strptime(timestamp.replace("[", ""), dateFormat)
        print("Guard sleep end:", sleepEnd.minute)
        timeAsleep[guardId] += sleepEnd.minute - sleepStart.minute
        print("Guard #", guardId, "total time asleep: ", timeAsleep[guardId])
        guards[guardId].append((sleepStart.minute, sleepEnd.minute))
