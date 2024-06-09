
# Read input
top_row = input().split()
bottom_row = input().split()

# Initialize variables
unknowns = []
knowns = []
proportions = []

# Separate known and unknown entries
for entry in top_row + bottom_row:
    if entry == '_':
        unknowns.append(0)
    else:
        knowns.append(int(entry))

# Calculate proportions
for i in range(5):
    for j in range(i+1, 5):
        if knowns[i] != 0 and knowns[j] != 0:
            proportions.append(knowns[i] / knowns[j])

# Count distinct solutions
if len(proportions) == 0:
    print("many")
else:
    distinct_solutions = set()
    for i in range(1, 201):
        valid_solution = True
        for j in range(5):
            if top_row[j] == '_':
                if i * proportions[j] not in range(1, 201):
                    valid_solution = False
                    break
            if bottom_row[j] == '_':
                if i not in range(1, 201):
                    valid_solution = False
                    break
        if valid_solution:
            distinct_solutions.add(i)
    print(len(distinct_solutions))
