
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

    # Calculate the sum between A and B
    query_sum = sum(dials[A:B+1])

    # Update the current sum
    current_sum += query_sum

    # Update the dials
    for i in range(A, B+1):
        dials[i] = (dials[i] + 1) % 10

    # Append the sum to the list
    sums.append(query_sum)

# Output the sums
for s in sums:
    print(s)
