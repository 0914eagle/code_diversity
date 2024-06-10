
def read_input():
    n, m, d = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    return n, m, d, matrix

def solve(n, m, d, matrix):
    # Initialize variables
    min_moves = 0
    target = matrix[0][0]
    visited = set()

    # Breadth-first search
    queue = [(0, 0, 0)]
    while queue:
        row, col, moves = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if matrix[row][col] == target:
            min_moves = max(min_moves, moves)
        else:
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < n and 0 <= c < m and matrix[r][c] + d == target:
                    queue.append((r, c, moves+1))

    return min_moves if min_moves != 0 else -1

def main():
    n, m, d, matrix = read_input()
    print(solve(n, m, d, matrix))

if __name__ == '__main__':
    main()

