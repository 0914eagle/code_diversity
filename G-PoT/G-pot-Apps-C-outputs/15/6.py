
N = int(input())
weights = list(map(int, input().split()))

max_weight = max(weights) * 4
min_weight = sum(sorted(weights)[:4])
distinct_weights = len(set(sum(combination) for combination in itertools.combinations(weights, 4)))
expected_weight = sum(weights) * 0.25

print(max_weight, min_weight, distinct_weights, expected_weight)
