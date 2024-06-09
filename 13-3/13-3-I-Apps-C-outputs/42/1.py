
def is_reachable(start_config, target_config):
    # Initialize a queue to store the positions of the pegs to be checked
    queue = []
    
    # Initialize a set to store the positions of the pegs that have been checked
    checked = set()
    
    # Add the starting configuration to the queue
    queue.append(start_config)
    
    # Loop until the queue is empty
    while queue:
        # Get the current configuration from the queue
        config = queue.pop(0)
        
        # If the current configuration is the target configuration, return True
        if config == target_config:
            return True
        
        # Get the positions of the pegs that are up in the current configuration
        up_positions = [i for i, peg in enumerate(config) if peg == "O"]
        
        # Loop through each up peg and check if it can be hammered
        for position in up_positions:
            # If the peg has already been checked, skip it
            if position in checked:
                continue
            
            # Add the position to the checked set
            checked.add(position)
            
            # Create a new configuration by hammering the peg
            new_config = list(config)
            new_config[position] = "X"
            new_config = "".join(new_config)
            
            # Add the new configuration to the queue
            queue.append(new_config)
    
    # If the queue is empty and the target configuration has not been reached, return False
    return False

def main():
    r, c = map(int, input().split())
    start_config = input()
    target_config = input()
    print(is_reachable(start_config, target_config))

if __name__ == '__main__':
    main()

