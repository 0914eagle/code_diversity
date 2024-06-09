
def get_min_weight(stages, k):
    # Initialize the minimum weight to a large value
    min_weight = float('inf')
    # Loop through all possible combinations of stages
    for combination in combinations(stages, k):
        # Check if the combination satisfies the condition
        if is_valid_combination(combination):
            # Calculate the weight of the combination
            weight = sum([ord(stage) - ord('a') + 1 for stage in combination])
            # Update the minimum weight if necessary
            min_weight = min(min_weight, weight)
    # Return the minimum weight
    return -1 if min_weight == float('inf') else min_weight

def is_valid_combination(combination):
    # Check if the combination is valid
    for i in range(len(combination) - 1):
        if ord(combination[i + 1]) - ord(combination[i]) != 2:
            return False
    return True

def combinations(stages, k):
    # Generate all possible combinations of stages
    if k == 1:
        for stage in stages:
            yield [stage]
    else:
        for i in range(len(stages)):
            for combination in combinations(stages[i + 1:], k - 1):
                yield [stages[i]] + combination

n, k = map(int, input().split())
stages = input()
print(get_min_weight(stages, k))

