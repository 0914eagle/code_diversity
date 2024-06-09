
def get_min_messages(spies, enemies, connections):
    # Initialize a graph with the given connections
    graph = {i: set() for i in range(spies)}
    for connection in connections:
        graph[connection[0]].add(connection[1])
        graph[connection[1]].add(connection[0])
    
    # Initialize a set to keep track of the spies that have received the message
    received = set()
    
    # Function to send the message to all spies in the graph
    def send_message(spy):
        nonlocal received
        received.add(spy)
        for neighbor in graph[spy]:
            if neighbor not in received:
                send_message(neighbor)
    
    # Send the message to all spies that are not enemies
    for spy in range(spies):
        if spy not in enemies:
            send_message(spy)
    
    # Return the number of spies that received the message
    return len(received)

def main():
    spies, enemies, connections = map(int, input().split())
    connections = [tuple(map(int, input().split())) for _ in range(connections)]
    enemies = set(map(int, input().split()))
    print(get_min_messages(spies, enemies, connections))

if __name__ == '__main__':
    main()

