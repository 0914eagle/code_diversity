
def max_cuts(sequence, budget):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    # Initialize the maximum number of cuts to 0
    max_cuts = 0
    # Initialize the current budget to 0
    current_budget = 0
    # Iterate over the sequence
    for i in range(len(sequence)):
        # Check if the current element is odd
        if sequence[i] % 2 == 1:
            # If the current element is odd, add it to the current budget
            current_budget += sequence[i]
        # Check if the current budget is less than or equal to the budget
        if current_budget <= budget:
            # If the current budget is less than or equal to the budget, increment the maximum number of cuts
            max_cuts += 1
        # If the current budget is greater than the budget, break the loop
        else:
            break
    # Return the maximum number of cuts
    return max_cuts

