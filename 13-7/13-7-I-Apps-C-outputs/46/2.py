
def reconstruct_arrows(N, K, moves):
    # Initialize a list to store the arrows
    arrows = [0] * N
    # Iterate through the moves
    for i in range(N):
        # Find the next position of the current dancer
        next_pos = moves[i] - 1
        # If the next position is not the current position, add an arrow from the current position to the next position
        if next_pos != i:
            arrows[i] = next_pos
    # Return the arrows
    return arrows

