
import sys
import math

def get_input():
    n, m = map(int, input().split())
    v = list(map(int, input().split()))
    edges = []
    for i in range(m):
        x, y = map(int, input().split())
        edges.append((x, y))
    return n, m, v, edges

def solve(n, m, v, edges):
    # Initialize the minimum energy needed to remove each part
    min_energy = [math.inf] * (n + 1)
    min_energy[0] = 0

    # Initialize the parent of each part
    parent = [0] * (n + 1)

    # Loop through all the edges
    for i in range(m):
        x, y = edges[i]
        # If the minimum energy needed to remove the parent of x is less than the minimum energy needed to remove x itself
        if min_energy[parent[x]] < min_energy[x]:
            # Set the minimum energy needed to remove x to be the minimum energy needed to remove its parent
            min_energy[x] = min_energy[parent[x]]
        # If the minimum energy needed to remove the parent of y is less than the minimum energy needed to remove y itself
        if min_energy[parent[y]] < min_energy[y]:
            # Set the minimum energy needed to remove y to be the minimum energy needed to remove its parent
            min_energy[y] = min_energy[parent[y]]
    
    # Return the minimum energy needed to remove all the parts
    return sum(min_energy)

def main():
    n, m, v, edges = get_input()
    print(solve(n, m, v, edges))

if __name__ == '__main__':
    main()

