
def solve(n, k, stages):
    # Initialize the minimum weight to a large value
    min_weight = 1000
    # Loop through all possible combinations of stages
    for combination in itertools.combinations(stages, k):
        # Check if the combination satisfies the condition
        if is_valid_combination(combination):
            # Calculate the weight of the combination
            weight = sum([stages.index(stage) for stage in combination])
            # Update the minimum weight if necessary
            min_weight = min(min_weight, weight)
    # Return the minimum weight
    return min_weight if min_weight != 1000 else -1

# Check if a combination of stages satisfies the condition
def is_valid_combination(combination):
    for i in range(len(combination)):
        # Check if the current stage is adjacent to the previous stage in the alphabet
        if abs(combination[i].index(combination[i-1]) - 1) == 0:
            return False
    return True

