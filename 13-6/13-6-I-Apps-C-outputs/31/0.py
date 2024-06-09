
import math

def f1(n, t):
    # Calculate the number of ways to choose the values of s_i
    num_ways = math.factorial(n) // math.factorial(n - 2)
    
    # Calculate the number of ways to permute the chairs
    num_permutations = math.factorial(n)
    
    # Calculate the number of ways to choose the values of s_i and permute the chairs
    result = num_ways * num_permutations
    
    return result % (10**9 + 7)

def f2(n, t):
    # Calculate the number of ways to choose the values of s_i
    num_ways = math.factorial(n) // math.factorial(n - 2)
    
    # Calculate the number of ways to permute the chairs
    num_permutations = math.factorial(n)
    
    # Calculate the number of ways to choose the values of s_i and permute the chairs
    result = num_ways * num_permutations
    
    return result % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    print(f1(n, t))
    print(f2(n, t))

