
def build_rocket(stages, k):
    # Initialize the minimum weight and the resulting rocket
    min_weight = float('inf')
    rocket = []

    # Iterate over all possible combinations of stages
    for combination in combinations(stages, k):
        # Check if the combination satisfies the condition
        if is_valid_combination(combination):
            # Calculate the weight of the combination
            weight = sum(alphabet.index(stage) for stage in combination)

            # If the weight is less than the minimum weight, update the minimum weight and the resulting rocket
            if weight < min_weight:
                min_weight = weight
                rocket = combination

    # Return the resulting rocket or -1 if it is impossible to build a rocket
    return '-1' if min_weight == float('inf') else ''.join(rocket)

# Check if a combination of stages satisfies the condition
def is_valid_combination(combination):
    for i in range(len(combination) - 1):
        if alphabet.index(combination[i + 1]) - alphabet.index(combination[i]) != 2:
            return False
    return True

# Dictionary to map each stage to its position in the alphabet
alphabet = {stage: i for i, stage in enumerate(ascii_lowercase, 1)}

# Function to generate all combinations of stages
from itertools import combinations

# Test the build_rocket function with example inputs
stages = 'xyabd'
k = 3
print(build_rocket(stages, k))

stages = 'problem'
k = 4
print(build_rocket(stages, k))

stages = 'ab'
k = 2
print(build_rocket(stages, k))

stages = 'abaabbaaabbb'
k = 1
print(build_rocket(stages, k))

