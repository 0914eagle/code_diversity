
import math

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # Sort the array A in non-decreasing order
    A.sort()

    # Initialize B as an array of ones with the same length as A
    B = [1] * N

    # Loop through each element of A and find the smallest number that satisfies the condition
    for i in range(N):
        B[i] = int(math.ceil(A[i] / B[i - 1])) if i > 0 else 1

    # Calculate the sum of B modulo (10^9 + 7)
    sum_B = sum(B) % (10**9 + 7)

    return sum_B

print(solve())

