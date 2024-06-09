
def solve(n, k, stages):
    # Initialize the minimum weight to a large value
    min_weight = float('inf')
    # Loop through all possible combinations of stages
    for combination in itertools.combinations(stages, k):
        # Check if the combination satisfies the condition
        if is_valid_combination(combination):
            # Calculate the weight of the combination
            weight = sum([stages.index(stage) for stage in combination])
            # Update the minimum weight if necessary
            min_weight = min(min_weight, weight)
    # Return the minimum weight or -1 if it is impossible to build the rocket
    return min_weight if min_weight < float('inf') else -1

# Check if a combination of stages satisfies the condition
def is_valid_combination(combination):
    for i in range(len(combination)):
        # Check if the current stage is not the last stage in the combination
        if i < len(combination) - 1:
            # Check if the next stage is not adjacent in the alphabet
            if stages.index(combination[i + 1]) - stages.index(combination[i]) != 2:
                return False
    return True

# Test the function with example inputs
n = 5
k = 3
stages = "xyabd"
print(solve(n, k, stages))

n = 7
k = 4
stages = "problem"
print(solve(n, k, stages))

n = 2
k = 2
stages = "ab"
print(solve(n, k, stages))

n = 12
k = 1
stages = "abaabbaaabbb"
print(solve(n, k, stages))

