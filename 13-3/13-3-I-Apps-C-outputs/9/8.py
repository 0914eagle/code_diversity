
def f1(S, E, C, connections, enemies):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(S)]

    # Add edges to the graph
    for i in range(C):
        graph[connections[i][0]].append(connections[i][1])
        graph[connections[i][1]].append(connections[i][0])

    # Initialize a set to store the enemies
    enemy_set = set(enemies)

    # Initialize a queue to store the nodes to be visited
    queue = [0]

    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a variable to store the number of messages
    messages = 0

    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)

        # If the node is not visited, mark it as visited and increment the number of messages
        if node not in visited:
            visited.add(node)
            messages += 1

            # If the node is an enemy, do not add its neighbors to the queue
            if node in enemy_set:
                continue

            # Add the neighbors of the node to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return messages

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    S, E, C = map(int, input().split())
    connections = []
    for _ in range(C):
        connections.append(list(map(int, input().split())))
    enemies = list(map(int, input().split()))
    print(f1(S, E, C, connections, enemies))

