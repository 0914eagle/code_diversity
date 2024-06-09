
# Read input
N, M = map(int, input().split())
dials = list(map(int, input().strip()))

# Initialize variables
sums = []
total_sum = sum(dials)

# Process each query
for _ in range(M):
    A, B = map(int, input().split())
    sum_between = sum(dials[A-1:B])
    sums.append(sum_between)
    
    # Update total sum
    total_sum += sum_between
    
# Output the sums
for s in sums:
    print(s)
