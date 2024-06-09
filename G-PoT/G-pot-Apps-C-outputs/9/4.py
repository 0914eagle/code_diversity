
# Read input
N, M = map(int, input().split())
dials = list(map(int, input().strip()))

# Initialize variables
sums = []
current_sum = sum(dials)

# Iterate through each query
for _ in range(M):
    A, B = map(int, input().split())
    
    # Calculate the sum of dials between A and B
    query_sum = sum(dials[A-1:B])
    sums.append(query_sum)
    
    # Update the current sum by subtracting the previous sum and adding the new sum
    current_sum = current_sum - query_sum + (B - A + 1) * 1
    
# Output the sums
for s in sums:
    print(s)
