
def get_min_messages(spies, enemies, connections):
    # Initialize a graph with the given connections
    graph = {i: set() for i in range(spies)}
    for connection in connections:
        graph[connection[0]].add(connection[1])
        graph[connection[1]].add(connection[0])
    
    # Initialize a set to keep track of visited spies
    visited = set()
    
    # Initialize a queue to do a BFS traversal of the graph
    queue = [0]
    
    # Do a BFS traversal of the graph starting from spy 0
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            queue += list(graph[current])
    
    # Return the number of spies in the visited set, which is the minimum number of messages needed to send the information to all spies in the network
    return len(visited)

def main():
    spies, enemies, connections = map(int, input().split())
    connections = [tuple(map(int, input().split())) for _ in range(connections)]
    enemies = set(map(int, input().split()))
    print(get_min_messages(spies, enemies, connections))

if __name__ == '__main__':
    main()

