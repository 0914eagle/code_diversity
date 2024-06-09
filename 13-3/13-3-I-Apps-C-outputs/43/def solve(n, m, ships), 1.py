
def solve(n, m, ships):
    # Initialize a list to store the instructions
    instructions = []

    # Loop through each ship and check if it can be avoided
    for ship in ships:
        # Check if the ship is within the range of the torpedo
        if ship[0] <= n and ship[1] >= -n:
            # Check if the ship is already hit
            if ship[0] in instructions or ship[1] in instructions:
                return "impossible"
            # Add the ship's endpoints to the instructions
            instructions.extend([ship[0], ship[1]])

    # If all ships are avoided, return the instructions
    return "".join(instructions)

