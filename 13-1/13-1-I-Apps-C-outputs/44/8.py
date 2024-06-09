
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
            current_visited = set()
            
            # Iterate through all possible paths from the current node
            for path in dfs(graph, node, current_visited):
                # Calculate the current energy for the current path
                current_energy += calculate_energy(path, alpha)
                
                # If the current energy is less than the minimum energy, update the minimum energy
                if current_energy < min_energy:
                    min_energy = current_energy
    
    # Return the minimum energy
    return min_energy

def dfs(graph, node, visited):
    # Yield the current node
    yield node
    
    # Mark the current node as visited
    visited.add(node)
    
    # Iterate through all neighbors of the current node
    for neighbor in graph[node]:
        if neighbor[0] not in visited:
            # Recursively search for paths from the neighbor
            yield from dfs(graph, neighbor[0], visited)

def calculate_energy(path, alpha):
    # Initialize a variable to keep track of the maximum number of candies
    max_candies = 0
    
    # Iterate through all nodes in the path
    for i in range(len(path)-1):
        # Calculate the number of candies on the current road
        candies = path[i+1][1] - path[i][1]
        
        # If the number of candies is greater than the maximum, update the maximum
        if candies > max_candies:
            max_candies = candies
    
    # Return the energy for the current path
    return max_candies**2 + alpha * (len(path)-1)

if __name__ == '__main__':
    N, M, alpha = map(int, input().split())
    roads = []
    for _ in range(M):
        u, v, c = map(int, input().split())
        roads.append((u, v, c))
    print(get_min_energy(N, M, alpha, roads))

