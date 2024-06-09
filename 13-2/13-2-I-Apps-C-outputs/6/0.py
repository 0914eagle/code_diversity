
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is already passed by the torpedo
        if ship[0] < 0 and ship[1] < 0:
            continue

        # Check if the ship is already hit by the torpedo
        if ship[0] > n and ship[1] > n:
            continue

        # Check if the ship is in the range of the torpedo
        if ship[0] <= n and ship[1] >= 0:
            # Add the instruction to avoid the ship
            instructions.append("-")
        else:
            # Add the instruction to hit the ship
            instructions.append("+")

    # Check if all the ships are avoided
    if len(instructions) == m:
        return "".join(instructions)
    else:
        return "impossible"

