
import math

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # Sort the array A in non-decreasing order
    A.sort()

    # Initialize the array B with the values A[i]^2
    B = [A[i]**2 for i in range(N)]

    # Calculate the sum of the squares of the elements of B
    sum_B = sum(B)

    # Calculate the sum of the squares of the elements of A
    sum_A = sum(A[i]**2 for i in range(N))

    # Calculate the minimum possible value of B_1 + ... + B_N for B_1,...,B_N that satisfy the condition
    min_sum = sum_B - sum_A + (N-1)*(A[0]**2)

    # Return the result modulo (10^9 + 7)
    return min_sum % (10**9 + 7)

print(solve())

