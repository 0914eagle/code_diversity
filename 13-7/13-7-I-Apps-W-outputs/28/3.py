
def count_ways(field):
    # Initialize the number of ways to be 0
    ways = 0
    
    # Loop through each cell in the field
    for i in range(len(field)):
        # If the cell contains a bomb, skip it
        if field[i] == "*":
            continue
        # If the cell is empty, count the number of ways to fill it
        if field[i] == "?":
            # Get the number of bombs in the adjacent cells
            num_bombs = count_bombs(field, i)
            # If the number of bombs is 0, 1, or 2, increment the number of ways
            if num_bombs in [0, 1, 2]:
                ways += 1
    
    # Return the number of ways
    return ways

def count_bombs(field, i):
    # Initialize the number of bombs to 0
    bombs = 0
    
    # Loop through the adjacent cells
    for j in range(i-1, i+2):
        # If the cell is out of range, skip it
        if j < 0 or j >= len(field):
            continue
        # If the cell contains a bomb, increment the number of bombs
        if field[j] == "*":
            bombs += 1
    
    # Return the number of bombs
    return bombs

if __name__ == '__main__':
    field = input()
    print(count_ways(field))

