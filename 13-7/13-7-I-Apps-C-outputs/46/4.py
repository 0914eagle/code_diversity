
def reconstruct_arrows(N, K, moves):
    # Initialize a dictionary to map each person to their next move
    person_to_move = {i: i for i in range(1, N + 1)}
    # Initialize a set to keep track of the moves that have been made
    made_moves = set()
    # Loop through each move and update the dictionary and set
    for move in moves:
        person_to_move[move] = person_to_move[move - 1]
        made_moves.add(move)
    # Check if all moves have been made
    if len(made_moves) == K:
        # If all moves have been made, return the dictionary as the solution
        return [person_to_move[i] for i in range(1, N + 1)]
    else:
        # If not all moves have been made, return "Impossible"
        return "Impossible"

