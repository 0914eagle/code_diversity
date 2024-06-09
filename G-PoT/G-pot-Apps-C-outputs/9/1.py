
# Read input
N, M = map(int, input().split())
dials = list(map(int, input().strip()))

# Initialize variables
sums = []
total_sum = sum(dials)

# Process each query
for _ in range(M):
    A, B = map(int, input().split())
    current_sum = sum(dials[A-1:B])
    sums.append(current_sum)
    
    # Update total sum and dials
    total_sum += current_sum
    for i in range(A-1, B):
        dials[i] = (dials[i] + 1) % 10

    # Print the current sum
    print(current_sum)
