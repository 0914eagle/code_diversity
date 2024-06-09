
def solve(H, n, d):
    # Initialize the monster's hit points
    hp = H
    # Iterate through each minute of the battle
    for i in range(n):
        # Update the monster's hit points
        hp += d[i]
        # If the monster's hit points are less than or equal to 0, return the current minute
        if hp <= 0:
            return i+1
    # If the battle continues infinitely, return -1
    return -1

