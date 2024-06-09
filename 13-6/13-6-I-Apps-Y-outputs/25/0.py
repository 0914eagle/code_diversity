
def solve(N, K, health):
    # Initialize variables
    attacks = 0
    special_moves = K
    monsters_alive = N

    # Sort the health array in descending order
    health.sort(reverse=True)

    # Loop through the health array
    for i in range(N):
        # If the current monster's health is 1, we can win without using Special Move
        if health[i] == 1:
            return attacks + 1

        # If the current monster's health is 2 and we have Special Move available, use it
        if health[i] == 2 and special_moves > 0:
            special_moves -= 1
            monsters_alive -= 1
            continue

        # Otherwise, do an Attack
        attacks += 1
        health[i] -= 1

        # If the current monster's health is 0, we can win without using Special Move
        if health[i] == 0:
            monsters_alive -= 1
            if monsters_alive == 0:
                return attacks

    # If we reach this point, we need to do an additional Attack to win
    return attacks + 1

