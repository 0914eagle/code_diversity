
def get_next_state(current_state, direction):
    # Initialize the next state with the current state
    next_state = current_state.copy()

    # Get the number of rows and columns in the grid
    num_rows, num_cols = len(current_state), len(current_state[0])

    # Loop through each row and column
    for i in range(num_rows):
        for j in range(num_cols):
            # Check if the current cell is empty
            if current_state[i][j] == 0:
                continue

            # Get the coordinates of the current cell
            curr_row, curr_col = i, j

            # Get the coordinates of the next cell in the given direction
            if direction == 0:  # left
                next_row, next_col = curr_row, curr_col - 1
            elif direction == 1:  # up
                next_row, next_col = curr_row - 1, curr_col
            elif direction == 2:  # right
                next_row, next_col = curr_row, curr_col + 1
            elif direction == 3:  # down
                next_row, next_col = curr_row + 1, curr_col

            # Check if the next cell is out of bounds
            if next_row < 0 or next_row >= num_rows or next_col < 0 or next_col >= num_cols:
                continue

            # Check if the next cell is empty
            if next_state[next_row][next_col] == 0:
                next_state[next_row][next_col] = current_state[curr_row][curr_col]
                next_state[curr_row][curr_col] = 0
            # Check if the next cell has the same value as the current cell
            elif next_state[next_row][next_col] == current_state[curr_row][curr_col]:
                next_state[next_row][next_col] *= 2
                next_state[curr_row][curr_col] = 0

    return next_state

def get_input():
    current_state = []
    for i in range(4):
        current_state.append(list(map(int, input().split())))
    direction = int(input())
    return current_state, direction

if __name__ == '__main__':
    current_state, direction = get_input()
    next_state = get_next_state(current_state, direction)
    for row in next_state:
        print(*row)

