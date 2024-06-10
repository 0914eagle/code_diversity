
import sys
import math

def get_input():
    n, m = map(int, input().split())
    return n, m

def solve(n, m):
    # Initialize the graph with the initial world
    graph = {0: {1}, 1: {0}}
    
    # Add the new vertices and edges in each change
    for i in range(n):
        w = i + 2
        u, v = map(int, input().split())
        graph[w] = {u, v}
        graph[u].add(w)
        graph[v].add(w)
    
    # Count the number of non-similar worlds
    count = 0
    for i in range(1, len(graph)):
        for j in range(i + 1, len(graph)):
            if len(graph[i] & graph[j]) == m:
                count += 1
    
    return count % (10**9 + 7)

def main():
    n, m = get_input()
    print(solve(n, m))

if __name__ == '__main__':
    main()

