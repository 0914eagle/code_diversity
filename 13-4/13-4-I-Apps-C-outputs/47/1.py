
def solve_tomb_raider_puzzle(n, m, floorplan):
    # Initialize a dictionary to store the number of gargoyles that need to be rotated for each cell
    gargoyles_needed = {}
    
    # Loop through each cell in the floorplan
    for i in range(n):
        for j in range(m):
            # If the cell is a gargoyle, add it to the dictionary with the number of gargoyles needed to be rotated as the value
            if floorplan[i][j] in ["V", "H"]:
                gargoyles_needed[(i, j)] = 1
    
    # Loop through each cell in the floorplan again
    for i in range(n):
        for j in range(m):
            # If the cell is not a gargoyle or an obstacle, continue to the next cell
            if floorplan[i][j] not in ["V", "H", "#"]:
                continue
            
            # If the cell is a gargoyle or an obstacle, check if it is connected to any other gargoyles or obstacles
            if floorplan[i][j] in ["V", "H"] or floorplan[i][j] == "#":
                # If the cell is connected to any other gargoyles or obstacles, add the number of gargoyles needed to be rotated for that cell to the total number of gargoyles needed
                if (i, j) in gargoyles_needed:
                    gargoyles_needed[(i, j)] += 1
    
    # Return the minimum number of gargoyles needed to be rotated
    return min(gargoyles_needed.values()) if gargoyles_needed else -1

