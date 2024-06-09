
def solve_lava_game(elsa_step_length, father_step_length, map_width, map_height, map_data):
    # Initialize the starting position of Elsa and the father
    elsa_position = (0, 0)
    father_position = (0, 0)
    
    # Initialize the set of safe tiles
    safe_tiles = set()
    
    # Loop through the map data and add the safe tiles to the set
    for i in range(map_height):
        for j in range(map_width):
            if map_data[i][j] == "W":
                safe_tiles.add((i, j))
    
    # Initialize the set of visited tiles
    visited_tiles = set()
    
    # Loop through the map data and add the visited tiles to the set
    for i in range(map_height):
        for j in range(map_width):
            visited_tiles.add((i, j))
    
    # Initialize the minimum distance between Elsa and the goal
    min_distance = float("inf")
    
    # Loop through the map data and find the minimum distance between Elsa and the goal
    for i in range(map_height):
        for j in range(map_width):
            if map_data[i][j] == "G":
                distance = abs(i - elsa_position[0]) + abs(j - elsa_position[1])
                if distance < min_distance:
                    min_distance = distance
    
    # If Elsa can reach the goal within her step length, return "GO FOR IT"
    if min_distance <= elsa_step_length:
        return "GO FOR IT"
    
    # If the father can reach the goal within his step length, return "NO CHANCE"
    if min_distance <= father_step_length:
        return "NO CHANCE"
    
    # If neither Elsa nor the father can reach the goal, return "NO WAY"
    return "NO WAY"

