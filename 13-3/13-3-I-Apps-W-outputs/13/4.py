
import math

def solve(N, A):
    # Calculate the greatest common divisor (gcd) of all A_i
    gcd = math.gcd(A[0], math.gcd(A[1], A[2]))

    # Divide all A_i by their gcd
    A = [a // gcd for a in A]

    # Calculate the sum of the reciprocals of all A_i
    sum_reciprocals = sum([1 / a for a in A])

    # Calculate the minimum possible value of B_1 + ... + B_N
    min_value = int((sum_reciprocals * gcd) % (10**9 + 7))

    return min_value

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))

