
import sys

def get_input():
    n, e = map(int, input().split())
    roads = []
    for i in range(e):
        a, b = map(int, input().split())
        roads.append((a, b))
    return n, e, roads

def solve(n, e, roads):
    # Initialize a matrix to keep track of the number of restaurants for each chain in each city
    restaurants = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize a list to keep track of the roads that have been assigned
    assigned_roads = []

    # Loop through each road and assign it to the chain with the least number of restaurants in the city it connects
    for road in roads:
        a, b = road
        if a not in assigned_roads:
            if restaurants[a][1] < restaurants[b][1]:
                assigned_roads.append(a)
                restaurants[a][1] += 1
            else:
                assigned_roads.append(b)
                restaurants[b][1] += 1
        elif b not in assigned_roads:
            if restaurants[b][1] < restaurants[a][1]:
                assigned_roads.append(b)
                restaurants[b][1] += 1
            else:
                assigned_roads.append(a)
                restaurants[a][1] += 1
        else:
            # If both cities have been assigned, the solution is not unique
            return "0"

    # If all roads have been assigned, return the solution
    return "".join(str(restaurants[road][1]) for road in assigned_roads)

n, e, roads = get_input()
print(solve(n, e, roads))

