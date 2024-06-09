
def solve(n, m, field):
    # Initialize a set to store the positions of walls
    walls = set()
    
    # Iterate over the field and add the positions of walls to the set
    for i in range(n):
        for j in range(m):
            if field[i][j] == "*":
                walls.add((i, j))
    
    # Initialize a set to store the positions of rows and columns that have at least one wall
    rows = set()
    cols = set()
    
    # Iterate over the walls and add the positions of rows and columns that have at least one wall to the sets
    for wall in walls:
        rows.add(wall[0])
        cols.add(wall[1])
    
    # Check if there is a row and a column that have at least one wall each
    if len(rows) == 1 and len(cols) == 1:
        # If there is such a row and a column, return the coordinates of the cell at which the bomb should be laid
        return "YES\n" + str(list(rows)[0]) + " " + str(list(cols)[0])
    
    # If there is no such row and a column, return "NO"
    return "NO"

