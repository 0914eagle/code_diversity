
def solve(N, K, H):
    # Initialize variables
    attack_count = 0
    special_move_count = 0
    monsters_alive = N

    # Sort the health values in descending order
    H.sort(reverse=True)

    # Loop through the monsters and attack them
    for i in range(N):
        # If Fennec has used all her special moves, attack the monster with the lowest health
        if special_move_count == K:
            H[i] -= 1
        # Otherwise, use a special move on the monster with the lowest health
        else:
            special_move_count += 1
            H[i] = 0

        # Check if any monsters are still alive
        if H[i] > 0:
            monsters_alive -= 1

        # If all monsters are dead, break the loop
        if monsters_alive == 0:
            break

    # Return the number of attacks Fennec needs to do before winning
    return attack_count

