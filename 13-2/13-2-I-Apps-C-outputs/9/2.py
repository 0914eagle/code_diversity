
def solve_lava_game(ela_step_length, father_step_length, map_width, map_height, map_data):
    # Initialize the starting position of Elsa and the father
    ela_position = (0, 0)
    father_position = (0, 0)
    
    # Initialize the visited matrix to keep track of the tiles that have been visited
    visited = [[False for _ in range(map_width)] for _ in range(map_height)]
    
    # Initialize the queue to keep track of the tiles to be visited
    queue = [(ela_position, father_position)]
    
    # Loop through the queue until it is empty
    while queue:
        # Get the current position of Elsa and the father
        ela_position, father_position = queue.pop(0)
        
        # If both Elsa and the father have reached the goal, return "SUCCESS"
        if ela_position == (map_width - 1, map_height - 1) and father_position == (map_width - 1, map_height - 1):
            return "SUCCESS"
        
        # If Elsa has reached the goal and the father has not, return "GO FOR IT"
        if ela_position == (map_width - 1, map_height - 1) and father_position != (map_width - 1, map_height - 1):
            return "GO FOR IT"
        
        # If the father has reached the goal and Elsa has not, return "NO CHANCE"
        if father_position == (map_width - 1, map_height - 1) and ela_position != (map_width - 1, map_height - 1):
            return "NO CHANCE"
        
        # If both Elsa and the father are not at the goal, find the next positions for them to visit
        ela_next_position = (ela_position[0] + ela_step_length, ela_position[1] + ela_step_length)
        father_next_position = (father_position[0] + father_step_length, father_position[1] + father_step_length)
        
        # If both Elsa and the father are not at the goal and the next positions are valid, add them to the queue
        if ela_next_position[0] >= 0 and ela_next_position[0] < map_width and ela_next_position[1] >= 0 and ela_next_position[1] < map_height and not visited[ela_next_position[0]][ela_next_position[1]]:
            queue.append((ela_next_position, father_position))
            visited[ela_next_position[0]][ela_next_position[1]] = True
        if father_next_position[0] >= 0 and father_next_position[0] < map_width and father_next_position[1] >= 0 and father_next_position[1] < map_height and not visited[father_next_position[0]][father_next_position[1]]:
            queue.append((ela_position, father_next_position))
            visited[father_next_position[0]][father_next_position[1]] = True
    
    # If neither Elsa nor the father has reached the goal, return "NO WAY"
    return "NO WAY"

