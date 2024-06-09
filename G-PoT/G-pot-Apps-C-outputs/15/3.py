
# Read input
N = int(input())
weights = list(map(int, input().split()))

# Calculate maximum weight of a 4-pack
max_weight = max(weights) * 4

# Calculate minimum weight of a 4-pack
min_weight = sum(sorted(weights)[:4])

# Calculate number of distinct weights for 4-packs
distinct_weights = sum(weights) - sum(sorted(weights)[:4]) + 1

# Calculate expected weight of a 4-pack
expected_weight = sum(weights) * 0.25

# Output results
print(max_weight, min_weight, distinct_weights, expected_weight)
