
# Read input
top_row = input().split()
bottom_row = input().split()

# Count number of empty slots
num_empty_slots = top_row.count('_') + bottom_row.count('_')

# Check if there are infinitely many solutions
if num_empty_slots == 0:
    print("many")
else:
    # Calculate the number of distinct solutions
    distinct_solutions = 1
    for i in range(num_empty_slots):
        distinct_solutions *= 10

    print(distinct_solutions)
