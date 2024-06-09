
# Read input
N, M = map(int, input().split())
initial_config = list(map(int, input().strip()))

# Initialize variables
dials = initial_config.copy()
sums = []

# Calculate sums
for _ in range(M):
    A, B = map(int, input().split())
    total = sum(dials[A-1:B])
    sums.append(total)
    
    # Press the button on dials between A and B
    for i in range(A-1, B):
        dials[i] = (dials[i] + 1) % 10

# Output the sums
for total in sums:
    print(total)
