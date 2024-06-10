
def get_penalty(n, m, k):
    # Initialize the matrix and the penalty
    matrix = [[0] * m for _ in range(n)]
    penalty = 0
    
    # Place the candies
    for i in range(k):
        # Find the next empty cell
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    break
            else:
                continue
            break
        
        # Place the candy in the cell
        matrix[row][col] = i + 1
        
        # Find the path from (1, 1) to (row, col)
        path = [(1, 1)]
        while (row, col) != (1, 1):
            for r, c in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
                if 0 <= r < n and 0 <= c < m and matrix[r][c] == 0:
                    break
            else:
                continue
            break
            path.append((r, c))
            row, col = r, c
        path.reverse()
        
        # Add the path to the penalty
        penalty += len(path)
    
    return penalty

def get_paths(n, m, k):
    # Initialize the matrix and the paths
    matrix = [[0] * m for _ in range(n)]
    paths = [[] for _ in range(k)]
    
    # Place the candies
    for i in range(k):
        # Find the next empty cell
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 0:
                    break
            else:
                continue
            break
        
        # Place the candy in the cell
        matrix[row][col] = i + 1
        
        # Find the path from (1, 1) to (row, col)
        path = [(1, 1)]
        while (row, col) != (1, 1):
            for r, c in [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]:
                if 0 <= r < n and 0 <= c < m and matrix[r][c] == 0:
                    break
            else:
                continue
            break
            path.append((r, c))
            row, col = r, c
        path.reverse()
        
        # Add the path to the paths
        paths[i] = path
    
    return paths

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    penalty = get_penalty(n, m, k)
    print(penalty)
    for path in get_paths(n, m, k):
        print(' '.join(map(str, path)))

