
def get_new_state(state, direction):
    # Initialize the new state with the current state
    new_state = state.copy()

    # Get the number of rows and columns in the state
    num_rows, num_cols = len(state), len(state[0])

    # Loop through each row and column
    for i in range(num_rows):
        for j in range(num_cols):
            # Get the current cell value
            current_value = state[i][j]

            # Check if the current cell is not empty
            if current_value != 0:
                # Get the new row and column indices based on the direction
                if direction == 0:  # left
                    new_i, new_j = i, j - 1
                elif direction == 1:  # up
                    new_i, new_j = i - 1, j
                elif direction == 2:  # right
                    new_i, new_j = i, j + 1
                else:  # down
                    new_i, new_j = i + 1, j

                # Check if the new cell is within the bounds of the grid
                if 0 <= new_i < num_rows and 0 <= new_j < num_cols:
                    # Get the new cell value
                    new_value = state[new_i][new_j]

                    # Check if the new cell is empty or if the current cell can merge with the new cell
                    if new_value == 0 or current_value == new_value:
                        # Set the new cell value to the sum of the current cell value and the new cell value
                        new_state[new_i][new_j] = current_value + new_value

                        # Set the current cell value to 0
                        new_state[i][j] = 0

    return new_state

def main():
    # Get the input state and direction
    state = [[int(x) for x in input().split()] for _ in range(4)]
    direction = int(input())

    # Get the new state
    new_state = get_new_state(state, direction)

    # Print the new state
    for row in new_state:
        print(*row)

if __name__ == '__main__':
    main()

