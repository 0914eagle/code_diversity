
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is within the range of the torpedo
        if ship[0] <= n and ship[1] >= -n:
            # Check if the ship is on the same y-coordinate as the torpedo
            if ship[2] == 0:
                # If the ship is on the same y-coordinate as the torpedo, it cannot be avoided
                return "impossible"
            # Check if the ship is above or below the torpedo
            elif ship[2] > 0:
                # If the ship is above the torpedo, add a "+" instruction
                instructions.append("+")
            else:
                # If the ship is below the torpedo, add a "-" instruction
                instructions.append("-")

    # If all ships can be avoided, return the instructions
    return "".join(instructions)

