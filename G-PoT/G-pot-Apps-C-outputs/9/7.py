
# Read input
N, M = map(int, input().split())
dials = list(map(int, input().strip()))

# Initialize variables
sums = []
prefix_sums = [0] * (N + 1)

# Calculate prefix sums
for i in range(1, N + 1):
    prefix_sums[i] = prefix_sums[i - 1] + dials[i - 1]

# Process each query
for _ in range(M):
    A, B = map(int, input().split())
    total_sum = prefix_sums[B] - prefix_sums[A - 1]
    sums.append(total_sum)

# Output the sums
for s in sums:
    print(s)
