
def can_fold(squares):
    # Check if the input is valid
    if len(squares) != 6 or any(len(row) != 6 for row in squares):
        return "Invalid input"
    
    # Count the number of unit squares
    num_unit_squares = sum(row.count("#") for row in squares)
    if num_unit_squares != 6:
        return "Invalid input"
    
    # Check if the input forms a connected component
    visited = set()
    queue = [(0, 0)]
    while queue:
        row, col = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if squares[row][col] == "#":
            queue.extend([(row-1, col), (row+1, col), (row, col-1), (row, col+1)])
    
    if len(visited) != 6:
        return "Cannot fold"
    
    # Check if the input forms a cube
    for row in range(6):
        for col in range(6):
            if squares[row][col] == "#":
                if any(squares[row+1][col] != "#" or squares[row-1][col] != "#" or squares[row][col+1] != "#" or squares[row][col-1] != "#" for row in range(6)):
                    return "Cannot fold"
    
    return "Can fold"

def main():
    squares = [input() for _ in range(6)]
    print(can_fold(squares))

if __name__ == '__main__':
    main()

