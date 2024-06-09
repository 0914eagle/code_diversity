
import math

def solve(N, A):
    # Calculate the greatest common divisor (gcd) of all A_i
    gcd = math.gcd(A[0], math.gcd(A[1], A[2]))

    # Calculate the least common multiple (lcm) of all A_i
    lcm = int(A[0] * A[1] / gcd)

    # Calculate the minimum possible value of B_1 + ... + B_N
    min_sum = lcm * N

    # Return the result modulo (10^9 + 7)
    return min_sum % (10**9 + 7)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

