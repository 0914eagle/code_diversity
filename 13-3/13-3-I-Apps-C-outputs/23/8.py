
def get_max_executives(briefcases):
    # Sort the briefcases by number of bananas in descending order
    briefcases.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of executives and the total number of bananas
    num_executives = 0
    total_bananas = 0

    # Loop through the briefcases and assign them to the executives
    for briefcase in briefcases:
        # If the current executive is more evil than the previous one, increase the number of executives
        if briefcase[1] > total_bananas:
            num_executives += 1
            total_bananas = briefcase[1]
        # Otherwise, give the briefcase to the current executive
        else:
            total_bananas += briefcase[1]

    return num_executives

