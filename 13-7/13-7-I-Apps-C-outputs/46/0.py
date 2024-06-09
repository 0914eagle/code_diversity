
def reconstruct_arrows(N, K, moves):
    # Initialize a dictionary to map each person to their next move
    person_to_move = {i: moves[i-1] for i in range(1, N+1)}
    # Initialize a set to keep track of the visited moves
    visited_moves = set()
    # Initialize a list to store the arrows
    arrows = []
    
    # Loop through each move and construct the arrows
    for i in range(K):
        # Get the current person and their next move
        current_person = i % N + 1
        next_move = person_to_move[current_person]
        
        # If the next move has not been visited before, add it to the arrows list
        if next_move not in visited_moves:
            arrows.append(next_move)
            visited_moves.add(next_move)
        # If the next move has been visited before, add it to the arrows list and update the person_to_move dictionary
        else:
            arrows.append(next_move)
            person_to_move[current_person] = next_move
    
    # If the number of arrows is not equal to the number of people, return "Impossible"
    if len(arrows) != N:
        return "Impossible"
    
    # Return the arrows list
    return arrows

