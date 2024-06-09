
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

        # If the node is a store and all the items have been bought, return "unique"
        if node in range(len(graph)) and len(bought_items) == len(items):
            return "unique"

        # If the node is an item and it has not been bought, buy it and add it to the set of bought items
        if node in items and node not in bought_items:
            bought_items.add(node)

        # Add the neighbors of the current node to the queue
        queue += graph[node]

    # If all the items have been bought, return "unique"
    if len(bought_items) == len(items):
        return "unique"

    # Otherwise, return "impossible"
    return "impossible"

if __name__ == '__main__':
    N, K = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(K)]
    graph = f1(N, K, items)
    result = f2(graph, items)
    print(result)

