
# Read input
N = int(input())
weights = list(map(int, input().split()))

# Calculate maximum weight
max_weight = sum(sorted(weights)[-4:])

# Calculate minimum weight
min_weight = sum(sorted(weights)[:4])

# Calculate number of distinct weights
distinct_weights = len(set(sum(combination) for combination in itertools.combinations(weights, 4)))

# Calculate expected weight
expected_weight = sum(weights) * 1.0 / N * 4

# Print output
print(max_weight, min_weight, distinct_weights, expected_weight)
