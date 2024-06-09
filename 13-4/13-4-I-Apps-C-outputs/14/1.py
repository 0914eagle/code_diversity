
import sys

def get_input():
    n, e = map(int, input().split())
    roads = []
    for i in range(e):
        a, b = map(int, input().split())
        roads.append((a, b))
    return n, e, roads

def solve(n, e, roads):
    # Initialize the chains array with 0s
    chains = [0] * (n + 1)
    
    # Loop through each road
    for i in range(e):
        # Get the two cities connected by the road
        a, b = roads[i]
        
        # If the first chain has not been assigned to either city, assign it to the first city
        if chains[a] == 0:
            chains[a] = 1
        
        # If the second chain has not been assigned to either city, assign it to the second city
        if chains[b] == 0:
            chains[b] = 2
        
        # If both chains have been assigned to the cities, check if they are the same
        if chains[a] != chains[b]:
            # If they are not the same, return "0" as the solution is not unique
            return "0"
    
    # If we reach this point, the solution is unique, so return the chains array
    return "".join(str(chain) for chain in chains[1:])

n, e, roads = get_input()
print(solve(n, e, roads))

