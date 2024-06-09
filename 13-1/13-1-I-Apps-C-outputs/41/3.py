
def f1(N, K, items):
    # Initialize a graph with N nodes and no edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the items available at each store
    for i, item in items:
        graph[i].append(item)

    # Return the graph
    return graph

def f2(graph, items):
    # Initialize a set to store the items that have been bought
    bought_items = set()

    # Initialize a queue to store the nodes to visit
    queue = [0]

    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)

        # If the node is a bought item, add it to the set of bought items
        if node in items:
            bought_items.add(node)

        # If the node has not been visited yet, mark it as visited and add its neighbors to the queue
        if node not in graph[node]:
            graph[node].append(node)
            queue += graph[node]

    # If all items have been bought, return "unique"
    if len(bought_items) == len(items):
        return "unique"

    # If not all items have been bought, return "impossible"
    return "impossible"

if __name__ == '__main__':
    N, K = map(int, input().split())
    items = [input().split() for _ in range(K)]
    graph = f1(N, K, items)
    print(f2(graph, items))

