
def is_rectangle_possible(puzzle_piece):
    n, m = map(int, input().split())
    puzzle_piece = [input() for _ in range(n)]
    
    # Check if the puzzle piece is a rectangle
    if n != m:
        return "NO"
    
    # Check if the puzzle piece is a 4-connected region
    if not all(puzzle_piece[0][0] == 'X' for row in puzzle_piece for _ in row):
        return "NO"
    
    # Check if the puzzle piece can be moved to form a rectangle
    for i in range(n):
        for j in range(m):
            if puzzle_piece[i][j] == 'X':
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    return "NO"
                elif i > 0 and j == 0:
                    return "NO"
                elif puzzle_piece[i-1][j-1] != 'X':
                    return "NO"
    
    return "YES"

