
def is_reachable(start_config, target_config):
    # Initialize a queue to store the positions of the pegs to be checked
    queue = []
    
    # Initialize a dictionary to keep track of the positions of the pegs that have been checked
    checked = {}
    
    # Add the starting configuration to the queue
    queue.append(start_config)
    
    # Loop until the queue is empty
    while queue:
        # Get the current configuration from the queue
        current_config = queue.pop(0)
        
        # If the current configuration is the target configuration, return True
        if current_config == target_config:
            return True
        
        # Get the positions of the pegs that are up in the current configuration
        up_positions = [i for i, peg in enumerate(current_config) if peg == "O"]
        
        # Loop through each up peg and check if it can be "hammered"
        for position in up_positions:
            # Get the row and column of the peg
            row, col = divmod(position, len(current_config))
            
            # Create a new configuration by "hammering" the peg
            new_config = list(current_config)
            new_config[position] = "X"
            
            # If the new configuration has not been checked before, add it to the queue
            if new_config not in checked:
                queue.append(new_config)
                checked[new_config] = True
    
    # If the queue is empty and the target configuration has not been reached, return False
    return False

def main():
    r, c = map(int, input().split())
    start_config = [input() for _ in range(r)]
    target_config = [input() for _ in range(r)]
    print(is_reachable(start_config, target_config))

if __name__ == '__main__':
    main()

