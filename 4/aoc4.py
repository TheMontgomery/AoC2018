import datetime
import re
from collections import defaultdict

workingDir = "G:/Python/adventofcode2018/4/"

# ----- PART 1 -----
# Input file is an unsorted list of date/timestamps, each logging an action (guard starts shift, falls asleep, wakes up)
# Need to sort the inputs chronologically, then parse out w
# Example lines :
# [1518-06-18 00:04] Guard #859 begins shift
# [1518-06-26 00:38] falls asleep

# Takes an input file, reads it into a list, and then sorts by date.
# Returns sorted list
def sort_date_time(file_path):
    with open(file_path) as infile:
        log_entries = []
        date_pattern = r'(\d\d\d\d)-(0?[0-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01]) (00|0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])'
        for record in infile:

            timestamp, _, log_event = record.partition("] ")
            log_datetime = datetime.datetime()
            print(timestamp, " ", log_event)
            #timestamp =
            #year, month, day, hour, minute = re.compile(date_pattern).match(record).groups()
            #print("year: ", year, " month: ", month, " day: ", day, " hour: ", hour, " minute: ", minute)
            #print(record)
            #print("Date: ", log_date, " Time: ", log_time, " Detail: ", log_event)


sort_date_time(workingDir + "input2")