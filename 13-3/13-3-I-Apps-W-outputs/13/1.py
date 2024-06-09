
import math

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # Sort the array A in non-decreasing order
    A.sort()

    # Initialize B as an array of ones
    B = [1] * N

    # Loop through the array A and update B
    for i in range(N):
        B[i] = math.ceil(B[i] * A[i])

    # Calculate the sum of B modulo (10^9 + 7)
    sum_B = sum(B) % (10**9 + 7)

    return sum_B

print(solve())

