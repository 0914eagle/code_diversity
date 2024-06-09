
def solve(n, k, health):
    # Initialize variables
    attacks = 0
    special_moves = k
    health = sorted(health, reverse=True)

    # Loop through the monsters
    for i in range(n):
        # If the monster's health is 1, we can use a special move on it
        if health[i] == 1:
            special_moves -= 1
            if special_moves == 0:
                break
        # Otherwise, we need to attack it
        else:
            attacks += 1
            health[i] -= 1

    # Return the number of attacks needed
    return attacks

