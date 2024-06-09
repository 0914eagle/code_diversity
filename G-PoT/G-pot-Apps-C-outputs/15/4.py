
# Read input
N = int(input())
weights = list(map(int, input().split()))

# Calculate maximum and minimum weight of a 4-pack
max_weight = max(weights) * 4
min_weight = sum(sorted(weights)[:4])

# Calculate number of distinct weights
distinct_weights = set()
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            for l in range(k, N):
                distinct_weights.add(weights[i] + weights[j] + weights[k] + weights[l])
num_distinct_weights = len(distinct_weights)

# Calculate expected weight of a 4-pack
expected_weight = sum(distinct_weights) / num_distinct_weights

# Output results
print(max_weight, min_weight, num_distinct_weights, expected_weight)
