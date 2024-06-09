
def solve(N, K, healths):
    # Initialize variables
    attacks = 0
    special_move = K
    healths = sorted(healths, reverse=True)

    # Loop through the monsters
    for i in range(N):
        # If the monster's health is 1, we can win without using Special Move
        if healths[i] == 1:
            return attacks

        # If we have Special Move left, use it
        if special_move > 0:
            special_move -= 1
            healths[i] = 0

        # Otherwise, do Attack
        else:
            attacks += 1
            healths[i] -= 1

    # If we reach this point, all monsters' healths are greater than 1, so we need to do Attack more times
    return attacks + N

