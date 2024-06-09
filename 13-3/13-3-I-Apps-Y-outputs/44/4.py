
def solve(ants1, ants2, time):
    # Initialize the order of the ants after time seconds
    order = ""

    # Loop through each second
    for i in range(time):
        # If it's an even second, ants in the first row move forward
        if i % 2 == 0:
            order += ants1
        # If it's an odd second, ants in the second row move forward
        else:
            order += ants2

        # If it's not the first second, ants may jump over each other
        if i > 0:
            # Loop through each ant in the first row
            for j in range(len(ants1)):
                # If the ant is not the first ant and the ant in front of it is in the second row
                if j > 0 and ants1[j-1] in ants2:
                    # Swap the positions of the two ants
                    order = order[:j] + ants1[j-1] + ants1[j] + order[j+1:]

    return order

