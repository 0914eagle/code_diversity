
import sys

def count_ways(N, d):
    # Initialize the number of ways to be 1, since we can choose not to connect any components
    ways = 1

    # Iterate over each component
    for i in range(N):
        # Calculate the number of ways to connect the current component to the previous components
        ways *= (d[i] * (d[i] - 1)) // 2

    # Return the result modulo 998244353
    return ways % 998244353

if __name__ == '__main__':
    N = int(input())
    d = list(map(int, input().split()))
    print(count_ways(N, d))

