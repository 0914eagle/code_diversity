
# Read input
top_row = input().split()
bottom_row = input().split()

# Initialize a counter for solutions
solution_count = 0

# Loop through all possible values for the missing entries
for burger in range(1, 201):
    for slop in range(1, 201):
        for sushi in range(1, 201):
            for drumstick in range(1, 201):
                # Check if the values satisfy the proportions
                if top_row.count('_') == 2:
                    prop_ratio = (burger + slop) / (sushi + drumstick)
                    if (int(top_row[0]) + int(top_row[1])) / (int(bottom_row[0]) + int(bottom_row[1])) == prop_ratio:
                        solution_count += 1
                elif top_row.count('_') == 1:
                    if top_row[0] == '_':
                        prop_ratio = slop / drumstick
                        if int(top_row[1]) / int(bottom_row[1]) == prop_ratio:
                            solution_count += 1
                    else:
                        prop_ratio = burger / sushi
                        if int(top_row[0]) / int(bottom_row[0]) == prop_ratio:
                            solution_count += 1

# Output the number of distinct solutions
if solution_count == 0:
    print("many")
else:
    print(solution_count)
