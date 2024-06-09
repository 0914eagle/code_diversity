
# Read input
N, M = map(int, input().split())
dials = list(map(int, input().strip()))

# Initialize variables
sums = []
total_sum = sum(dials)

# Calculate sums
for _ in range(M):
    A, B = map(int, input().split())
    current_sum = sum(dials[A-1:B])
    sums.append(current_sum)
    total_sum += current_sum - (dials[A-1] + dials[B-1])
    dials[A-1:B] = [(x+1)%10 for x in dials[A-1:B]]

    print(current_sum)

