
def get_max_health(areas, passages, health):
    # Initialize a graph to represent the cave-system
    graph = {i: set() for i in range(1, len(areas) + 1)}
    for e, b, a, h in passages:
        graph[e].add((b, a, h))
    
    # Dijkstra's algorithm to find the shortest path from area 1 to area n
    dist, prev = dijkstra(graph, 1, len(areas))
    
    # Calculate the maximum health Unnar can have after getting through the cave-system
    max_health = health
    for i in range(1, len(areas)):
        attack, health = graph[i][0]
        max_health -= attack
        if max_health <= 0:
            break
    
    return max_health

def dijkstra(graph, start, end):
    # Initialize the distance and previous node dictionaries
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    
    # Set the distance of the starting node to 0
    dist[start] = 0
    
    # Loop until the shortest path to all nodes is found
    nodes = set(graph)
    while nodes:
        # Get the node with the minimum distance
        node = min(nodes, key=dist.get)
        nodes.remove(node)
        
        # If the node is the end node, return the distance and previous node dictionaries
        if node == end:
            return dist, prev
        
        # Relax the node's neighbors
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
    
    # If the shortest path to all nodes is not found, return None
    return None, None

def main():
    # Read the input
    health, n, m = map(int, input().split())
    areas = [0] + [tuple(map(int, input().split())) for _ in range(m)]
    
    # Call the get_max_health function and print the result
    print(get_max_health(areas, areas[1:], health))

if __name__ == '__main__':
    main()

