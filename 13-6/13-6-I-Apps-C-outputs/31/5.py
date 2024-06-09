
import math

def f1(n, t):
    # Calculate the number of ways to choose the values of s_i
    num_ways = 1
    for i in range(n):
        num_ways *= math.factorial(n - i)
    
    # Return the result modulo 10^9 + 7
    return num_ways % (10**9 + 7)

def f2(n, t):
    # Calculate the number of ways to choose the values of s_i
    num_ways = 1
    for i in range(n):
        num_ways *= math.factorial(n - i)
    
    # Return the result modulo 10^9 + 7
    return num_ways % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(f1(n, t))
    print(f2(n, t))

