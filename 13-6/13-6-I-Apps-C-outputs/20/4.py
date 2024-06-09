
def is_cube_foldable(squares):
    # Check if the input is valid
    if len(squares) != 6 or any(len(row) != 6 for row in squares):
        return "invalid input"
    
    # Check if there are 6 unit squares
    if squares.count("#") != 6:
        return "cannot fold"
    
    # Check if the unit squares form a connected component
    if not is_connected(squares):
        return "cannot fold"
    
    # Check if the unit squares can be folded into a cube
    if not can_fold(squares):
        return "cannot fold"
    
    return "can fold"

def is_connected(squares):
    # Check if all the unit squares are connected
    for i in range(6):
        for j in range(6):
            if squares[i][j] == "#":
                if not is_connected_helper(squares, i, j):
                    return False
    return True

def is_connected_helper(squares, i, j):
    # Base case: if we reach a border, return True
    if i < 0 or j < 0 or i >= 6 or j >= 6:
        return True
    
    # If the current square is empty, return True
    if squares[i][j] == ".":
        return True
    
    # If the current square is a unit square, mark it as visited and recurse on the surrounding squares
    if squares[i][j] == "#":
        squares[i][j] = "*"
        return is_connected_helper(squares, i-1, j) and is_connected_helper(squares, i+1, j) and is_connected_helper(squares, i, j-1) and is_connected_helper(squares, i, j+1)
    
    # If the current square is a visited unit square, return True
    if squares[i][j] == "*":
        return True

def can_fold(squares):
    # Check if the unit squares can be folded into a cube
    for i in range(6):
        for j in range(6):
            if squares[i][j] == "#":
                if not can_fold_helper(squares, i, j):
                    return False
    return True

def can_fold_helper(squares, i, j):
    # Base case: if we reach a border, return True
    if i < 0 or j < 0 or i >= 6 or j >= 6:
        return True
    
    # If the current square is empty, return True
    if squares[i][j] == ".":
        return True
    
    # If the current square is a unit square, mark it as visited and recurse on the surrounding squares
    if squares[i][j] == "#":
        squares[i][j] = "*"
        return can_fold_helper(squares, i-1, j) and can_fold_helper(squares, i+1, j) and can_fold_helper(squares, i, j-1) and can_fold_helper(squares, i, j+1)
    
    # If the current square is a visited unit square, return True
    if squares[i][j] == "*":
        return True

if __name__ == '__main__':
    squares = [input() for _ in range(6)]
    print(is_cube_foldable(squares))

