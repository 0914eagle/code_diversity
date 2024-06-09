
def f1(n, m, field):
    # Initialize variables
    moves = 0
    dwarves = []
    candy_cells = []
    
    # Parse the field
    for i in range(n):
        for j in range(m):
            if field[i][j] == "G":
                dwarves.append((i, j))
            elif field[i][j] == "S":
                candy_cells.append((i, j))
    
    # Check if the goal can be achieved
    if len(dwarves) == 0 or len(candy_cells) == 0:
        return -1
    
    # Game loop
    while dwarves:
        # Choose lines where dwarves are not on candy cells
        lines = set()
        for dwarf in dwarves:
            lines.add(dwarf[0])
        
        # Move dwarves to the right
        for line in lines:
            for i in range(m):
                for dwarf in dwarves:
                    if dwarf[0] == line and dwarf[1] == i:
                        dwarf[1] += 1
                        break
        
        # Check if any dwarf reached the candy cell
        for dwarf in dwarves:
            for candy_cell in candy_cells:
                if dwarf[0] == candy_cell[0] and dwarf[1] == candy_cell[1]:
                    dwarves.remove(dwarf)
                    break
        
        # Check if any dwarf reached the rightmost cell
        for dwarf in dwarves:
            if dwarf[1] == m - 1:
                return -1
        
        moves += 1
    
    return moves

def f2(n, m, field):
    # Initialize variables
    moves = 0
    dwarves = []
    candy_cells = []
    
    # Parse the field
    for i in range(n):
        for j in range(m):
            if field[i][j] == "G":
                dwarves.append((i, j))
            elif field[i][j] == "S":
                candy_cells.append((i, j))
    
    # Check if the goal can be achieved
    if len(dwarves) == 0 or len(candy_cells) == 0:
        return -1
    
    # Game loop
    while dwarves:
        # Choose lines where dwarves are not on candy cells
        lines = set()
        for dwarf in dwarves:
            lines.add(dwarf[0])
        
        # Move dwarves to the right
        for line in lines:
            for i in range(m):
                for dwarf in dwarves:
                    if dwarf[0] == line and dwarf[1] == i:
                        dwarf[1] += 1
                        break
        
        # Check if any dwarf reached the candy cell
        for dwarf in dwarves:
            for candy_cell in candy_cells:
                if dwarf[0] == candy_cell[0] and dwarf[1] == candy_cell[1]:
                    dwarves.remove(dwarf)
                    break
        
        # Check if any dwarf reached the rightmost cell
        for dwarf in dwarves:
            if dwarf[1] == m - 1:
                return -1
        
        moves += 1
    
    return moves

if __name__ == '__main__':
    n, m = map(int, input().split())
    field = []
    for i in range(n):
        field.append(list(input()))
    print(f1(n, m, field))
    print(f2(n, m, field))

