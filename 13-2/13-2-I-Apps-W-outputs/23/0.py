
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
    
    # Check if there is a row and a column that contain all walls
    for row in rows:
        for col in cols:
            if (row, col) in walls:
                return "YES", (row, col)
    
    return "NO", (0, 0)

