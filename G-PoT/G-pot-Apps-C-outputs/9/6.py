
# Read input
N, M = map(int, input().split())
dials = list(map(int, input().strip()))

# Initialize variables
sums = []
current_sum = sum(dials)

# Process each query
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    current_sum += (dials[B] - dials[A] + 10) % 10
    sums.append(current_sum)
    for i in range(A, B+1):
        dials[i] = (dials[i] + 1) % 10

# Output the sums
for s in sums:
    print(s)
