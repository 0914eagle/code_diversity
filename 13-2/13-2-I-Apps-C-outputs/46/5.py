
def get_maximum_gold(n, m, roads, gold):
    # Initialize a graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        graph[roads[i][0]].append(roads[i][1])
        graph[roads[i][1]].append(roads[i][0])
    
    # Initialize a visited array and a parent array
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    
    # Initialize the maximum gold to 0
    max_gold = 0
    
    # Iterate through all the villages
    for village in range(1, n + 1):
        # If the village has not been visited yet
        if not visited[village]:
            # Perform DFS on the graph starting from the current village
            dfs(graph, visited, parent, village)
            # Get the maximum gold collected by the bandits during the DFS
            max_gold = max(max_gold, get_max_gold(parent, village, gold))
    
    return max_gold

def dfs(graph, visited, parent, village):
    # Mark the current village as visited
    visited[village] = True
    # Iterate through the neighbors of the current village
    for neighbor in graph[village]:
        # If the neighbor has not been visited yet
        if not visited[neighbor]:
            # Perform DFS on the neighbor
            dfs(graph, visited, parent, neighbor)
            # Update the parent of the current village
            parent[village] = neighbor

def get_max_gold(parent, village, gold):
    # Initialize the maximum gold to 0
    max_gold = 0
    # Iterate through the parents of the current village
    while village != 0:
        # Add the gold in the current village to the maximum gold
        max_gold += gold[village]
        # Update the current village to its parent
        village = parent[village]
    
    return max_gold

# Main function
def main():
    # Read the input
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        a, b = map(int, input().split())
        roads.append([a, b])
    gold = list(map(int, input().split()))
    
    # Get the maximum gold
    max_gold = get_maximum_gold(n, m, roads, gold)
    
    # Print the maximum gold
    print(max_gold)

if __name__ == "__main__":
    main()

