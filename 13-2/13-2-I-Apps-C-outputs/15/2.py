
def solve(n, files):
    # Initialize a graph with the given files as nodes
    graph = {file: set() for file in files}

    # Populate the graph with edges based on the import statements
    for file, imports in files.items():
        for import_file in imports:
            graph[file].add(import_file)

    # Find a shortest cycle in the graph
    cycle = find_shortest_cycle(graph)

    # If there is no cycle, return "SHIP IT"
    if not cycle:
        return "SHIP IT"

    # Otherwise, return the names of the files in the cycle
    return " ".join(cycle)

def find_shortest_cycle(graph):
    # Initialize a set to keep track of visited nodes
    visited = set()

    # Initialize a queue to keep track of nodes to visit
    queue = [node for node in graph if node not in visited]

    # While the queue is not empty
    while queue:
        # Dequeue a node and mark it as visited
        node = queue.pop(0)
        visited.add(node)

        # If the node has neighbors that have not been visited, add them to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

        # If the node has a neighbor that has already been visited, we have found a cycle
        for neighbor in graph[node]:
            if neighbor in visited:
                # Return the cycle by tracing back the path from the node to the neighbor
                cycle = [node]
                while True:
                    cycle.append(neighbor)
                    neighbor = graph[neighbor].intersection(visited).pop()
                    if neighbor == node:
                        break
                return cycle

    # If we reach this point, there is no cycle
    return []

