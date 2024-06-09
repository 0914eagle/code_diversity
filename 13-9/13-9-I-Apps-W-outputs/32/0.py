
def solve(n, k, initial_state):
    # Initialize the state of the chips
    state = list(initial_state)

    # Iterate over the number of iterations
    for i in range(k):
        # Iterate over the chips
        for j in range(n):
            # Get the neighbors of the current chip
            neighbors = get_neighbors(j, n)

            # Count the number of white and black chips among the neighbors
            num_white, num_black = 0, 0
            for neighbor in neighbors:
                if state[neighbor] == "W":
                    num_white += 1
                else:
                    num_black += 1

            # Check if the current chip should become white or black
            if num_white > num_black:
                state[j] = "W"
            else:
                state[j] = "B"

    # Return the final state of the chips
    return "".join(state)

def get_neighbors(i, n):
    # Handle the edge cases
    if i == 0:
        return [n-1, 1, 2]
    elif i == n-1:
        return [n-2, n-1, 0]
    else:
        return [i-1, i, i+1]

