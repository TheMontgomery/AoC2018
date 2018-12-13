from collections import defaultdict

workingDir = "G:/Python/adventofcode2018/7/"

stepsMaster = set()
prereqs = defaultdict(set)
stepOrder = ''
# Read the steps, and extract the prerequisite step, along with the step.
# Sample format:
# Step C must be finished before step A can begin.
#
# Where "C" is the prerequisite, and A is the next step
# Some steps will not have prerequisites, hence need to have master set of all steps
with open(workingDir + 'input') as inFile:
    for line in inFile:
        prereq, step = line.rstrip().split(" ")[1:9:6]
        stepsMaster.add(step)
        stepsMaster.add(prereq)
        prereqs[step].add(prereq)
    inFile.close()

# Convert set of steps to sorted list, as we need to evaluate alphabetically
steps = sorted(stepsMaster)
print(steps)
while steps:
    for step in steps:
        parents = sorted(prereqs[step])

        # Check if parents is empty, OR if ALL parents are already complete
        step_complete = (len(parents) == 0) or all(prereq in stepOrder for prereq in parents)
        # print("step_complete:", step_complete)

        if step_complete:
            stepOrder += step
            steps.remove(step)
            break

print("Part 1:", stepOrder)

# ----- PART 2 -----
#
# 4 Elves offer to help build. Each step takes 60+1/letter seconds (e.g. A = 61 seconds, C = 63, etc.)
# Each worker can work on 1 step at a time, and simultaneously-available steps should be done alphabetically.
# Need to find total time for completion, as well as the new order of steps.
# Stated sequence of steps and prerequisites is still the same.

from string import ascii_uppercase as alpha
NUM_WORKERS = 5
BASE_TIME = 61


workers = defaultdict(list)
steps = sorted(stepsMaster)
stepOrder = []
timeElapsed = 0
# Populate workerTime and workerTask per NUM_WORKERS
for i in range(NUM_WORKERS):
    workers[i] = None

def timeNeeded(step):
    offset = alpha.find(step)
    return BASE_TIME + offset

inProgress = set()
#for i in range(6):
while steps or any(workers.values()):
    #print("\nCurrent second: ", timeElapsed)

    # Assign tasks if available.
    for worker in workers:
        # Check if worker is assigned
        print("worker:", worker, "workers[worker]:", workers[worker])
        if workers[worker]:
            currentTask, workTime = workers[worker]
            workTime -= 1
            print("Current task:", currentTask, "Time remaining:", workTime)
            if workTime == 0:
                print("Task {0} complete by worker {1}".format(currentTask, worker))
                inProgress.remove(currentTask)
                stepOrder.append(currentTask)
                steps.remove(currentTask)
                workers[worker] = None
                print("Current sequence:", ''.join(stepOrder))
            else:
                workers[worker] = [currentTask, workTime]
        else:
            # If worker is available, find the appropriate available task
            available = sorted(set(steps).difference(inProgress))
            for step in available:
                parents = sorted(prereqs[step])
                #print("Available: ", available)
                if len(parents) == 0 or all(prereq in stepOrder for prereq in parents):
                    print("Best available:", step, "Time needed:", timeNeeded(step), "worker ID:", worker)
                    inProgress.add(step)
                    workers[worker] = [step, timeNeeded(step)]
                    break
            #print("available steps:", available)
            #workers[worker] = (,0)

    # Make a second pass of the assigned workers, and decrement the task time
    for worker in workers:
        if workers[worker]:
            currentTask, workTime = workers[worker]
            workTime -= 1
            print("Current task:", currentTask, "Time remaining:", workTime)
            if workTime == 0:
                print("Task {0} complete by worker {1}".format(currentTask, worker))
                inProgress.remove(currentTask)
                stepOrder.append(currentTask)
                steps.remove(currentTask)
                workers[worker] = None
                print("Current sequence:", ''.join(stepOrder))
    print("Current second: ", timeElapsed, "\n")
    timeElapsed += 1

print("\nPart 2: ", ''.join(stepOrder))
print("Time elapsed: {0} seconds".format(timeElapsed))
    # for step in steps:
    #     parents = sorted(prereqs[step])
    #
    #     # Check if any workers are available:
    #     if not all(workerTime.values()):
    #         # Check that current step not yet assigned:
    #         if step not in inProgress:
    #             # Get an available worker ID
    #             workerId = min(i for i in workerTime if workerTime[i] == 0)
    #             print("workerId:", workerId)
    #             workerTime[workerId] = timeNeeded(step)
    #             workerTask[step] = workerId
    #             inProgress.add(step)
    #
    #     # Get workerId for current step, if any:
    #     workerId = workerTask[step]
    #
    #     # Check if parents is empty, OR if ALL parents are already complete
    #     step_complete = (len(parents) == 0) or all(prereq in stepOrder for prereq in parents)
    #     step_complete = step_complete and workerTime[workerId] == 0
    #     # print("step_complete:", step_complete)
    #
    #     timeElapsed += 1
    #     if step_complete:
    #         stepOrder += step
    #         steps.remove(step)
    #         inProgress.remove(step)
    #         workerTask[step] = None
    #         break