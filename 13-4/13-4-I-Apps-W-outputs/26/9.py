
def solve(desires):
    # Initialize a dictionary to store the number of desires that can be satisfied for each (x, y) coordinate
    desires_dict = {}

    # Iterate over the desires and increment the number of desires that can be satisfied for each (x, y) coordinate
    for desire in desires:
        x, y, color = desire
        if (x, y) not in desires_dict:
            desires_dict[(x, y)] = 1
        else:
            desires_dict[(x, y)] += 1

    # Find the maximum number of desires that can be satisfied at the same time
    max_desires = max(desires_dict.values())

    return max_desires

