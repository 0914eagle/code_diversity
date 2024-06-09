
import sys

def get_winning_sequence(board):
    # Initialize variables
    n, m, p = len(board), len(board[0]), len(set(board[0]))
    visited = [[False] * m for _ in range(n)]
    queue = [(0, 0)]
    visited[0][0] = True
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Breadth-first search
    while queue:
        row, col = queue.pop(0)
        for d in direction:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < n and 0 <= new_col < m and not visited[new_row][new_col] and board[new_row][new_col] == p:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))
                if all(all(row) for row in visited):
                    break
        else:
            continue
        break

    # Construct the winning sequence
    sequence = []
    while not queue:
        row, col = queue.pop()
        sequence.append(row * m + col + 1)
        for d in direction:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < n and 0 <= new_col < m and visited[new_row][new_col] and board[new_row][new_col] != p:
                queue.append((new_row, new_col))
                break
        else:
            continue
    return sequence[::-1]

def main():
    n, m, p = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    sequence = get_winning_sequence(board)
    if sequence:
        print(len(sequence))
        print(*sequence)
    else:
        print(-1)

if __name__ == "__main__":
    main()

