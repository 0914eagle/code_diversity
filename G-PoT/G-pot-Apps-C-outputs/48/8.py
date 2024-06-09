
# Read input
top_row = input().split()
bottom_row = input().split()

# Initialize variables
solutions = set()
unknowns = []

# Find unknowns and store their indices
for i in range(10):
    if top_row[i] == '_':
        unknowns.append((0, i))
    if bottom_row[i] == '_':
        unknowns.append((1, i))

# Generate all possible combinations for unknowns
for combo in range(10 ** len(unknowns)):
    combo_str = str(combo).zfill(len(unknowns))
    values = [int(combo_str[j]) for j in range(len(unknowns))]

    # Fill in unknowns with values from current combination
    for idx, (row, col) in enumerate(unknowns):
        if row == 0:
            top_row[col] = str(values[idx])
        else:
            bottom_row[col] = str(values[idx])

    # Check if current combination is consistent
    consistent = True
    for i in range(5):
        if top_row[2*i] != '_' and top_row[2*i+1] != '_':
            ratio = int(top_row[2*i]) / int(top_row[2*i+1])
            for j in range(5):
                if j != i:
                    if top_row[2*j] == '_':
                        top_row[2*j] = str(int(top_row[2*j+1]) * ratio)
                    elif top_row[2*j+1] == '_':
                        top_row[2*j+1] = str(int(top_row[2*j]) / ratio)

        if bottom_row[2*i] != '_' and bottom_row[2*i+1] != '_':
            ratio = int(bottom_row[2*i]) / int(bottom_row[2*i+1])
            for j in range(5):
                if j != i:
                    if bottom_row[2*j] == '_':
                        bottom_row[2*j] = str(int(bottom_row[2*j+1]) * ratio)
                    elif bottom_row[2*j+1] == '_':
                        bottom_row[2*j+1] = str(int(bottom_row[2*j]) / ratio)

    # Check if all entries are positive integers
    for entry in top_row + bottom_row:
        if entry != '_' and int(entry) <= 0:
            consistent = False
            break

    # If consistent, add solution to set
    if consistent:
        solutions.add(tuple(top_row + bottom_row))

# Output number of distinct solutions
if len(solutions) == 0:
    print("many")
else:
    print(len(solutions))
