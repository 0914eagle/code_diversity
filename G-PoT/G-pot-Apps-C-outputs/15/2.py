
import itertools

# Read input
N = int(input())
weights = list(map(int, input().split()))

# Calculate maximum weight of a 4-pack
max_weight = sum(sorted(weights)[-4:])

# Calculate minimum weight of a 4-pack
min_weight = sum(sorted(weights)[:4])

# Calculate number of distinct weights for 4-packs
distinct_weights = set()
for comb in itertools.combinations_with_replacement(weights, 4):
    distinct_weights.add(sum(comb))
num_distinct_weights = len(distinct_weights)

# Calculate expected weight of a 4-pack
total_weight = sum(weights)
num_combinations = len(list(itertools.combinations_with_replacement(weights, 4)))
expected_weight = total_weight * num_combinations / num_distinct_weights

# Output results
print(max_weight, min_weight, num_distinct_weights, expected_weight)
