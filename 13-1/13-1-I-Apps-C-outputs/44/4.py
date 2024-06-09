
def get_min_energy(N, M, alpha, roads):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for u, v, c in roads:
        graph[u-1].append((v-1, c))
        graph[v-1].append((u-1, c))
    
    # Initialize a set to keep track of visited nodes
    visited = set()
    
    # Initialize a variable to keep track of the minimum energy
    min_energy = float('inf')
    
    # Iterate through all possible starting nodes
    for node in range(N):
        if node not in visited:
            # Initialize a variable to keep track of the current energy
            current_energy = 0
            
            # Initialize a set to keep track of visited nodes in the current path
            path_visited = set()
            
            # Iterate through all possible paths from the current node
            for path in dfs(graph, node, visited, path_visited):
                # Calculate the energy for the current path
                current_energy += calculate_energy(path, alpha)
                
                # Update the minimum energy if necessary
                min_energy = min(min_energy, current_energy)
    
    # Return the minimum energy
    return min_energy if min_energy < float('inf') else "Poor girl"

def dfs(graph, node, visited, path_visited):
    # Yield the current path
    yield [node]
    
    # Mark the current node as visited
    visited.add(node)
    path_visited.add(node)
    
    # Iterate through all neighbors of the current node
    for neighbor, _ in graph[node]:
        # If the neighbor has not been visited, recurse
        if neighbor not in visited:
            yield from dfs(graph, neighbor, visited, path_visited)
        # If the neighbor has been visited but is not in the current path, recurse
        elif neighbor not in path_visited:
            yield from dfs(graph, neighbor, visited, path_visited)

def calculate_energy(path, alpha):
    # Initialize a variable to keep track of the maximum number of candies
    max_candies = 0
    
    # Iterate through all nodes in the path
    for i in range(len(path)-1):
        # Calculate the number of candies for the current road
        candies = path[i+1][1] - path[i][1]
        
        # Update the maximum number of candies if necessary
        max_candies = max(max_candies, candies)
    
    # Return the energy for the current path
    return max_candies**2 + alpha * (len(path)-1)

if __name__ == '__main__':
    N, M, alpha = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(M)]
    print(get_min_energy(N, M, alpha, roads))

