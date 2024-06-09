
def solve(H, n, d):
    # Initialize the monster's hit points
    hp = H
    # Iterate through each minute of the battle
    for i in range(n):
        # Update the monster's hit points
        hp += d[i]
        # If the monster's hit points are reduced to zero or less, return the current minute
        if hp <= 0:
            return i
    # If the battle continues infinitely, return -1
    return -1

