
import math

def f1(n, t):
    # Calculate the number of ways to choose the values of s_i
    num_ways = math.factorial(n)
    for i in range(n):
        num_ways //= math.factorial(t[i] - 1)
    return num_ways

def f2(n, t):
    # Calculate the number of ways to choose the values of s_i modulo 10^9 + 7
    num_ways = 1
    for i in range(n):
        num_ways = (num_ways * t[i]) % (10**9 + 7)
    return num_ways

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(f2(n, t))

