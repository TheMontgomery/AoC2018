from collections import defaultdict

workingDir = "G:/Python/adventofcode2018/7/"

steps = defaultdict(set)
prereqs = defaultdict(set)
stepOrder = ''
# Read the steps, and extract the prerequisite step, along with the step.
# Sample format:
# Step C must be finished before step A can begin.
#
# Where "C" is the prerequisite, and A is the next step
with open(workingDir + 'input2') as inFile:
    for line in inFile:
        prereq, step = line.rstrip().split(" ")[1:9:6]
        steps[prereq].add(step)
        prereqs[step].add(prereq)
    inFile.close()


print("prereqs:", prereqs)
print("steps:", steps)
# InOrder traversal of the list of steps, defaultdict should mimic Binary Search Tree
# Accepts List argument, named subtree
def inOrder(subtree):
    stack = []
    if len(subtree) == 1:
        stack.append(subtree[0])
    else:
        stack = inOrder(subtree[1:])

for step in steps:
    print(step, sorted(steps[step]))
    # Get list of all child steps
    children = sorted(steps[step])

    # If the current step is not in the order, add it
    if step not in stepOrder:
        stepOrder.append(step)

    # If current step has only 1 child, append the child step; else, do breadth-first search
    if len(children) == 1:
        stepOrder.append(children[0])
    elif len(children) > 1:
        stepOrder.pop()
        print(inOrder(children))

print("Part 1:", stepOrder)

