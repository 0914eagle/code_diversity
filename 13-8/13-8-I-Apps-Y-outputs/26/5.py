
def solve(H, n, d):
    # Initialize the monster's hp to its initial value
    hp = H
    # Iterate through each minute of the battle
    for i in range(n):
        # Update the monster's hp according to the given sequence
        hp += d[i]
        # If the monster's hp becomes negative or zero, return the current minute
        if hp <= 0:
            return i+1
    # If the battle continues infinitely, return -1
    return -1

