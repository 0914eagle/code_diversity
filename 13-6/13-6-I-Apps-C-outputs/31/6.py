
import sys

def hop(n, t):
    # Initialize a dictionary to store the number of ways to choose s_i
    ways = {i: 0 for i in range(1, n + 1)}
    ways[1] = 1
    
    # Iterate over the hops
    for i in range(2, n + 1):
        # Calculate the number of ways to choose s_i
        ways[i] = sum(ways[j] for j in range(1, i))
    
    # Return the number of ways to choose s_i modulo 10^9 + 7
    return ways[t] % 1000000007

def main():
    n = int(input())
    t = list(map(int, input().split()))
    print(hop(n, t))

if __name__ == '__main__':
    main()

