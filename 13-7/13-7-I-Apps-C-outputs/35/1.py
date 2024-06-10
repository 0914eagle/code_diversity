
import sys

def get_input():
    N = int(input())
    edges = []
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return N, edges

def count_ways(N, edges):
    # Initialize a dictionary to store the number of ways for each vertex
    ways = {i: 1 for i in range(1, N + 1)}

    # Iterate through the edges and update the number of ways for each vertex
    for x, y in edges:
        ways[x] = (ways[x] * ways[y]) % 1000000007
        ways[y] = ways[x]

    # Return the sum of the number of ways for all vertices
    return sum(ways.values()) % 1000000007

def main():
    N, edges = get_input()
    print(count_ways(N, edges))

if __name__ == '__main__':
    main()

