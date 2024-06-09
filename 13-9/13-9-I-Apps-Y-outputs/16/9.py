
def solve(H, n, d):
    # Initialize the monster's hit points
    hp = H
    # Initialize the minute counter
    minute = 0
    # Loop through each minute of the battle
    while minute < n:
        # Add the change in hit points for the current minute
        hp += d[minute]
        # Check if the monster has died
        if hp <= 0:
            return minute + 1
        # Increment the minute counter
        minute += 1
    # If the battle continues infinitely, return -1
    return -1

