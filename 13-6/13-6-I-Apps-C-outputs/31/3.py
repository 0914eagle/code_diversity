
def f1(n):
    return n * (n - 1) // 2

def f2(n, t):
    import math
    import itertools
    from fractions import Fraction
    from functools import reduce

    # Calculate the number of ways to choose the values of s_i
    num_ways = 1
    for i in range(n):
        num_ways *= math.factorial(t[i] - 1)

    # Calculate the number of ways to permute the values of s_i
    num_permutations = math.factorial(n)

    # Calculate the final answer
    answer = num_ways * num_permutations
    return answer % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(f2(n, t))

