
def get_min_messages(spies, enemies, connections):
    # Initialize a graph with the given connections
    graph = {i: set() for i in range(spies)}
    for connection in connections:
        graph[connection[0]].add(connection[1])
        graph[connection[1]].add(connection[0])
    
    # Initialize a set to keep track of the enemies
    enemy_set = set(enemies)
    
    # Initialize a queue to do a BFS traversal of the graph
    queue = [0]
    
    # Initialize a dictionary to keep track of the number of messages sent to each spy
    message_count = {0: 0}
    
    while queue:
        # Dequeue a spy from the queue
        current_spy = queue.pop(0)
        
        # If the current spy is an enemy, skip them
        if current_spy in enemy_set:
            continue
        
        # If the current spy has not been visited before, mark them as visited and add them to the queue
        if current_spy not in message_count:
            message_count[current_spy] = 0
            queue += list(graph[current_spy])
        
        # Increment the message count for the current spy
        message_count[current_spy] += 1
    
    # Return the minimum number of messages needed to send to all spies
    return max(message_count.values())

def main():
    spies, enemies, connections = map(int, input().split())
    connections = [tuple(map(int, input().split())) for _ in range(connections)]
    enemies = set(map(int, input().split()))
    print(get_min_messages(spies, enemies, connections))

if __name__ == '__main__':
    main()

