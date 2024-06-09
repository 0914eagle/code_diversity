
def get_min_moves(n, bombs):
    # Initialize a dictionary to store the positions of the bombs
    bomb_positions = {}
    for i in range(len(bombs)):
        bomb_positions[i] = (bombs[i][0], bombs[i][1])
    
    # Initialize a queue to store the positions of the bombs that need to be moved
    queue = []
    for position in bomb_positions.values():
        if position in [(1, 1), (1, n), (n, 1), (n, n)]:
            continue
        queue.append(position)
    
    # Initialize a set to store the positions of the bombs that have been moved
    moved_bombs = set()
    
    # Initialize a variable to store the minimum number of moves required
    min_moves = 0
    
    # Loop until the queue is empty
    while queue:
        # Get the current position of the bomb from the queue
        current_position = queue.pop(0)
        
        # Check if the current position is already in the moved_bombs set
        if current_position in moved_bombs:
            continue
        
        # Add the current position to the moved_bombs set
        moved_bombs.add(current_position)
        
        # Get the four possible positions of the bombs that can be moved from the current position
        possible_positions = [(current_position[0] + 1, current_position[1]),
                              (current_position[0] - 1, current_position[1]),
                              (current_position[0], current_position[1] + 1),
                              (current_position[0], current_position[1] - 1)]
        
        # Loop through the possible positions and add them to the queue if they are not already in the moved_bombs set
        for position in possible_positions:
            if position not in moved_bombs and position not in queue:
                queue.append(position)
        
        # Increment the minimum number of moves required
        min_moves += 1
    
    # Return the minimum number of moves required
    return min_moves

def main():
    n, b = map(int, input().split())
    bombs = []
    for i in range(b):
        x, y = map(int, input().split())
        bombs.append((x, y))
    print(get_min_moves(n, bombs))

if __name__ == '__main__':
    main()

