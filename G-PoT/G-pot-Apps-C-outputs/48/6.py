
# Read input
top_row = list(map(lambda x: int(x) if x != '_' else None, input().split()))
bottom_row = list(map(lambda x: int(x) if x != '_' else None, input().split()))

# Initialize variables
solutions = set()
proportions = []

# Calculate proportions for each monster
for i in range(5):
    for j in range(i+1, 5):
        if top_row[i] is not None and top_row[j] is not None:
            proportion = top_row[i] / top_row[j]
            proportions.append((i, j, proportion))
        if bottom_row[i] is not None and bottom_row[j] is not None:
            proportion = bottom_row[i] / bottom_row[j]
            proportions.append((i, j, proportion))

# Generate all possible solutions
for i in range(1, 201):
    valid = True
    current_top_row = top_row.copy()
    current_bottom_row = bottom_row.copy()
    
    for a, b, proportion in proportions:
        if current_top_row[a] is None and current_top_row[b] is not None:
            current_top_row[a] = current_top_row[b] * proportion
        elif current_top_row[b] is None and current_top_row[a] is not None:
            current_top_row[b] = current_top_row[a] / proportion
        
        if current_bottom_row[a] is None and current_bottom_row[b] is not None:
            current_bottom_row[a] = current_bottom_row[b] * proportion
        elif current_bottom_row[b] is None and current_bottom_row[a] is not None:
            current_bottom_row[b] = current_bottom_row[a] / proportion
        
        if current_top_row[a] != int(current_top_row[a]) or current_top_row[b] != int(current_top_row[b]) or current_bottom_row[a] != int(current_bottom_row[a]) or current_bottom_row[b] != int(current_bottom_row[b]):
            valid = False
            break
    
    if valid:
        solutions.add((tuple(map(int, current_top_row)), tuple(map(int, current_bottom_row)))

# Output the number of distinct solutions
if len(solutions) == 0:
    print("many")
else:
    print(len(solutions))
