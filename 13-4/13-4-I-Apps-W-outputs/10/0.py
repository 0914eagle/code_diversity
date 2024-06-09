
def max_cuts(sequence, budget):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    # Initialize the maximum number of cuts to 0
    max_cuts = 0
    # Initialize the current budget to 0
    current_budget = 0
    # Iterate over the sequence
    for i in range(len(sequence) - 1):
        # Calculate the cost of the current cut
        cost = abs(sequence[i] - sequence[i + 1])
        # Check if the current cut is within budget
        if current_budget + cost <= budget:
            # Increment the maximum number of cuts
            max_cuts += 1
            # Increment the current budget
            current_budget += cost
    # Return the maximum number of cuts
    return max_cuts

