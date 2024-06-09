
def solve(n, m, field):
    # Initialize a set to store the coordinates of the walls
    walls = set()
    
    # Iterate over the field and add the coordinates of the walls to the set
    for i in range(n):
        for j in range(m):
            if field[i][j] == "*":
                walls.add((i, j))
    
    # Initialize a set to store the coordinates of the rows and columns that contain walls
    rows = set()
    cols = set()
    
    # Iterate over the walls and add the coordinates of the rows and columns that contain walls to the sets
    for wall in walls:
        rows.add(wall[0])
        cols.add(wall[1])
    
    # Check if there is a row and column that contain all walls
    for row in rows:
        for col in cols:
            if (row, col) in walls:
                return "YES\n" + str(row) + " " + str(col)
    
    return "NO"

