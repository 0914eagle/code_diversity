
# Read input
top_row = input().split()
bottom_row = input().split()

# Initialize variables
num_solutions = 0

# Loop through possible values for the missing entries
for burger in range(1, 201):
    for slop in range(1, 201):
        for sushi in range(1, 201):
            for drumstick in range(1, 201):
                # Check if the values satisfy the proportions
                if top_row.count('_') == 2:
                    prop_ratio = (burger + slop) / (sushi + drumstick)
                    if (int(top_row[0]) + int(top_row[1])) / (int(top_row[2]) + int(top_row[3]) == prop_ratio:
                        top_row_filled = [burger, slop, sushi, drumstick]
                else:
                    top_row_filled = [int(val) if val != '_' else 0 for val in top_row]

                if bottom_row.count('_') == 2:
                    prop_ratio = (burger + slop) / (sushi + drumstick)
                    if (int(bottom_row[0]) + int(bottom_row[1])) / (int(bottom_row[2]) + int(bottom_row[3]) == prop_ratio:
                        bottom_row_filled = [burger, slop, sushi, drumstick]
                else:
                    bottom_row_filled = [int(val) if val != '_' else 0 for val in bottom_row]

                # Check if the filled plates match the proportions
                if (top_row_filled[0] + bottom_row_filled[0]) / (top_row_filled[1] + bottom_row_filled[1]) == (top_row_filled[2] + bottom_row_filled[2]) / (top_row_filled[3] + bottom_row_filled[3]):
                    num_solutions += 1

# Output the number of distinct solutions
print(num_solutions)
