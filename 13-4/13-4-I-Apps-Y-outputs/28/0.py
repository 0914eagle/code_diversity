
def solve(N, A, B, C):
    # Sort the parts by size in descending order
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # Initialize the number of altars to 0
    altars = 0

    # Loop through each possible combination of upper, middle, and lower parts
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                # Check if the parts satisfy the conditions for an altar
                if A[i] < B[j] and B[j] < C[k]:
                    altars += 1

    return altars

