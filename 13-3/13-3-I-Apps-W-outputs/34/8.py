
import sys

def get_input():
    h, w = map(int, input().split())
    costs = []
    for i in range(10):
        costs.append(list(map(int, input().split())))
    wall = []
    for i in range(h):
        wall.append(list(map(int, input().split())))
    return h, w, costs, wall

def solve(h, w, costs, wall):
    # Initialize the minimum cost to turn every digit into 1
    min_cost = 0
    # Loop through each row of the wall
    for i in range(h):
        # Loop through each column of the wall
        for j in range(w):
            # If the current square contains a digit
            if wall[i][j] != -1:
                # Get the cost of turning the current digit into 1
                cost = costs[wall[i][j]][1]
                # If the cost is not zero
                if cost != 0:
                    # Add the cost to the minimum cost
                    min_cost += cost
    return min_cost

h, w, costs, wall = get_input()
print(solve(h, w, costs, wall))

