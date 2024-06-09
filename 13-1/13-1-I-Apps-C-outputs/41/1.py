
def f1(N, K, items):
    # Initialize a graph with N nodes and no edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the items available at each store
    for i, item in items:
        graph[i].append(item)

    # Return the graph
    return graph

def f2(graph, items):
    # Initialize a set to keep track of the items that have been bought
    bought_items = set()

    # Initialize a queue to keep track of the nodes to visit
    queue = [0]

    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)

        # If the node is a store and it has items that have not been bought, add them to the set of bought items
        if node < len(graph) and graph[node]:
            bought_items.update(graph[node])

        # Add the neighbors of the current node to the queue
        queue.extend(graph[node])

    # If all items have been bought, return "unique"
    if bought_items == set(items):
        return "unique"

    # If not all items have been bought, return "impossible"
    return "impossible"

if __name__ == '__main__':
    N, K = map(int, input().split())
    items = [tuple(input().split()) for _ in range(K)]
    graph = f1(N, K, items)
    print(f2(graph, items))

