
def is_rectangle_possible(puzzle_piece):
    n, m = map(int, input().split())
    puzzle_piece = [input() for _ in range(n)]
    
    # Check if the puzzle piece is a 4-connected region
    if not is_4_connected(puzzle_piece):
        return "NO"
    
    # Check if the puzzle piece can be rotated to form a rectangle
    if can_rotate_to_rectangle(puzzle_piece):
        return "YES"
    
    # Check if the puzzle piece can be flipped to form a rectangle
    if can_flip_to_rectangle(puzzle_piece):
        return "YES"
    
    # Check if the puzzle piece can be shifted to form a rectangle
    if can_shift_to_rectangle(puzzle_piece):
        return "YES"
    
    return "NO"

def is_4_connected(puzzle_piece):
    n, m = len(puzzle_piece), len(puzzle_piece[0])
    visited = [[False] * m for _ in range(n)]
    queue = [(0, 0)]
    visited[0][0] = True
    
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and puzzle_piece[ni][nj] == 'X':
                visited[ni][nj] = True
                queue.append((ni, nj))
    
    return visited[n - 1][m - 1]

def can_rotate_to_rectangle(puzzle_piece):
    n, m = len(puzzle_piece), len(puzzle_piece[0])
    for i in range(n):
        for j in range(m):
            if puzzle_piece[i][j] == 'X':
                break
        else:
            continue
        break
    
    for j in range(m):
        for i in range(n):
            if puzzle_piece[i][j] == 'X':
                break
        else:
            continue
        break
    
    return i == n - 1 and j == m - 1

def can_flip_to_rectangle(puzzle_piece):
    n, m = len(puzzle_piece), len(puzzle_piece[0])
    for i in range(n):
        for j in range(m):
            if puzzle_piece[i][j] == 'X':
                break
        else:
            continue
        break
    
    for j in range(m):
        for i in range(n):
            if puzzle_piece[i][j] == 'X':
                break
        else:
            continue
        break
    
    return i == n - 1 and j == m - 1

def can_shift_to_rectangle(puzzle_piece):
    n, m = len(puzzle_piece), len(puzzle_piece[0])
    for i in range(n):
        for j in range(m):
            if puzzle_piece[i][j] == 'X':
                break
        else:
            continue
        break
    
    for j in range(m):
        for i in range(n):
            if puzzle_piece[i][j] == 'X':
                break
        else:
            continue
        break
    
    return i == n - 1 and j == m - 1

if __name__ == "__main__":
    print(is_rectangle_possible(puzzle_piece))

