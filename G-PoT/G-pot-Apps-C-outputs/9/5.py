
# Read input values
N, M = map(int, input().split())
initial_config = list(map(int, input().strip()))

# Initialize variables
dials = initial_config.copy()
sums = []

# Calculate sums and update dials
for _ in range(M):
    A, B = map(int, input().split())
    current_sum = sum(dials[A-1:B])
    sums.append(current_sum)
    for i in range(A-1, B):
        dials[i] = (dials[i] + 1) % 10

# Print the calculated sums
for s in sums:
    print(s)
