
def get_min_moves(matrix, d):
    # Initialize variables
    rows, cols = len(matrix), len(matrix[0])
    min_moves = 0
    visited = set()
    queue = [(0, 0, 0)]

    # Loop through the queue
    while queue:
        row, col, moves = queue.pop(0)

        # Check if the current cell is already visited
        if (row, col) in visited:
            continue

        # Check if the current cell is the last cell
        if row == rows - 1 and col == cols - 1:
            return moves

        # Mark the current cell as visited
        visited.add((row, col))

        # Add the current cell to the queue
        queue.append((row, col + 1, moves))
        queue.append((row + 1, col, moves))

        # Check if the current cell can be modified
        if matrix[row][col] % d == 0:
            continue

        # Modify the current cell
        matrix[row][col] += d
        min_moves += 1

    # If the queue is empty, it means that it is not possible to make all the elements equal
    return -1

def main():
    # Read the input
    n, m, d = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # Get the minimum number of moves
    min_moves = get_min_moves(matrix, d)

    # Print the result
    print(min_moves)

if __name__ == '__main__':
    main()

