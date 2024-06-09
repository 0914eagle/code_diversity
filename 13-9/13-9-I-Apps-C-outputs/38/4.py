
import sys

def count_ways(N, d):
    # Calculate the number of ways to connect the parts
    num_ways = 1
    for i in range(N-1):
        num_ways = num_ways * (d[i] * (d[i+1]-1)) % 998244353
    return num_ways

if __name__ == "__main__":
    N = int(input())
    d = list(map(int, input().split()))
    print(count_ways(N, d))

