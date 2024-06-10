
def get_people_left_behind(people_to_cross, boulders, logs):
    # Initialize a graph with the boulders as nodes and the logs as edges
    graph = {i: set() for i in range(-2, boulders)}
    for log in logs:
        graph[log[0]].add(log[1])
        graph[log[1]].add(log[0])
    
    # Create a queue to store the nodes to visit
    queue = [(0, -2)]
    
    # Keep track of the time it takes to cross each log
    time_taken = {log: 1 for log in logs}
    
    # Keep track of the people who have crossed the river
    people_crossed = set()
    
    # Loop until all people have crossed the river
    while queue and len(people_crossed) < people_to_cross:
        # Get the current node and time from the queue
        current_node, current_time = queue.pop(0)
        
        # If the current node is a boulder, add it to the people who have crossed the river
        if current_node >= 0:
            people_crossed.add(current_node)
        
        # Add the neighbors of the current node to the queue
        for neighbor in graph[current_node]:
            queue.append((current_time + time_taken[neighbor], neighbor))
    
    # Return the number of people who were left behind
    return people_to_cross - len(people_crossed)

def get_min_time(people_to_cross, boulders, logs):
    # Initialize a graph with the boulders as nodes and the logs as edges
    graph = {i: set() for i in range(-2, boulders)}
    for log in logs:
        graph[log[0]].add(log[1])
        graph[log[1]].add(log[0])
    
    # Create a queue to store the nodes to visit
    queue = [(0, -2)]
    
    # Keep track of the time it takes to cross each log
    time_taken = {log: 1 for log in logs}
    
    # Keep track of the people who have crossed the river
    people_crossed = set()
    
    # Loop until all people have crossed the river
    while queue and len(people_crossed) < people_to_cross:
        # Get the current node and time from the queue
        current_node, current_time = queue.pop(0)
        
        # If the current node is a boulder, add it to the people who have crossed the river
        if current_node >= 0:
            people_crossed.add(current_node)
        
        # Add the neighbors of the current node to the queue
        for neighbor in graph[current_node]:
            queue.append((current_time + time_taken[neighbor], neighbor))
    
    # Return the total time it took to cross the river
    return current_time

if __name__ == '__main__':
    people_to_cross, boulders, logs = map(int, input().split())
    logs = [list(map(int, input().split())) for _ in range(logs)]
    print(get_min_time(people_to_cross, boulders, logs))

