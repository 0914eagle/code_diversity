
import math

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # Sort the array A in non-decreasing order
    A.sort()

    # Initialize the array B with the values A[i] for i = 1, 2, ..., N
    B = [A[i] for i in range(N)]

    # Loop through each element of the array A and check if the condition is satisfied
    for i in range(N):
        for j in range(i+1, N):
            if A[i] * A[j] != A[j] * A[i]:
                # If the condition is not satisfied, swap the elements of the array B
                B[i], B[j] = B[j], B[i]

    # Calculate the sum of the elements of the array B
    sum_B = sum(B)

    # Return the sum modulo (10^9 + 7)
    return sum_B % (10**9 + 7)

print(solve())

