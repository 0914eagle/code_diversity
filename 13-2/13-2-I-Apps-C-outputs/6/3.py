
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

        # Check if the ship is within the range of the torpedo
        if ship[0] > n or ship[1] > n:
            return "impossible"

        # Add the instruction to avoid the ship
        instructions.append("-")

    # If all ships are avoided, return the instructions
    return "".join(instructions)

