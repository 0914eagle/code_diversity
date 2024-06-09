
def solve(H, n, d):
    # Initialize the monster's hit points
    hp = H
    # Iterate through each round
    for i in range(n):
        # Update the monster's hit points based on the damage dealt in the current round
        hp += d[i]
        # If the monster's hit points drop to zero or below, return the current round number
        if hp <= 0:
            return i + 1
    # If the battle continues infinitely, return -1
    return -1

