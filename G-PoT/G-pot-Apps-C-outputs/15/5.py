
import itertools

# Read input
N = int(input())
weights = list(map(int, input().split()))

# Calculate maximum weight of a 4-pack
max_weight = sum(sorted(weights)[-4:])

# Calculate minimum weight of a 4-pack
min_weight = sum(sorted(weights)[:4])

# Calculate number of distinct weights
distinct_weights = set()
for combo in itertools.combinations(weights, 4):
    distinct_weights.add(sum(combo))
num_distinct_weights = len(distinct_weights)

# Calculate expected weight of a 4-pack
expected_weight = sum(weights) * 1.0 / N * 4

# Output results
print(max_weight, min_weight, num_distinct_weights, expected_weight)
