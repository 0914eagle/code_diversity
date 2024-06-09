
def solve(n, m, field):
    # Initialize a set to store the positions of walls
    walls = set()
    
    # Iterate over the field and add the positions of walls to the set
    for i in range(n):
        for j in range(m):
            if field[i][j] == "*":
                walls.add((i, j))
    
    # Initialize a set to store the positions of rows and columns that contain walls
    rows = set()
    cols = set()
    
    # Iterate over the walls and add the positions of rows and columns that contain walls to the sets
    for wall in walls:
        rows.add(wall[0])
        cols.add(wall[1])
    
    # If the number of rows and columns that contain walls is equal to the total number of rows and columns, return "NO"
    if len(rows) == n and len(cols) == m:
        return "NO"
    
    # Initialize a variable to store the position of the cell at which the bomb should be laid
    bomb_position = None
    
    # Iterate over the rows and columns that contain walls
    for row in rows:
        for col in cols:
            # If the cell at the current row and column is empty, set the bomb position to that cell
            if field[row][col] == ".":
                bomb_position = (row, col)
                break
    
    # If the bomb position is not None, return "YES" and the bomb position
    if bomb_position is not None:
        return "YES\n" + str(bomb_position[0]) + " " + str(bomb_position[1])
    
    # If the bomb position is None, return "NO"
    return "NO"

