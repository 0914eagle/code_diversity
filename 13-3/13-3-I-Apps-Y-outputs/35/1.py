
def find_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a counter for the number of cycles
    cycles = 0

    # Iterate over the graph
    for node in graph:
        if node not in visited:
            # Find all cycles starting from the current node
            cycles += find_cycles_util(node, graph, visited)

    return cycles

def find_cycles_util(node, graph, visited):
    # Mark the current node as visited
    visited.add(node)

    # Initialize a counter for the number of cycles
    cycles = 0

    # Iterate over the neighbors of the current node
    for neighbor in graph[node]:
        # If the neighbor is not visited, find all cycles starting from the neighbor
        if neighbor not in visited:
            cycles += find_cycles_util(neighbor, graph, visited)

    # If the current node has a neighbor that is not visited, it means that there is a cycle
    if len(visited) > 1:
        cycles += 1

    return cycles

# Main function
def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    print(find_cycles(n, m, edges))

if __name__ == "__main__":
    main()

