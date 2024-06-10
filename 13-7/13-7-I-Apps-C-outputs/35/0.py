
import sys

def get_input():
    N = int(input())
    edges = []
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return N, edges

def solve(N, edges):
    # Initialize the count to 0
    count = 0
    
    # Iterate over all possible pairs of vertices
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            # Check if there is an edge between i and j
            if (i, j) in edges or (j, i) in edges:
                # Increment the count if there is an edge between i and j
                count += 1
    
    # Return the count modulo 10^9 + 7
    return count % 1000000007

def main():
    N, edges = get_input()
    print(solve(N, edges))

if __name__ == '__main__':
    main()

