
def avoid_ships(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is already outside the range of the torpedo
        if ship[0] > n or ship[1] < -n:
            continue

        # Check if the ship is within the range of the torpedo
        if -n <= ship[0] <= n and -n <= ship[1] <= n:
            # Add the instruction to avoid the ship
            instructions.append("-")
        else:
            # Add the instruction to go straight
            instructions.append("0")

    # Return the instructions
    return "".join(instructions)

