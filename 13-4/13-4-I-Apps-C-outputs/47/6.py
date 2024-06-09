
def solve_tomb_puzzle(n, m, floorplan):
    # Initialize a list to store the gargoyles' positions
    gargoyles = []
    
    # Loop through each row of the floorplan
    for i in range(n):
        # Loop through each column of the floorplan
        for j in range(m):
            # If the current cell is a gargoyle, add its position to the list of gargoyles
            if floorplan[i][j] in ["V", "H"]:
                gargoyles.append((i, j))
    
    # Initialize a variable to store the minimum number of gargoyles that need to be rotated
    min_rotations = float("inf")
    
    # Loop through each possible rotation of the gargoyles
    for rotation in range(4):
        # Initialize a variable to store the number of gargoyles that are currently connected
        connected_gargoyles = 0
        
        # Loop through each gargoyle and its neighboring gargoyles
        for i in range(len(gargoyles)):
            # Get the current gargoyle's position
            curr_gargoyle = gargoyles[i]
            
            # Get the position of the neighboring gargoyle
            neighbor_gargoyle = gargoyles[(i + 1) % len(gargoyles)]
            
            # If the current gargoyle and its neighbor are connected, increase the number of connected gargoyles
            if are_connected(curr_gargoyle, neighbor_gargoyle, floorplan, rotation):
                connected_gargoyles += 1
        
        # If all gargoyles are connected, update the minimum number of rotations required
        if connected_gargoyles == len(gargoyles):
            min_rotations = min(min_rotations, rotation)
    
    # Return the minimum number of rotations required to solve the puzzle
    return min_rotations if min_rotations < float("inf") else -1

# Check if two gargoyles are connected
def are_connected(gargoyle1, gargoyle2, floorplan, rotation):
    # Get the positions of the two gargoyles
    pos1 = gargoyle1
    pos2 = gargoyle2
    
    # If the two gargoyles are the same, return True
    if pos1 == pos2:
        return True
    
    # Get the direction of the gargoyles' faces
    face1 = floorplan[pos1[0]][pos1[1]]
    face2 = floorplan[pos2[0]][pos2[1]]
    
    # If the two gargoyles are facing each other, return False
    if face1 == face2:
        return False
    
    # Get the direction of the beam of light
    light_dir = (pos2[0] - pos1[0], pos2[1] - pos1[1])
    
    # If the beam of light is blocked by an obstacle, return False
    if any(floorplan[pos1[0] + light_dir[0] * i][pos1[1] + light_dir[1] * i] == "#" for i in range(1, abs(light_dir[0]) + abs(light_dir[1]))):
        return False
    
    # If the beam of light is reflected by a mirror, update the direction of the beam
    if floorplan[pos1[0] + light_dir[0]][pos1[1] + light_dir[1]] in ["/", "\\"]:
        light_dir = (-light_dir[1], light_dir[0])
    
    # If the beam of light is blocked by an obstacle or a gargoyle, return False
    if any(floorplan[pos1[0] + light_dir[0] * i][pos1[1] + light_dir[1] * i] in ["#", "V", "H"] for i in range(1, abs(light_dir[0]) + abs(light_dir[1]))):
        return False
    
    # If the beam of light reaches the second gargoyle, return True
    return floorplan[pos2[0] + light_dir[0]][pos2[1] + light_dir[1]] == "."

