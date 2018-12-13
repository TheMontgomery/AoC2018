from collections import defaultdict

workingDir = "G:/Python/adventofcode2018/7/"

steps = set()
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
        steps.add(step)
        steps.add(prereq)
        prereqs[step].add(prereq)
    inFile.close()


print("prereqs:", prereqs)
print("steps:", steps)
print("len steps:", len(steps))
print("len prereqs:", len(prereqs))

# Convert set of steps to sorted list, as we need to evaluate alphabetically
steps = sorted(steps)
print(steps)
while steps:
    for step in steps:
        parents = sorted(prereqs[step])
        # print("\nstep:", step, "parents:", parents)
        # print("len(parents):", len(parents))
        # print("len(stepOrder):", len(stepOrder))

        # Check if parents is empty, OR if ALL parents are already complete
        step_complete = (len(parents) == 0) or all(prereq in stepOrder for prereq in parents)
        # print("step_complete:", step_complete)

        if step_complete:
            stepOrder += step
            steps.remove(step)
            break

print("Part 1:", stepOrder, steps)

