
import math

def solve(N, A):
    # Calculate the sum of the reciprocals of the numbers
    sum_reciprocals = sum([1/a for a in A])
    
    # Calculate the minimum possible value of B_1 + ... + B_N
    min_value = math.ceil(sum_reciprocals * N)
    
    # Return the minimum value modulo (10^9 + 7)
    return min_value % (10**9 + 7)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

