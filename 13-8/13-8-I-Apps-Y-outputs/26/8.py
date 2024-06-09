
def solve(H, n, d):
    # Initialize the monster's hit points
    hp = H
    # Initialize the minute counter
    minute = 0
    # Loop through each minute of the battle
    while hp > 0:
        # Update the monster's hit points according to the given sequence
        for i in range(n):
            hp += d[i]
        # Increment the minute counter
        minute += 1
        # If the monster's hit points become negative, return -1
        if hp <= 0:
            return -1
    # If the battle continues infinitely, return -1
    return minute

