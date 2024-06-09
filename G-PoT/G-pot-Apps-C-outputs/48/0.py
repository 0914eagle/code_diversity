
# Read input
top_row = list(map(lambda x: int(x) if x != '_' else None, input().split()))
bottom_row = list(map(lambda x: int(x) if x != '_' else None, input().split()))

# Initialize counter for distinct solutions
distinct_solutions = 0

# Loop through all possible values for the missing entries
for burger_salamander in range(1, 201):
    for slop_salamander in range(1, 201):
        for sushi_yeti in range(1, 201):
            for drumstick_yeti in range(1, 201):
                for burger_golem in range(1, 201):
                    for slop_golem in range(1, 201):
                        for sushi_imp in range(1, 201):
                            for drumstick_imp in range(1, 201):
                                for slop_kraken in range(1, 201):
                                    for drumstick_kraken in range(1, 201):
                                        # Check if the current values satisfy the proportions
                                        if (top_row[0] is None or top_row[0] == burger_salamander) and \
                                           (top_row[1] is None or top_row[1] == slop_salamander) and \
                                           (top_row[2] is None or top_row[2] == sushi_yeti) and \
                                           (top_row[3] is None or top_row[3] == drumstick_yeti) and \
                                           (top_row[4] is None or top_row[4] == burger_golem) and \
                                           (bottom_row[0] is None or bottom_row[0] == sushi_imp) and \
                                           (bottom_row[1] is None or bottom_row[1] == drumstick_imp) and \
                                           (bottom_row[2] is None or bottom_row[2] == slop_kraken) and \
                                           (bottom_row[3] is None or bottom_row[3] == drumstick_kraken):
                                            distinct_solutions += 1

# Output the number of distinct solutions
print(distinct_solutions)
