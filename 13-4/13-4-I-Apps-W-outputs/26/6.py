
def solve(desires):
    # Initialize a dictionary to store the number of desires that can be satisfied for each (x, y) coordinate
    desires_dict = {}

    # Iterate over the desires and increment the number of desires that can be satisfied for each (x, y) coordinate
    for desire in desires:
        x, y, c = desire
        if (x, y) not in desires_dict:
            desires_dict[(x, y)] = 1
        else:
            desires_dict[(x, y)] += 1

    # Return the maximum number of desires that can be satisfied
    return max(desires_dict.values())

