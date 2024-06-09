
def solve(N, K, health):
    # Initialize variables
    attacks = 0
    special_moves = K
    health = sorted(health, reverse=True)

    # Loop through the monsters
    for i in range(N):
        # If the monster's health is 1, we can use Special Move to kill it
        if health[i] == 1:
            special_moves -= 1
            if special_moves == 0:
                break
        # Otherwise, we need to do Attack
        else:
            attacks += 1
            health[i] -= 1

    # Return the number of Attacks needed
    return attacks

