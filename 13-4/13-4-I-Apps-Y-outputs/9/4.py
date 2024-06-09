
import sys
input = sys.stdin.read().splitlines()
n, m, k = map(int, input[0].split())
roads = [tuple(map(int, input[i].split())) for i in range(1, m+1)]
routes = [tuple(map(int, input[m+i].split())) for i in range(k)]

# Create a graph with n vertices and m edges
# The edges are represented as a list of tuples (u, v, w), where
# u and v are the vertices connected by the edge and w is the cost
# of traveling along that edge
graph = [(roads[i-1][0], roads[i-1][1], roads[i-1][2]) for i in range(1, m+1)]

# Function to find the minimum cost of traveling between two vertices
def find_min_cost(u, v):
    min_cost = float('inf')
    for edge in graph:
        if edge[0] == u and edge[1] == v:
            min_cost = min(min_cost, edge[2])
    return min_cost

# Function to find the minimum total cost of traveling between all pairs of vertices
def find_min_total_cost():
    min_total_cost = 0
    for i in range(k):
        u, v = routes[i]
        min_total_cost += find_min_cost(u, v)
    return min_total_cost

# Function to find the minimum total cost of traveling between all pairs of vertices after making at most one road cost zero
def find_min_total_cost_with_zero_cost_road():
    # Initialize the minimum total cost to infinity
    min_total_cost = float('inf')
    # Loop through all possible roads that can be made cost zero
    for i in range(m):
        # Find the cost of traveling between all pairs of vertices before making the current road cost zero
        total_cost_before = find_min_total_cost()
        # Make the current road cost zero
        graph[i] = (graph[i][0], graph[i][1], 0)
        # Find the cost of traveling between all pairs of vertices after making the current road cost zero
        total_cost_after = find_min_total_cost()
        # If the cost of traveling between all pairs of vertices after making the current road cost zero is less than the current minimum total cost, update the minimum total cost
        if total_cost_after < min_total_cost:
            min_total_cost = total_cost_after
        # Make the current road cost non-zero again
        graph[i] = (graph[i][0], graph[i][1], graph[i][2])
    return min_total_cost

print(find_min_total_cost_with_zero_cost_road())

