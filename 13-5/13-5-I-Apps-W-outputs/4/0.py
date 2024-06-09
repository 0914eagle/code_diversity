
def get_min_weight(stages, k):
    # Initialize the minimum weight to a large value
    min_weight = float('inf')
    # Loop through all possible combinations of stages
    for combination in combinations(stages, k):
        # Check if the combination satisfies the condition
        if is_valid_combination(combination):
            # Calculate the weight of the combination
            weight = sum(ord(stage) for stage in combination)
            # Update the minimum weight if necessary
            min_weight = min(min_weight, weight)
    # Return the minimum weight
    return -1 if min_weight == float('inf') else min_weight

# Check if a combination of stages satisfies the condition
def is_valid_combination(combination):
    for i in range(len(combination) - 1):
        if ord(combination[i + 1]) - ord(combination[i]) != 2:
            return False
    return True

# Driver code to test the function
if __name__ == '__main__':
    stages = 'xyabd'
    k = 3
    print(get_min_weight(stages, k))

