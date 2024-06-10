
def is_possible(n, m, k, capacities, existing_connections):
    # Initialize a graph with the given number of nodes and edges
    graph = Graph(n)

    # Add the existing connections to the graph
    for u, v in existing_connections:
        graph.add_edge(u, v)

    # Initialize a set to keep track of the edited nodes
    edited_nodes = set()

    # Loop through each node and try to find a path to all other nodes
    for node in range(n):
        if node in edited_nodes:
            continue

        # Find a path to all other nodes from the current node
        path = graph.find_path(node, edited_nodes)

        # If a path cannot be found, return "no"
        if path is None:
            return "no"

        # Add the current node to the set of edited nodes
        edited_nodes.add(node)

        # If the number of edited nodes is greater than the number of available edits, return "no"
        if len(edited_nodes) > k:
            return "no"

    # If all nodes can be reached from each other, return "yes"
    return "yes"

class Graph:
    def __init__(self, n):
        self.n = n
        self.adjacency_list = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def find_path(self, node, edited_nodes):
        # Base case: if the node is the destination node, return the path
        if node == self.n - 1:
            return [node]

        # Recursive case: try to find a path to the destination node from the current node
        for neighbor in self.adjacency_list[node]:
            if neighbor not in edited_nodes:
                path = self.find_path(neighbor, edited_nodes)
                if path is not None:
                    return [node] + path

        # If no path can be found, return None
        return None

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    capacities = list(map(int, input().split()))
    existing_connections = []
    for _ in range(m):
        u, v = map(int, input().split())
        existing_connections.append((u, v))
    print(is_possible(n, m, k, capacities, existing_connections))

