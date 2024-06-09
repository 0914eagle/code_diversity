
import sys
import itertools

def get_input():
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    return N, M, conditions

def count_ways(N, M, conditions):
    # Initialize the number of ways to paint each square
    ways = [1] * (N + 1)
    # Loop through each condition
    for l, r, x in conditions:
        # Loop through each square between l and r
        for i in range(l, r + 1):
            # Calculate the number of ways to paint the square
            ways[i] = (ways[i - 1] + ways[i]) % 1000000007
    return ways[N]

def main():
    N, M, conditions = get_input()
    print(count_ways(N, M, conditions))

if __name__ == '__main__':
    main()

