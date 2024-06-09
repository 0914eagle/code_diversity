
# Read input
top_row = input().split()
bottom_row = input().split()

# Initialize counter for distinct solutions
count = 0

# Loop through all possible values for the empty slots
for burger in range(1, 201):
    for slop in range(1, 201):
        for sushi in range(1, 201):
            for drumstick in range(1, 201):
                # Check if the values satisfy the proportions
                if top_row.count('_') == 2:
                    prop_ratio = (burger + slop) / (sushi + drumstick)
                    if (int(top_row[0]) + int(top_row[1])) / (int(bottom_row[0]) + int(bottom_row[1])) == prop_ratio:
                        count += 1
                elif top_row.count('_') == 3:
                    prop_ratio = (burger + slop) / (sushi + drumstick)
                    if (int(top_row[1]) + int(top_row[3])) / (int(bottom_row[1]) + int(bottom_row[3])) == prop_ratio:
                        count += 1

# Output the number of distinct solutions
print(count if count > 0 else "many")
