
def count_optimal_paths(n, roads):
    # Initialize a graph with n junctions and n-1 roads
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # Function to count the number of optimal paths of length 2 from a junction to another
    def count_optimal_paths_helper(curr, visited, target, count):
        # Base case: if the current junction is the target junction, return 1
        if curr == target:
            return 1
        
        # Mark the current junction as visited
        visited[curr] = True
        
        # Recursively count the number of optimal paths from the current junction to the target junction
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                count += count_optimal_paths_helper(neighbor, visited, target, count)
        
        # Unmark the current junction as visited
        visited[curr] = False
        
        return count
    
    # Initialize the count of optimal paths to 0
    count = 0
    
    # Iterate over all junctions and count the number of optimal paths from each junction to the target junction
    for junction in range(n):
        count += count_optimal_paths_helper(junction, [False] * n, junction, count)
    
    return count

