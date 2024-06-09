
import math

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # Sort the array A in non-decreasing order
    A.sort()

    # Initialize the array B with the values of A
    B = A[:]

    # Calculate the minimum possible value of B_1 + ... + B_N for B_1,...,B_N that satisfy the condition
    min_sum = math.inf
    for i in range(N):
        for j in range(i+1, N):
            if A[i] * A[j] == A[j] * A[i]:
                min_sum = min(min_sum, B[i] + B[j])

    # Print the minimum possible value of B_1 + ... + B_N modulo (10^9 + 7)
    print(min_sum % (10**9 + 7))

solve()

