
import math

def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, edges

def solve(n, edges):
    # Check if the tree has a path of length 2
    for u, v in edges:
        if u == v:
            return "NO"
    
    # Check if the tree has a cycle
    visited = set()
    for u, v in edges:
        if u in visited and v in visited:
            return "NO"
        visited.add(u)
        visited.add(v)
    
    # Check if the tree is a binary tree
    if len(edges) != n - 1:
        return "NO"
    
    # Check if the tree has a path of length 3
    for u, v in edges:
        if u == 1 and v == 2:
            return "NO"
    
    return "YES"

def main():
    n, edges = get_input()
    print(solve(n, edges))

if __name__ == '__main__':
    main()

