
def reconstruct_arrows(N, K, moves):
    # Initialize a dictionary to map each person to their next move
    person_to_move = {i: i for i in range(1, N + 1)}
    # Initialize a set to keep track of the visited moves
    visited_moves = set()
    # Initialize a list to store the final arrows
    arrows = []
    
    # Iterate through the moves
    for i in range(K):
        # Get the current person and their next move
        current_person = moves[i]
        next_move = person_to_move[current_person]
        
        # If the next move is not visited yet, add it to the visited moves set
        if next_move not in visited_moves:
            visited_moves.add(next_move)
            # Add the arrow from the current person to the next move
            arrows.append((current_person, next_move))
            # Update the person_to_move dictionary with the new move
            person_to_move[current_person] = next_move
    
    return arrows

