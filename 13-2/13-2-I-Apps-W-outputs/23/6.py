
def solve(n, m, field):
    # Initialize a set to store the positions of the walls
    walls = set()
    
    # Iterate over the field and add the positions of the walls to the set
    for i in range(n):
        for j in range(m):
            if field[i][j] == "*":
                walls.add((i, j))
    
    # Initialize a set to store the positions of the rows and columns that contain walls
    rows = set()
    cols = set()
    
    # Iterate over the walls and add the positions of the rows and columns that contain walls to the sets
    for wall in walls:
        rows.add(wall[0])
        cols.add(wall[1])
    
    # If the number of rows and columns that contain walls is equal to the total number of rows and columns, return "NO"
    if len(rows) == n and len(cols) == m:
        return "NO"
    
    # Initialize a variable to store the position of the cell at which the bomb should be laid
    bomb_position = None
    
    # Iterate over the walls and find a cell that is not in a row or column that contains a wall
    for wall in walls:
        if wall[0] not in rows and wall[1] not in cols:
            bomb_position = wall
            break
    
    # If a cell has been found, return "YES" and the position of the cell
    if bomb_position:
        return "YES\n" + str(bomb_position[0]) + " " + str(bomb_position[1])
    
    # If no cell has been found, return "NO"
    return "NO"

