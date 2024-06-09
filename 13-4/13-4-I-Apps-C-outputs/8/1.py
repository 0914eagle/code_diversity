
def get_min_turns(intersections, alice_intersection, bob_intersection):
    # Initialize a dictionary to store the minimum number of turns to reach each intersection from the starting intersection
    min_turns = {alice_intersection: 0, bob_intersection: 0}
    
    # Initialize a queue to perform BFS
    queue = [alice_intersection, bob_intersection]
    
    # Loop until the queue is empty
    while queue:
        # Dequeue an intersection from the queue
        current_intersection = queue.pop(0)
        
        # Get the left and right intersections from the current intersection
        left_intersection = intersections[current_intersection][0]
        right_intersection = intersections[current_intersection][1]
        
        # If the left intersection has not been visited before, add it to the queue and update the minimum number of turns
        if left_intersection not in min_turns:
            min_turns[left_intersection] = min_turns[current_intersection] + 1
            queue.append(left_intersection)
        
        # If the right intersection has not been visited before, add it to the queue and update the minimum number of turns
        if right_intersection not in min_turns:
            min_turns[right_intersection] = min_turns[current_intersection] + 1
            queue.append(right_intersection)
    
    # Return the minimum number of turns to reach either intersection from the starting intersection
    return min(min_turns.values())

def main():
    # Read the input
    n, alice_intersection, bob_intersection = map(int, input().split())
    intersections = [list(map(int, input().split())) for _ in range(n)]
    
    # Call the function to get the minimum number of turns
    min_turns = get_min_turns(intersections, alice_intersection, bob_intersection)
    
    # Print the output
    print(min_turns)

if __name__ == '__main__':
    main()

