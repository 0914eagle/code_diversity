
# Read input
top_row = input().split()
bottom_row = input().split()

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
                                        # Check if the values satisfy the proportions
                                        if (top_row[0] == '_' or int(top_row[0]) == burger_salamander) and \
                                           (top_row[1] == '_' or int(top_row[1]) == slop_salamander) and \
                                           (top_row[2] == '_' or int(top_row[2]) == sushi_yeti) and \
                                           (top_row[3] == '_' or int(top_row[3]) == drumstick_yeti) and \
                                           (top_row[4] == '_' or int(top_row[4]) == burger_golem) and \
                                           (top_row[5] == '_' or int(top_row[5]) == slop_golem) and \
                                           (top_row[6] == '_' or int(top_row[6]) == sushi_imp) and \
                                           (top_row[7] == '_' or int(top_row[7]) == drumstick_imp) and \
                                           (top_row[8] == '_' or int(top_row[8]) == slop_kraken) and \
                                           (top_row[9] == '_' or int(top_row[9]) == drumstick_kraken) and \
                                           (bottom_row[0] == '_' or int(bottom_row[0]) == burger_salamander) and \
                                           (bottom_row[1] == '_' or int(bottom_row[1]) == slop_salamander) and \
                                           (bottom_row[2] == '_' or int(bottom_row[2]) == sushi_yeti) and \
                                           (bottom_row[3] == '_' or int(bottom_row[3]) == drumstick_yeti) and \
                                           (bottom_row[4] == '_' or int(bottom_row[4]) == burger_golem) and \
                                           (bottom_row[5] == '_' or int(bottom_row[5]) == slop_golem) and \
                                           (bottom_row[6] == '_' or int(bottom_row[6]) == sushi_imp) and \
                                           (bottom_row[7] == '_' or int(bottom_row[7]) == drumstick_imp) and \
                                           (bottom_row[8] == '_' or int(bottom_row[8]) == slop_kraken) and \
                                           (bottom_row[9] == '_' or int(bottom_row[9]) == drumstick_kraken):
                                            distinct_solutions += 1

# Output the number of distinct solutions
print(distinct_solutions)
