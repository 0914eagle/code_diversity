
def reconstruct_arrows(N, K, moves):
    # Initialize a dictionary to map each person to their next move
    person_to_move = {i: i for i in range(1, N + 1)}
    # Initialize a set to keep track of the visited moves
    visited_moves = set()
    # Initialize a list to store the arrows
    arrows = []

    # Loop through each move
    for i in range(K):
        # Get the current person and their next move
        current_person = person_to_move[i]
        next_move = moves[current_person - 1]

        # If the next move is not visited before, add it to the visited moves set
        if next_move not in visited_moves:
            visited_moves.add(next_move)
            # Add the arrow from the current person to the next move
            arrows.append((i, next_move))
            # Update the person_to_move dictionary with the new move
            person_to_move[i] = next_move

    # If all moves are visited, return the arrows list
    if len(visited_moves) == N:
        return arrows
    else:
        return "Impossible"

